# 📄 Extractor de CUFE desde PDFs  

**Versión 1.0.0** | 🫠 **Python 3.13.2+** | 🖥️ **Windows / macOS / Linux**  

🚀 Aplicación de escritorio para extraer el **CUFE** de facturas electrónicas en **PDF**, evitando duplicados y mostrando los resultados en una **interfaz moderna** con tabla interactiva.  

---

## 📌 Características  
👉 **Interfaz gráfica profesional con Tkinter y ttk**  
👉 **Carga y análisis de múltiples archivos PDF**  
👉 **Prevención de registros duplicados (archivos y CUFEs)**  
👉 **Almacenamiento local en SQLite**  
👉 **Tabla interactiva (`Treeview`) con scroll y diseño limpio**  
👉 **Botones para limpiar, recargar registros y verificar la ubicación de la base de datos**  
👉 **Totalmente portable y sin necesidad de instalar bases de datos externas**  

---

## 🔧 Requisitos Técnicos  

### 🗉️ **Requisitos del sistema**  
- 👉 **Python 3.13.2+**  
- 👉 **Sistema Operativo:** Windows, macOS o Linux  
- 👉 **Bibliotecas necesarias:** Especificadas en `requirements.txt`  

---

## 🗉️ **Manuales**  
- 👉 **Manual de Usuario**  
- 👉 **Manual Técnico**  

---

## 📦 Instalación  

### **1️⃣ Clonar el repositorio**
```bash
git clone https://github.com/nowen21/prueba-python-adres.git
cd prueba-python-adres

```

### **2️⃣ Instalar dependencias**
Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### **3️⃣ Ejecutar la aplicación**
Para iniciar la aplicación, ejecuta:

```bash
python extraeCUFE.py
```

---

## 🎯 Uso  

1️⃣ Abre la aplicación y selecciona los archivos PDF que contienen las facturas electrónicas.  
2️⃣ La aplicación extraerá automáticamente los CUFE y los mostrará en la tabla interactiva.  
3️⃣ Puedes limpiar, recargar o exportar los registros según sea necesario.  

---

## 🏢 Tecnologías Usadas  
- **Python 3.13.2+**  
- **Tkinter y ttk para la interfaz gráfica**  
- **SQLite para almacenamiento local**  
- **pdfplumber para la extracción de texto desde PDFs**  
- **Pandas para manipulación y organización de datos**  

---

## 📑 Licencia  
Este proyecto está bajo la licencia [MIT](LICENSE).  

---

## 👤 Autor  
Desarrollado por [Ing. José Dúmar Jimémez Ruíz](https://github.com/nowen21).  

