"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
"""Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

"""
import doctest
import numpy as np
import urllib.request

def ingest_data():
    years_to_download = np.arange(1995,2022,1)
    url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
    path_to_save_rawdata = 'data_lake/landing/'
    for years in years_to_download:
        if years in range(2016,2018):
            extension = '.xls'
            url_to_download = str(url) + str(years) + str(extension)
            path_to_save = str(path_to_save_rawdata) + str(years) + str(extension[0:4])
            urllib.request.urlretrieve(url_to_download, path_to_save)
        else:
            extension = '.xlsx'      
            url_to_download = str(url) + str(years) + str(extension)
            path_to_save = str(path_to_save_rawdata) + str(years) + str(extension[0:5])
            urllib.request.urlretrieve(url_to_download, path_to_save)
    
if __name__ == "__main__":
    doctest.testmod()
    ingest_data()
    
