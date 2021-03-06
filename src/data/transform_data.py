"""
Módulo de transformación de datos.
-------------------------------------------------------------------------------
En este modulo se transforman los documentos .xls y .xlsx previamente
descargados en el modulo clean_data.py utilizando las siguientes funciones:

get_files_to_export: obtiene list de la ruta de los 27 archivos de precios.
get_file_name: concatena la ruta a grabar con el nombre del archivo, formando
    el path completo donde se extraen los documentos excel.
format_headers: da formato a las columnas de cada excel en tipo H00
remove_nas: elimina aquellas filas con registros en N/A.
remove_duplicated: elimina filas con registros duplicados, dejando la primera
    observación.
save_file: guarda el archivo transformado en tipo CSV
"""


"""Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    
""""""""   
import doctest
from importlib.metadata import files
import os
import pandas as pd
from datetime import datetime
import openpyxl 
import xlrd

def transform_data():
    files_to_export = get_files_to_export()
    path_to_export = 'data_lake/landing/'
    for files in files_to_export:
        file_name = get_file_name(path_to_export,files)
        if files == 'result.txt':
            break
        if int(files[0:4]) in range(1995,2000):
            print(files[0:4])
            file_to_csv = pd.read_excel(file_name,skiprows=range(1, 3), header=1, usecols = "A:Y")
            file_to_csv_wo_format = file_to_csv.copy()
            file_to_csv_with_header = format_headers(file_to_csv_wo_format)
            file_to_csv_with_dates = format_dates(file_to_csv_with_header)
            file_to_csv_wo_nas = remove_nas(file_to_csv_with_dates)
            file_to_csv_wo_duplicated = remove_duplicated(file_to_csv_wo_nas)
            save_file(file_to_csv_wo_duplicated,files)
        if int(files[0:4]) in range(2000,2016):
            file_to_csv = pd.read_excel(file_name,skiprows=range(1, 2), header=1, usecols = "A:Y")
            file_to_csv_wo_format = file_to_csv.copy()
            file_to_csv_with_header = format_headers(file_to_csv_wo_format)
            file_to_csv_with_dates = format_dates(file_to_csv_with_header)
            file_to_csv_wo_nas = remove_nas(file_to_csv_with_dates)
            file_to_csv_wo_duplicated = remove_duplicated(file_to_csv_wo_nas)
            save_file(file_to_csv_wo_duplicated,files)
        if int(files[0:4]) in range(2016,2018):
            file_to_csv = pd.read_excel(file_name,skiprows=range(1, 2), header=1, usecols = "A:Y")
            file_to_csv_wo_format = file_to_csv.copy()
            file_to_csv_with_header = format_headers(file_to_csv_wo_format)
            file_to_csv_with_dates = format_dates(file_to_csv_with_header)
            file_to_csv_wo_nas = remove_nas(file_to_csv_with_dates)
            file_to_csv_wo_duplicated = remove_duplicated(file_to_csv_wo_nas)
            save_file(file_to_csv_wo_duplicated,files)
        if int(files[0:4]) in range(2018,2022):
            file_to_csv = pd.read_excel(file_name,usecols = "A:Y")
            file_to_csv_wo_format = file_to_csv.copy()
            file_to_csv_with_header = format_headers(file_to_csv_wo_format)
            file_to_csv_with_dates = format_dates(file_to_csv_with_header)
            file_to_csv_wo_nas = remove_nas(file_to_csv_with_dates)
            file_to_csv_wo_duplicated = remove_duplicated(file_to_csv_wo_nas)
            save_file(file_to_csv_wo_duplicated,files)

def get_files_to_export():     
    files_to_export = os.listdir('data_lake/landing')
    files_to_export = files_to_export[0:27]
    return files_to_export
        
def get_file_name(path,name_file):
    file_name = path + name_file
    return file_name

def format_headers(df_wo_headers):   
    column_names = list(df_wo_headers.columns)
    column_names = list((x.zfill(2) for x in column_names))
    column_names = list(map(lambda x: 'H'+str(x) if len(x)==2 else x,column_names))
    df_wo_headers.columns = column_names
    return df_wo_headers
    
def format_dates(file_to_csv_w_dates):
    file_to_csv_w_dates['Fecha'] = file_to_csv_w_dates['Fecha'].apply(
        lambda x: datetime.strptime(x,"%Y-%m-%d") if type(x) == str else x)
    return file_to_csv_w_dates
    
def remove_nas(data_w_na):
    data_wo_na = data_w_na.dropna()
    return data_wo_na
    
def remove_duplicated(data_w_duplicated):
    data_wo_duplicated = data_w_duplicated.drop_duplicates()
    return data_wo_duplicated

def save_file(df_to_save,files):
    df_to_save.to_csv('data_lake/raw/{}.csv'.format(files[0:4]),index=False,encoding='utf-8')

def test_remove_duplicated():
    prueba = [['a', 'a'],
              ['a', 'a'],
              ['b', 5]]
    resultado = ['a','b']
    df_prueba = pd.DataFrame(prueba)
    df_prueba = remove_duplicated(df_prueba)
    assert list(df_prueba[0]) == resultado

if __name__ == "__main__":
    doctest.testmod()
    transform_data()
