from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restful import Api

from resources.BR_Resource import BR_Acidente
from resources.CausaAcidente_Resource import CausaAcidente
from resources.DiaSemana_Resource import DiaSemana
from resources.Estado_fisico_Resource import Estado_fisico_Resource
from resources.SexoEst_Resource import SexoEst
from resources.Sexo_Resource import Sexo
from resources.TipoAcidente_Resource import TipoAcidente
from resources.Top_Resource import Top_Acidente
from resources.UF_Resource import UF_Acidente
from resources.Teste_Resource import Testa
from resources.MortosUF_Resource import Mortos
from resources.AcidentesMetereologia_Resource import Metereologia
from resources.Fase_Resource import FaseDia_Resource
#Criar o servidor
app = Flask(__name__)

app.config['DEBUG'] = True

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')


#links para concexao com a pagina WEB
#Resources
api.add_resource(UF_Acidente, '/UF')
api.add_resource(BR_Acidente, '/BR/<string:estado>')
api.add_resource(DiaSemana, '/dia')
api.add_resource(Sexo, '/Sexo')
api.add_resource(CausaAcidente, '/CausaAcidente')
api.add_resource(TipoAcidente, '/TipoAcidente')
api.add_resource(SexoEst, '/SexoEst/<string:estado>')
api.add_resource(Top_Acidente, '/Top/<string:estado>')
api.add_resource(Estado_fisico_Resource, '/fisico/<string:estado>')
api.add_resource(Testa, '/Testa')
api.add_resource(Mortos, '/Mortos')
api.add_resource(Metereologia, '/Metereologia')
api.add_resource(FaseDia_Resource, '/FaseDia_Resource')



app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run()
#app.run(host='0.0.0.0')


