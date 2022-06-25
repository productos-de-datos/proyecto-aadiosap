"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


from numpy import arange


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    from urllib import request
    
    years_to_download = arange(1995,2022,1)
    begining_url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
    end_url = '.xlsx?raw=True'
    path_to_save_rawdata = 'data_lake/landing/'

    for years in years_to_download:
        remote_url = str(begining_url) + str(years) + str(end_url)
        local_file = str(path_to_save_rawdata) + str(years) + str(end_url[0:4])
        request.urlretrieve(remote_url, local_file)


    # Definimos la URL del archivo a descargar

    remote_url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/1995.xlsx?raw=True'

    # Definimos el nombre del archivo local a guardar

    local_file = 'data_lake/landing/1995.xlsx' 

    # Se realiza la descarga y se guarda el archivo de manera local

    request.urlretrieve(remote_url, local_file)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


ingest_data()