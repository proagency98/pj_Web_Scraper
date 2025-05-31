# Web Scraper de Libros

Este proyecto es un web scraper que extrae información de libros del sitio web [Books to Scrape](https://books.toscrape.com/). El scraper recopila datos como nombres, precios y enlaces de los libros, y los guarda en un archivo CSV.

## Características

- Extracción de datos de libros (nombres, precios, enlaces)
- Manejo de errores robusto
- Almacenamiento de datos en formato CSV
- Dashboard interactivo con Streamlit

## Requisitos

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
.
├── scraper.py          # Script principal del scraper
├── dashboard.py        # Dashboard interactivo con Streamlit
├── data/              # Directorio para almacenar los datos
│   └── books.csv      # Archivo CSV con los datos extraídos
└── requirements.txt    # Dependencias del proyecto
```

## Uso

1. Ejecutar el scraper:
```bash
python scraper.py
```

2. Ejecutar el dashboard:
```bash
streamlit run dashboard.py
```

## Datos Extraídos

El scraper extrae la siguiente información de cada libro:
- Nombre del libro
- Precio (en libras esterlinas)
- Enlace al libro

## Tecnologías Utilizadas

- Python
- BeautifulSoup4
- Requests
- Pandas
- Streamlit

## Notas

- El scraper incluye manejo de errores para diferentes situaciones
- Los precios se muestran en libras esterlinas (£)
- El dashboard permite visualizar los datos de forma interactiva
