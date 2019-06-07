#Fazendo cunsultas sobre acidentes metereologicos por estados. 
from flask_restful import Resource, marshal_with, abort
from database.PgConector import *

class FaseDia_Resource(Resource):

    # GET Acidentes
    def get(self):

    #Consulta SQL
        sql = 'select fase_dia, count(fase_dia) from "MyData" group by fase_dia'

        cur.execute(sql)
        acidentePesquisa = cur.fetchall()
        #acidentePesquisa = cur.fetchall()[0]


        return acidentePesquisa
