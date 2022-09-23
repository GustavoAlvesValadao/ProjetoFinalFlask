# importando o Blueprint e adicionando render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.filmes import Filmes
from datetime import date, datetime

# Instanciar o blueprint
filmesBp = Blueprint('filmesBp', __name__)

@filmesBp.route('/')
def filmes_home():
    return render_template("filmes_home.html")

@filmesBp.route('/catalogo')
def filmes_list():

    #nova adição
    db.create_all()
# adiciona o acesso a banco e a chamada ao render_template
    filmes_query = Filmes.query.all()
    return render_template('filmes_list.html', filmes=filmes_query)

@filmesBp.route('/catalogo/create')
def create_filmes():
    return render_template('filmes_create.html')

@filmesBp.route('/catalogo/add', methods=["POST"])
def add_filmes():

    sTitulo = request.form["titulo"]
    sTipo = request.form["tipo"]
    sTemporada = request.form["temporada"]
    sEpisodio = request.form["episodio"]
    dData = datetime.strptime(request.form["data"], '%Y-%m-%d')

    filme = Filmes(titulo=sTitulo, tipo=sTipo, temporada=sTemporada, episodio=sEpisodio, data=dData)
    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filmesBp.filmes_list"))

#chamar o formulário de alteração
@filmesBp.route('/catalogo/update/<filmes_id>')
def update_filmes(filme_id=0):
    filme_query = Filmes.query.filter_by(id = filme_id).first()
    return render_template('filmes_update.html', filme=filme_query)

@filmesBp.route('/catalogo/upd', methods=["POST"])
def upd_filmes():

    idFilmes = request.form["id"]
    sTitulo = request.form["titulo"]
    sTipo = request.form["tipo"]
    sTemporada = request.form["temporada"]
    sEpisodio = request.form["episodio"]
    dData = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    filme = Filmes.query.filter_by(id = idFilmes).first()
    filme.titulo = sTitulo
    filme.tipo = sTipo
    filme.temporada = sTemporada
    filme.episodio = sEpisodio
    filme.data = dData
    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filmesBp.filmes_list"))

@filmesBp.route('/catalogo/delete/<filme_id>')
def delete_filmes(filme_id=0):
    filme_query = Filmes.query.filter_by(id = filme_id).first()
    return render_template('filmes_delete.html', filme=filme_query)

#rota para apagar de fato
@filmesBp.route('/catalogo/dlt', methods=["POST"])
def dlt_filmes():

    idFilmes = request.form["id"]
    filme = Filmes.query.filter_by(id = idFilmes).first()
    db.session.delete(filme)
    db.session.commit()

    return redirect(url_for("filmesBp.filmes_list"))