# adiciona o , render_template
from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Series

#Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/eventos')
def serie_list():
#    return "Teste"
    #adiciona isso
    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    filmes_query = Series.query.all()
    return render_template('serie_list.html', filmes=filmes_query)