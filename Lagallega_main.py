from LaGallega_scraping import scrapear_categoria

def main():
    archivo_excel = 'productos_lagallega.xlsx'

    print("Iniciando scraping de ofertas...")
    scrapear_categoria('Ofertas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=&TM=CM', 62, archivo_excel)

    print("Iniciando scraping de aceites y vinagres...")
    scrapear_categoria('Aceites y Vinagres', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03010000', 4,
                       archivo_excel)

    print("Iniciando scraping de copetin...")
    scrapear_categoria('Copetin', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03110000', 6, archivo_excel)

    print("Iniciando scraping de Arroz y Legumbres...")
    scrapear_categoria('Arroz y Legumbres', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03020000', 5,
                       archivo_excel)

    print("Iniciando scraping de Enlatados y Conservas...")
    scrapear_categoria('Enlatados y Conservas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03020000', 10,
                       archivo_excel)

    print("Iniciando scraping de Azucar y Edulcorantes...")
    scrapear_categoria('Azucar y Edulcorantes', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03080000', 4,
                       archivo_excel)

    print("Iniciando scraping de Frutos Secos y Semillas...")
    scrapear_categoria('Frutos Secos y Semillas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03120000', 3,
                       archivo_excel)

    print("Iniciando scraping de Cacao...")
    scrapear_categoria('Cacao', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03100000&TM=cx', 2,
                       archivo_excel)

    print("Iniciando scraping de Golosinas...")
    scrapear_categoria('Golosinas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03070000', 8,
                       archivo_excel)

    print("Iniciando scraping de Celiacos...")
    scrapear_categoria('Celiacos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03170000', 5,
                       archivo_excel)

    print("Iniciando scraping de Harinas...")
    scrapear_categoria('Harinas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03030000', 3,
                       archivo_excel)

    print("Iniciando scraping de Condimentos y Especias...")
    scrapear_categoria('Condimentos y Especias', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03090000', 6,
                       archivo_excel)

    print("Iniciando scraping de Huevos...")
    scrapear_categoria('Huevos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=03190000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Accesorios")
    scrapear_categoria('Bazar - Accesorios', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05050000', 9,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Aire Libre")
    scrapear_categoria('Bazar - Aire Libre', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05080000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Baño")
    scrapear_categoria('Bazar - Baño', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05020000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Pilas")
    scrapear_categoria('Bazar - Pilas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05010000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Plasticos")
    scrapear_categoria('Bazar - Plasticos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05060000', 6,
                       archivo_excel)

    print("Iniciando scraping de Bazar - Utensillos de Cocina")
    scrapear_categoria('Bazar - Utiensillos de Cocina',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05040000', 6, archivo_excel)

    print("Iniciando scraping de Bazar - Vajilla")
    scrapear_categoria('Bazar - Vajilla', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=05030000', 7,
                       archivo_excel)

    print("Iniciando scraping de Aguas")
    scrapear_categoria('Aguas', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=07060000', 6,
                       archivo_excel)

    print("Iniciando scraping de Aperitivos")
    scrapear_categoria('Aperitivos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07030000', 5,
                       archivo_excel)

    print("Iniciando scraping de Bebidas Blancas")
    scrapear_categoria('Bebidas Blancas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07040000', 7,
                       archivo_excel)

    print("Iniciando scraping de Cervezas")
    scrapear_categoria('Cervezas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07010000', 8,
                       archivo_excel)

    print("Iniciando scraping de Energizantes")
    scrapear_categoria('Energizantes', 'https://www.lagallega.com.ar/productosnl.asp?pg=2&nl=07080000', 3,
                       archivo_excel)

    print("Iniciando scraping de Espumantes, Sidras y Frizzantes")
    scrapear_categoria('Espumantes, Sidras y Frizzantes',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07090000', 8, archivo_excel)

    print("Iniciando scraping de Gaseosas")
    scrapear_categoria('Gaseosas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07050000', 5, archivo_excel)

    print("Iniciando scraping de Jugos")
    scrapear_categoria('Jugos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07070000', 8, archivo_excel)

    print("Iniciando scraping de Vinos")
    scrapear_categoria('Vinos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=07020000', 8, archivo_excel)

    print("Iniciando scraping de Carbon y Encendido")
    scrapear_categoria('Carbón y Encendido', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13070000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Carne de Cerdo")
    scrapear_categoria('Carne de Cerdo', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13020000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Carnes Blancas")
    scrapear_categoria('Carnes Blancas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13010000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Carnes Rojas")
    scrapear_categoria('Carnes Rojas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13030000', 8,
                       archivo_excel)

    print("Iniciando scraping de Embutidos")
    scrapear_categoria('Embutidos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13040000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Grasas")
    scrapear_categoria('Grasas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13050000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Menudencias")
    scrapear_categoria('Menudencias', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=13060000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Frutas y Vegetales Congelados")
    scrapear_categoria('Frutas y Vegetales Congelados',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15070000', 3, archivo_excel)

    print("Iniciando scraping de Hamburguesas, Pizas y Empanadas")
    scrapear_categoria('Hamburguesas, Pizas y Empanadas',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15020000', 4, archivo_excel)

    print("Iniciando scraping de Medallones de Arroz y Legumbres")
    scrapear_categoria('Medallones de Arroz y Legumbres',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15030000&TM=cx', 1, archivo_excel)

    print("Iniciando scraping de Milanesas de Soja")
    scrapear_categoria('Milanesas de Soja', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15040000', 3,
                       archivo_excel)

    print("Iniciando scraping de Papas Congeladas")
    scrapear_categoria('Papas Congeladas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15080000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pastas Congeladas")
    scrapear_categoria('Pastas Congeladas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15090000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pezcados")
    scrapear_categoria('Pezcados', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15060000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pollo y Carne")
    scrapear_categoria('Pollo y Carne', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=15010000', 3,
                       archivo_excel)

    print("Iniciando scraping de Cumpleaños")
    scrapear_categoria('Cumpleaños', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=09000000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Cafe")
    scrapear_categoria('Cafe', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06040000', 8, archivo_excel)

    print("Iniciando scraping de Cereales")
    scrapear_categoria('Cereales', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06060000', 5, archivo_excel)

    print("Iniciando scraping de Dulces y Mermeladas")
    scrapear_categoria('Dulces y Mermeladas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06030000', 3,
                       archivo_excel)

    print("Iniciando scraping de Galletitas")
    scrapear_categoria('Galletitas', 'https://www.lagallega.com.ar/productosnl.asp?pg=2&nl=06010000', 8, archivo_excel)

    print("Iniciando scraping de Te")
    scrapear_categoria('Te', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06050000', 5, archivo_excel)

    print("Iniciando scraping de Tostadas")
    scrapear_categoria('Tostadas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06020000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Yerba")
    scrapear_categoria('Yerba', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=06070000', 7, archivo_excel)

    print("Iniciando scraping de Climatizacion")
    scrapear_categoria('Climatizacion', 'https://www.lagallega.com.ar/productosnl.asp?pg=2&nl=04010000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Electrodomesticos Pequeños")
    scrapear_categoria('Electrodomesticos Pequeños', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=04020000',
                       3, archivo_excel)

    print("Iniciando scraping de Fiestas")
    scrapear_categoria('Fiestas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=02000000', 3, archivo_excel)

    print("Iniciando scraping de Frutas")
    scrapear_categoria('Frutas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=19010000', 4, archivo_excel)

    print("Iniciando scraping de Vegetales")
    scrapear_categoria('Vegetales', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=19020000', 6, archivo_excel)

    print("Iniciando scraping de Jugueteria")
    scrapear_categoria('Jugueteria', 'https://www.lagallega.com.ar/productosnl.asp?pg=2&nl=11000000', 7, archivo_excel)

    print("Iniciando scraping de Cremas")
    scrapear_categoria('Cremas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08010000', 3, archivo_excel)

    print("Iniciando scraping de Fiambres")
    scrapear_categoria('Fiambres', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08080000', 6, archivo_excel)

    print("Iniciando scraping de Leche")
    scrapear_categoria('Leche', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08020000', 7, archivo_excel)

    print("Iniciando scraping de Mantecas y Margarinas")
    scrapear_categoria('Mantecas y Margarinas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08030000', 3,
                       archivo_excel)

    print("Iniciando scraping de Pastas Frescas y Tapas")
    scrapear_categoria('Pastas Frescas y Tapas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08110000', 5,
                       archivo_excel)

    print("Iniciando scraping de Postres y Flanes")
    scrapear_categoria('Postres y Flanes', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08040000', 3,
                       archivo_excel)

    print("Iniciando scraping de Quesos")
    scrapear_categoria('Quesos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08050000', 9, archivo_excel)

    print("Iniciando scraping de Ricota")
    scrapear_categoria('Ricota', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08060000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Salchichas")
    scrapear_categoria('Salchichas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08100000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Yogures")
    scrapear_categoria('Yogures', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=08070000', 10, archivo_excel)

    print("Iniciando scraping de Libreria")
    scrapear_categoria('Libreria', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=10000000', 7, archivo_excel)

    print("Iniciando scraping de Limpieza")
    scrapear_categoria('Limpieza', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16010000', 8, archivo_excel)

    print("Iniciando scraping de Automoviles")
    scrapear_categoria('Automoviles', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=16020000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Limpieza Baño")
    scrapear_categoria('Limpieza Baño', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16030000', 3, archivo_excel)

    print("Iniciando scraping de Broches de ropa")
    scrapear_categoria('Broches de ropa', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=16150000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Betun")
    scrapear_categoria('Betun', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=16160000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Limpieza de cocina")
    scrapear_categoria('Limpieza de cocina', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16040000', 5,
                       archivo_excel)

    print("Iniciando scraping de Desodorante de ambiente")
    scrapear_categoria('Desodorante de ambiente', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16100000', 4,
                       archivo_excel)

    print("Iniciando scraping de Destapa Cañerias")
    scrapear_categoria('Destapa Cañerias', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=16060000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Insecticidas")
    scrapear_categoria('Insecticidas', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16070000', 4, archivo_excel)

    print("Iniciando scraping de Jabon para la ropa")
    scrapear_categoria('Jabon para la ropa', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16170000', 6,
                       archivo_excel)

    print("Iniciando scraping de Lavandinas")
    scrapear_categoria('Lavandinas', 'https://lagallega.com.ar/productosnl.asp?pg={}&nl=16080000', 3, archivo_excel)

    print("Iniciando scraping de Mascotas - Aves")
    scrapear_categoria('Mascotas - Aves', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=18010000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Mascotas - Gatos")
    scrapear_categoria('Mascotas - Gatos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=18020000', 4,
                       archivo_excel)

    print("Iniciando scraping de Mascotas - Perros")
    scrapear_categoria('Mascotas - Perros', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=18030000', 5,
                       archivo_excel)

    print("Iniciando scraping de Bebe - Absorventes")
    scrapear_categoria('Bebe - Absorventes', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17010000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Bebe - Accesorios")
    scrapear_categoria('Bebe - Accesorios', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17100000', 3,
                       archivo_excel)

    print("Iniciando scraping de Bebe - Aceite y Baños")
    scrapear_categoria('Bebe - Aceite y Baños', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17020000&TM=cx',
                       1, archivo_excel)

    print("Iniciando scraping de Bebe - Colonias y Jabones")
    scrapear_categoria('Bebe - Colonias y Jabones',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17030000&TM=cx', 1, archivo_excel)

    print("Iniciando scraping de Bebe - Cremas y Talcos")
    scrapear_categoria('Bebe - Cremas y Talcos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17040000&TM=cx',
                       1, archivo_excel)

    print("Iniciando scraping de Bebe - Leches y Alimentos")
    scrapear_categoria('Bebe - Leches y Alimentos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17050000', 4,
                       archivo_excel)

    print("Iniciando scraping de Bebe - Pañales")
    scrapear_categoria('Bebe - Pañales', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17060000', 5,
                       archivo_excel)

    print("Iniciando scraping de Bebe - Protectores Mamarios")
    scrapear_categoria('Bebe - Protectores Mamarios',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17070000&TM=cx', 1, archivo_excel)

    print("Iniciando scraping de Bebe - Shampoo y Enjuague")
    scrapear_categoria('Bebe - Shampoo y Enjuague', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17080000', 3,
                       archivo_excel)

    print("Iniciando scraping de Bebe-Toallitas Humedas y Oleos")
    scrapear_categoria('Bebe-Toallitas Humedas y Oleos',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=17090000', 3, archivo_excel)

    print("Iniciando scraping de Bizcochos y Facturas")
    scrapear_categoria('Bizcochos y Facturas',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14010000&TM=cx', 1, archivo_excel)

    print("Iniciando scraping de Budines y Pan Dulce")
    scrapear_categoria('Budines y Pan Dulce', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14020000', 3,
                       archivo_excel)

    print("Iniciando scraping de Levaduras")
    scrapear_categoria('Levaduras', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14030000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pan")
    scrapear_categoria('Pan', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14040000', 6, archivo_excel)

    print("Iniciando scraping de Pionono")
    scrapear_categoria('Pionono', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14050000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Postres y Masas")
    scrapear_categoria('Postres y Masas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14060000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pre-Pizas")
    scrapear_categoria('Pre-Pizas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14070000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Tortillas y Tacos")
    scrapear_categoria('Tortillas y Tacos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=14080000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Pascuas")
    scrapear_categoria('Pascuas', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=21000000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Afeitado")
    scrapear_categoria('Afeitado', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20010000', 3, archivo_excel)

    print("Iniciando scraping de Algodones e Hisopos")
    scrapear_categoria('Algodones e Hisopos', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20020000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Colonias")
    scrapear_categoria('Colonias', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20030000&TM=cx', 1,
                       archivo_excel)

    print("Iniciando scraping de Cuidado de la Piel")
    scrapear_categoria('Cuidado de la Piel', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20040000', 10,
                       archivo_excel)

    print("Iniciando scraping de Cuidado del Cabello")
    scrapear_categoria('Cuidado del Cabello', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20130000', 8,
                       archivo_excel)

    print("Iniciando scraping de Desodorantes")
    scrapear_categoria('Desodorantes', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20060000', 7,
                       archivo_excel)

    print("Iniciando scraping de Farmacia")
    scrapear_categoria('Farmacia', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20070000', 4, archivo_excel)

    print("Iniciando scraping de Higiene Bucal")
    scrapear_categoria('Higiene Bucal', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20080000', 8,
                       archivo_excel)

    print("Iniciando scraping de Jabones")
    scrapear_categoria('Jabones', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20090000', 10, archivo_excel)

    print("Iniciando scraping de Proteccion Femenina")
    scrapear_categoria('Proteccion Femenina', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20100000', 8,
                       archivo_excel)

    print("Iniciando scraping de Protectores Solares y Bronceadores")
    scrapear_categoria('Protectores y Bronceadores',
                       'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20110000', 3, archivo_excel)

    print("Iniciando scraping de Talco")
    scrapear_categoria('Talco', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=20050000', 3, archivo_excel)

    print("Iniciando scraping de Velas y Escencias")
    scrapear_categoria('Velas y Escencias', 'https://www.lagallega.com.ar/productosnl.asp?pg={}&nl=12000000&TM=cx', 1,
                       archivo_excel)

    print("¡Scraping completo!")

if __name__ == '__main__':
    main()
