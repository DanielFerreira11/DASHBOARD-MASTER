#Faznedo cunsultas sobre morte dos involvidos
from flask_restful import Resource, marshal_with, abort
from database.PgConector import *

class Mortos(Resource):

    # GET Acidentes
    def get(self):

    #Consulta SQL
        sql = 'select uf, count(mortos)  from "MyData" group by uf;'

        cur.execute(sql)
        acidentePesquisa = cur.fetchall()
        #acidentePesquisa = cur.fetchall()[0]


        return acidentePesquisa