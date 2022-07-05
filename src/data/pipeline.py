"""
Módulo de orquestamiento con luigui.
-------------------------------------------------------------------------------
En este modulo se orquestan los diferentes modulos necesarios para generar 
los precios promedios diarios y mensuales. Definiendo cada prerequisito
de cada modulo y ejecutando una acción si este se ejecuta correctamente
en este caso imprimir MODULO--------------OK

"""



"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget
import os
import pandas as pd
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_monthly_prices import compute_monthly_prices
from compute_daily_prices import compute_daily_prices

class Ingest_Transform_Clean_Data(Task):
    def output(self):
        return LocalTarget("data_lake/cleansed/precios-horarios.csv")

    def run(self):
        ingest_data()
        print("ingest_data-----------------OK")
        transform_data()
        print("transform_data----------OK")
        clean_data()
        print("clean_data-----------OK")

class compute_daily_prices(Task):
    def requires (self):
        return Ingest_Transform_Clean_Data()

    def output(self):
        return LocalTarget('data_lake/business/precios-diarios.csv')

    def run(self):
        compute_daily_prices()
        print("compute_daily_prices------------OK")

class compute_monthly_prices(Task):
    def requires(self):
        return Ingest_Transform_Clean_Data()

    def output(self):
        return LocalTarget('data_lake/business/precios-mensuales.csv')

    def run(self):
        compute_monthly_prices()
        print("compute_monthly_prices-------------------OK")

class Pipe_Run_All(Task):

    def requires(self):
        return [
            compute_daily_prices(),
            compute_monthly_prices(),
        ]

if __name__ == "__main__":
    import doctest
    luigi.run(['Pipe_Run_All','--local-scheduler'])
    doctest.testmod()
