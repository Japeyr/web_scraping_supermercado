
# 🛒 Web Scraping Supermercado

Este proyecto realiza **Web Scraping** en un sitio de un supermercado utilizando **Python**. Extrae información clave de los productos, como:

- 📌 **Nombre del producto**
- 💲 **Precio**
- 📄 **Número de página de donde se obtuvo**

Cada ejecución guarda los datos en un archivo **Excel**, creando una hoja diferente por cada página scrapeada.

---

## 📌 Tecnologías y Librerías utilizadas

Este proyecto utiliza las siguientes librerías de **Python**:

- **Pandas** 🐼 → Para manipulación y almacenamiento de datos  
- **BeautifulSoup4 (bs4)** 🥣 → Para analizar el HTML de las páginas  
- **lxml** 📄 → Para el procesamiento eficiente de XML y HTML  

---

## 🚀 Instalación y Configuración

**1️⃣ Clonar el repositorio:**

```bash
git clone https://github.com/Japeyr/web_scraping_supermercado.git
cd web_scraping_supermercado
```

**2️⃣ Instalar dependencias:**

```bash
pip install pandas beautifulsoup4 lxml
```

**3️⃣ Ejecutar el script:**

```bash
python Lagallega_main.py
```

---

## 📂 Estructura de archivos

- `Lagallega_main.py` → Script principal de scraping  
- `el archivo Excel` se guarda en la misma carpeta donde estan los archivos del programa  
- `README.md` → Documentación del proyecto  

---

## ⚡ Uso del script

Ejecutá el script con:

```bash
python Lagallega_main.py
```

El programa comenzará a recopilar información de las páginas del supermercado.  
Los datos se guardarán en archivos Excel dentro de la misma carpeta donde se aloja el programa`, con una hoja nueva por cada página scrapeada.


