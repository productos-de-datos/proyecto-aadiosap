"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    from urllib import request
    from numpy import arange
    
    def get_raw_data(years_to_download,url,path_to_save_rawdata):
        for years in years_to_download:
            if years in range(2016,2018):
                extension = '.xls?raw=true'
            else:
                extension = '.xlsx?raw=true'      
            url_to_download = str(url) + str(years) + str(extension)
            path_to_save = str(path_to_save_rawdata) + str(years) + str(extension[0:4])
            request.urlretrieve(url_to_download, path_to_save)
    
    get_raw_data(years_to_download,url,path_to_save_rawdata)
    
if __name__ == "__main__":
    import doctest

    years_to_download = arange(1995,2022,1)
    url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
    path_to_save_rawdata = 'data_lake/landing/'

    doctest.testmod()
    ingest_data()
