#Faznedo cunsultas sobre o tipo dos veiculos  dos involvidos
from flask_restful import Resource, marshal_with, abort
from database.PgConector import *

class Testa(Resource):

    # GET Acidentes
    def get(self):

    #Consulta SQL
        sql = 'select tipo_veiculo, count(tipo_veiculo) from public."MyData" group by tipo_veiculo'

        cur.execute(sql)
        acidentePesquisa = cur.fetchall()
        #acidentePesquisa = cur.fetchall()[0]


        return acidentePesquisa
