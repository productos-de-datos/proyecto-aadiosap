from datetime import date
from pandas import concat


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import os
    from datetime import datetime
    
    def get_files_to_combine(root_path):
        files_to_combine = os.listdir(root_path)
        files_to_combine = list(map(lambda x:'data_lake/raw/'+str(x),files_to_combine))
        return files_to_combine
    
    def combine_data(root_path):
        data_combine = pd.concat(map(pd.read_csv,get_files_to_combine(root_path)), ignore_index=True)
        data_combine = pd.melt(data_combine,id_vars=['Fecha'])
        data_combine = format_dates(data_combine)
        data_combine = format_columns(data_combine)
        print(data_combine.dtypes)
        data_combine.to_csv('data_lake/cleansed/precios-horarios.csv',index=False)

    def format_dates(data_wo_dates):
        data_wo_dates['Fecha'] = data_wo_dates['Fecha'].apply(
            lambda x: datetime.strptime(x,"%Y-%m-%d") if type(x) == str else x)
        data_w_dates = data_wo_dates
        return data_w_dates

    def format_columns(data_combine):
        colum_requested = ['fecha','hora','precio']
        data_combine.columns = colum_requested
        return data_combine

    if __name__ == "__main__":
        root_path = 'data_lake/raw'
        combine_data(root_path)


#    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    clean_data()

