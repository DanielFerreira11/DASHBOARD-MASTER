import psycopg2
#from model.Acidente import Acidente

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='123456')
cur = con.cursor()
print('Conexão OK')