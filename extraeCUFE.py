import os
import re
import sqlite3
import PyPDF2
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

# Expresión regular para CUFE
CUFE_PATTERN = re.compile(r"\b([0-9a-fA-F]\n*){95,100}\b")

# Obtener la ruta absoluta de la base de datos
db_path = os.path.abspath("facturas.db")

# Conectar a la base de datos SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS facturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_archivo TEXT UNIQUE,
        numero_paginas INTEGER,
        cufe TEXT UNIQUE,
        peso_archivo_kb REAL
    )
''')
conn.commit()

# ------------------- FUNCIONES -------------------

def extraer_cufe(texto):
    """Extrae el CUFE del texto usando la expresión regular."""
    match = CUFE_PATTERN.search(texto)
    return match.group(0).replace("\n", "") if match else "No encontrado"

def archivo_ya_cargado(nombre_archivo):
    """Verifica si el archivo ya existe en la base de datos."""
    cursor.execute("SELECT 1 FROM facturas WHERE nombre_archivo = ?", (nombre_archivo,))
    return cursor.fetchone() is not None

def cufe_ya_existe(cufe):
    """Verifica si el CUFE ya existe en la base de datos."""
    cursor.execute("SELECT 1 FROM facturas WHERE cufe = ?", (cufe,))
    return cursor.fetchone() is not None

def procesar_pdfs(rutas_pdfs):
    """Procesa múltiples archivos PDF, evita duplicados y actualiza la tabla."""
    if not rutas_pdfs:
        messagebox.showwarning("Aviso", "No se seleccionaron archivos PDF.")
        return

    for ruta_pdf in rutas_pdfs:
        try:
            nombre_archivo = os.path.basename(ruta_pdf)

            if archivo_ya_cargado(nombre_archivo):
                messagebox.showwarning("Archivo Duplicado", f"El archivo '{nombre_archivo}' ya fue cargado previamente.")
                continue

            with open(ruta_pdf, "rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                num_paginas = len(pdf_reader.pages)
                texto_completo = ""

                for page in pdf_reader.pages:
                    texto_completo += page.extract_text() or ""

                cufe = extraer_cufe(texto_completo)

                if cufe_ya_existe(cufe):
                    messagebox.showwarning("CUFE Duplicado", f"El CUFE '{cufe}' ya existe en la base de datos.")
                    continue

                peso_kb = os.path.getsize(ruta_pdf) / 1024

                cursor.execute('''
                    INSERT INTO facturas (nombre_archivo, numero_paginas, cufe, peso_archivo_kb)
                    VALUES (?, ?, ?, ?)
                ''', (nombre_archivo, num_paginas, cufe, peso_kb))
                conn.commit()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo procesar {nombre_archivo}: {e}")

    actualizar_tabla()

def seleccionar_pdfs():
    """Abre un cuadro de diálogo para seleccionar múltiples archivos PDF y procesarlos."""
    rutas_pdfs = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    if rutas_pdfs:
        procesar_pdfs(rutas_pdfs)

def actualizar_tabla():
    """Consulta la base de datos y actualiza la tabla con los registros."""
    limpiar_tabla()
    cursor.execute("SELECT nombre_archivo, numero_paginas, cufe, peso_archivo_kb FROM facturas")
    registros = cursor.fetchall()

    for registro in registros:
        tabla.insert("", "end", values=registro)

def limpiar_tabla():
    """Limpia todos los registros de la tabla en la interfaz sin afectar la base de datos."""
    for row in tabla.get_children():
        tabla.delete(row)

def mostrar_ubicacion_bd():
    """Muestra la ubicación del archivo de la base de datos en un mensaje."""
    messagebox.showinfo("Ubicación de la Base de Datos", f"La base de datos se encuentra en:\n{db_path}")

def cerrar_ventana():
    """Pregunta al usuario si desea cerrar la aplicación y la cierra si confirma."""
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres cerrar la aplicación?")
    if respuesta:
        conn.close()  
        root.destroy()

# ------------------- INTERFAZ -------------------

root = tk.Tk()
root.title("Extractor de CUFE desde PDFs")
root.geometry("950x550")  
root.resizable(False, False)

# Estilo Moderno con ttk
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6, relief="flat")
style.configure("TLabel", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
style.configure("Treeview", rowheight=25)

# Frame Principal
frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Título
lbl_titulo = ttk.Label(frame, text="Extractor de CUFE desde PDFs", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=5)

# Botones organizados en una fila
frame_botones = ttk.Frame(root)
frame_botones.pack(pady=10)

btn_seleccionar = ttk.Button(frame_botones, text="📂 Seleccionar PDFs", command=seleccionar_pdfs)
btn_seleccionar.grid(row=0, column=0, padx=5)

btn_cargar = ttk.Button(frame_botones, text="📋 Cargar Registros", command=actualizar_tabla)
btn_cargar.grid(row=0, column=1, padx=5)

btn_limpiar = ttk.Button(frame_botones, text="🔄 Limpiar", command=limpiar_tabla)
btn_limpiar.grid(row=0, column=2, padx=5)

btn_ver_bd = ttk.Button(frame_botones, text="📍 Ver Ubicación BD", command=mostrar_ubicacion_bd)
btn_ver_bd.grid(row=0, column=3, padx=5)

btn_salir = ttk.Button(frame_botones, text="❌ Salir", command=cerrar_ventana)
btn_salir.grid(row=0, column=4, padx=5)

# Tabla con Scroll y Estilo
frame_tabla = ttk.Frame(root)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

columnas = ("Nombre del Archivo", "Páginas", "CUFE", "Tamaño (KB)")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=220 if col == "CUFE" else 160)

# Alternar colores en filas
tabla.tag_configure("evenrow", background="#f0f0f0")

scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")
tabla.pack(fill="both", expand=True)

# Cargar Datos Iniciales
actualizar_tabla()

root.mainloop()
