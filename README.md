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

## 🗉️ **Manuales**  
- 👉 **Manual de Usuario**  
- 👉 **Manual Técnico**  

---

## 🔧 Requisitos Técnicos  

### 🗉️ **Requisitos del sistema**  
- 👉 **Python 3.13.2+**  
- 👉 **Sistema Operativo:** Windows, macOS o Linux  
- 👉 **Bibliotecas necesarias:** Especificadas en `requirements.txt`  

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

## 🏗️ Estructura del Proyecto  
```
PRUEBA-PYTHON-ADRES/
│── manuales/
│   │── Manual_Tecnico_Extractor_CUFE.docx
│   │── Manual_Usuario_Extractor_CUFE.docx
│── extraeCUFE.py
│── facturas.db
│── README.md
│── requirements.txt
```

---

## ✅ Regla de Validación  
### 📌 **Descripción del Problema**  
En una empresa se manejan facturas electrónicas en formato **PDF**, cada una de las cuales contiene un identificador único llamado **CUFE** (Código Único de Factura Electrónica). Se requiere un sistema que extraiga estos códigos automáticamente desde múltiples archivos **PDF**, valide la unicidad de los CUFEs y almacene la información en una base de datos local **SQLite**.

### 🎯 **Objetivo**  
Desarrollar un **script en Python** que lea múltiples archivos PDF, extraiga el **CUFE** de cada factura utilizando **expresiones regulares** y almacene los datos en una base de datos **SQLite**.

---

## 📋 **Reglas de Validación**  

1️⃣ **Expresión Regular para Extraer el CUFE**  
   - El CUFE es una secuencia de **95 a 100 caracteres hexadecimales** (letras y números).  
   - Se extraerá utilizando la siguiente **expresión regular**:  

   ```regex
   \b([0-9a-fA-F]\n*){95,100}\b
   ```

2️⃣ **Requisitos para el almacenamiento en la base de datos**  
   - **a. Nombre del archivo:** Nombre del archivo PDF procesado.  
   - **b. Número de páginas:** Cantidad de páginas en el archivo PDF.  
   - **c. CUFE:** Código único extraído de la factura.  
   - **d. Peso del archivo:** Tamaño del archivo en **kilobytes (KB)**.  

3️⃣ **Validaciones previas al almacenamiento**  
   - Si un archivo **ya ha sido procesado**, **evitar su duplicación** en la base de datos.  
   - Si un **CUFE ya existe**, no almacenarlo nuevamente para evitar registros repetidos.  

---

## 🛠️ **Condiciones de Desarrollo**  
🔹 **Lenguaje:** Python 3.13.2+  
🔹 **Bibliotecas permitidas:**  
   - `pdfplumber`: Para extraer texto de archivos PDF.  
   - `sqlite3`: Para la gestión de la base de datos local SQLite.  
   - `os`: Para obtener el tamaño de los archivos PDF.  
   - `re`: Para aplicar la expresión regular y extraer el CUFE.  

🔹 **Formato de salida esperado:**  
   - Los datos se almacenarán en una **tabla SQLite** con la estructura:  

   ```sql
   CREATE TABLE facturas (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre_archivo TEXT UNIQUE,
       numero_paginas INTEGER,
       cufe TEXT UNIQUE,
       peso_kb REAL
   );
   ```

---

## 📌 **Ejemplo de Entrada y Salida**  

### **Entrada:**  
📄 Archivos PDF en una carpeta:  
```
factura_001.pdf  
factura_002.pdf  
factura_003.pdf  
...
```

### **Salida esperada en la base de datos:**  
| id | nombre_archivo   | numero_paginas | cufe                                      | peso_kb |
|----|-----------------|---------------|------------------------------------------|--------|
| 1  | factura_001.pdf | 2             | 2A3F...9B5D (95-100 caracteres)         | 135.6  |
| 2  | factura_002.pdf | 3             | 1B4C...8E2A (95-100 caracteres)         | 210.4  |

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


