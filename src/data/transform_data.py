from sqlite3 import PARSE_COLNAMES
from numpy import arange, dtype


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd
    import os
    from datetime import datetime
  
    def get_files_to_export():     
        files_to_export = os.listdir('data_lake/landing')
        return files_to_export
        
    def get_df_raw(files_to_export,path_to_export):
        for files in files_to_export:
            file_name = get_file_name(path_to_export,files)
            file_to_csv_raw = pd.read_excel(file_name,header=None)
            file_to_csv_w_headers = pd.read_excel(file_name,header=get_header(file_to_csv_raw),usecols="A:Y")
            file_to_csv_with_headers = format_headers(file_to_csv_w_headers)
            file_to_csv = format_dates(file_to_csv_with_headers)
            file_to_csv = remove_nas(file_to_csv)
            file_to_csv = remove_duplicated(file_to_csv)
            save_file(file_to_csv,files)
    
    def get_file_name(path,name_file):
        file_name = path + name_file
        return file_name

    def get_header(file_to_csv_raw):
        header_row = file_to_csv_raw[file_to_csv_raw[0].eq('Fecha')].index.values[0]
        return header_row
    
    def format_headers(file_to_csv_w_headers):   
        column_names = list(file_to_csv_w_headers.columns)
        column_names = list((x.zfill(2) for x in column_names))
        column_names = list(map(lambda x: 'H'+str(x) if len(x)==2 else x,column_names))
        file_to_csv_w_headers.columns = column_names
        file_to_csv_with_header = file_to_csv_w_headers
        return file_to_csv_with_header
    
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

    def save_file(file_to_csv,files):
        file_to_csv.to_csv('data_lake/raw/{}.csv'.format(files[0:4]),index=False)

    if __name__ == "__main__":
        files_to_export = get_files_to_export()
        path_to_export = 'data_lake/landing/'
        get_df_raw(files_to_export,path_to_export)

#    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()




import pandas as pd

#file_to_csv_raw = pd.read_excel('data_lake/landing/1996.xlsx',header=None)
#header_row = file_to_csv_raw[file_to_csv_raw[0].eq('Fecha')].index.values[0]
#file_to_csv = pd.read_excel('data_lake/landing/1996.xlsx',header=header_row,usecols="A:Y")
#column_names = list(file_to_csv.columns)
#column_names = list((x.zfill(2) for x in column_names))
#column_names = list(map(lambda x: 'H'+str(x) if len(x)==2 else x,column_names))
#file_to_csv.columns = column_names
#file_to_csv['Fecha'] = file_to_csv['Fecha'].apply(lambda x: x.strftime("%Y-%m-%d") if type(x) != str else x)
#file_to_csv.to_csv('data_lake/raw/{}.csv'.format(files[0:4]))
#print(file_to_csv.tail(10))
#file_to_csv.to_csv('data_lake/raw/prueba.csv',index=False)