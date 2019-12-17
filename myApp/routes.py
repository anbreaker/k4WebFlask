from myApp import app
from flask import render_template
import csv

# Decorador
@app.route('/')
def index():
    # Funcionalindad necesaria para obtener los datos y pasar a index.html
    # Leer el fichero sales10.csv

    fSales = open('../data/sales10.csv', 'r')  # modo lectura

    csvReader = csv.reader(fSales, delimiter=',')  # Instancia manejador de csv
    registros = []
    for linea in csvReader:
        registros.append(linea)

    cabecera = registros[0]
    ventas = []
    for datos in registros[1:]:
        diccionario = {}
        for ix, nombreCampo in enumerate(cabecera):
            diccionario[nombreCampo] = datos[ix]
        ventas.append(diccionario)

    # procesrar para obtener totales

    resultado = {}  # Lista de diccionarios
    '''
    {'region':'Australia y oceania','Ingresos totales':3292856.72, 'Beneficios Totales':123654.36}
    {'region':'Central America and the Caribbean','Ingresos totales':3292856.72, 'Beneficios Totales':123654.36}
    '''

    # enviarlo a index html

    return render_template('index.html', registros=resultado)


# Decorador
@app.route('/detail')
def detail():
    return render_template('detail.html')
