#Fazendo consultas do numero de acidentes por tipo de veículo
from flask_restful import Resource, marshal_with, abort
from database.PgConector import *

class Tipo_Veiculo(Resource):

    # GET Acidentes
    def get(self):

        sql = 'select tipo_veiculo, count(tipo_veiculo) from public."MyData" group by tipo_veiculo'

        #Consulta SQL
        cur.execute(sql)
        acidentePesquisa = cur.fetchall()
        #acidentePesquisa = cur.fetchall()[0]


        return acidentePesquisa
