# importando o Blueprint e adicionando render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.uc import Uc
from datetime import date, datetime

# Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def uc_home():
    return render_template("uc_home.html")

@ucBp.route('/uc')
def uc_list():

    #nova adição
    db.create_all()
# adiciona o acesso a banco e a chamada ao render_template
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)

@ucBp.route('/uc/create')
def create_uc():
    return render_template('uc_create.html')

@ucBp.route('/uc/add', methods=["POST"])
def add_uc():

    sTitulo = request.form["titulo"]
    sTipo = request.form["tipo"]
    sTemporada = request.form["temporada"]
    sEpisodio = request.form["episodio"]
    dData = datetime.strptime(request.form["data"], '%Y-%m-%d')

    uc = Uc(titulo=sTitulo, tipo=sTipo, temporada=sTemporada, episodio=sEpisodio, data=dData)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))

#chamar o formulário de alteração
@ucBp.route('/uc/update/<uc_id>')
def update_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_update.html', uc=uc_query)

@ucBp.route('/uc/upd', methods=["POST"])
def upd_uc():

    iUc = request.form["id"]
    sTitulo = request.form["titulo"]
    sTipo = request.form["tipo"]
    sTemporada = request.form["temporada"]
    sEpisodio = request.form["episodio"]
    dData = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc.query.filter_by(id = iUc).first()
    uc.nome = sTitulo
    uc.tipo = sTipo
    uc.temporada = sTemporada
    uc.episodio = sEpisodio
    uc.data = dData
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))

@ucBp.route('/uc/delete/<uc_id>')
def delete_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_delete.html', uc=uc_query)

#rota para apagar de fato
@ucBp.route('/uc/dlt', methods=["POST"])
def dlt_uc():

    iUc = request.form["id"]
    uc = Uc.query.filter_by(id = iUc).first()
    db.session.delete(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))