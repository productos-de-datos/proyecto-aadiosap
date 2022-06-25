from ntpath import join
from pandas import concat


def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import os

    data_lake_dirs=["landing","raw","cleansed","business"]
    bussines_dirs=["reports","features","forecasts"]
    
    os.makedirs('data_lake', exist_ok=True)

    for dicts in data_lake_dirs:
        new_path="data_lake/"+str(dicts)
        os.makedirs(new_path,exist_ok=True)

    for dicts in bussines_dirs:
        new_path="data_lake/business/"+str(dicts)
        os.makedirs(new_path,exist_ok=True)
    
    os.makedirs('data_lake/business/reports/figures',exist_ok=True)

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

create_data_lake()