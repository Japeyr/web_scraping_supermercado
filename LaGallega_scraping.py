import bs4
import requests
import pandas as pd

def scrapear_categoria(nombre_hoja, url_base, paginas, nombre_archivo='productos_lagallega.xlsx'):
    datos = []

    for pagina in range(1, paginas + 1):
        url_pagina = url_base.format(pagina)
        resultado = requests.get(url_pagina)
        sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

        productos = sopa.select('.desc')
        precios = sopa.select('.izq')

        for producto, precio in zip(productos, precios):
            nombre = producto.text.strip()
            valor = precio.text.strip()
            datos.append({'Producto': nombre, 'Precio': valor, 'Página': pagina})

    df = pd.DataFrame(datos)

    # Guardar en hoja correspondiente del archivo Excel
    with pd.ExcelWriter(nombre_archivo, engine='openpyxl', mode='a' if pd.io.common.file_exists(nombre_archivo) else 'w') as writer:
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

    print(f"¡Hoja '{nombre_hoja}' escrita con éxito en {nombre_archivo}!")
