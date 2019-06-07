#Faznedo cunsultas sobre a metereologia das causas dos acidentes involvidos
from flask_restful import Resource, marshal_with, abort
from database.PgConector import *

class Metereologia(Resource):

    # GET Acidentes
    def get(self):

    #Consulta SQL
        sql = 'select condicao_metereologica, count(causa_acidente) from "MyData" group by condicao_metereologica'

        cur.execute(sql)
        acidentePesquisa = cur.fetchall()
        #acidentePesquisa = cur.fetchall()[0]


        return acidentePesquisa