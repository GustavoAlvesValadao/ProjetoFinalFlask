
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.uc import Uc
from datetime import date, datetime


ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def uc_home():
    return render_template("index.html")

@ucBp.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")

@ucBp.route('/sobre')
def sobre():
    return render_template("sobre.html")

@ucBp.route('/catalogo')
def uc_list():

    db.create_all()

    filmes2_query = Uc.query.all()
    return render_template('uc_list.html', filmes2=filmes2_query)

@ucBp.route('/catalogo/create')
def create_uc():
    return render_template('uc_create.html')

@ucBp.route('/catalogo/add', methods=["POST"])
def add_uc():

    sNome = request.form["titulo"]
    sTipo = request.form["tipo"]
    dDescricao = request.form["descricao"]
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc(titulo=sNome, tipo=sTipo, descricao=dDescricao, fim=dFim)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))


@ucBp.route('/catalogo/update/<uc_id>')
def update_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_update.html', uc=uc_query)

@ucBp.route('/catalogo/upd', methods=["POST"])
def upd_uc():

    iUc = request.form["id"]
    sNome = request.form["titulo"]
    sTipo = request.form["tipo"]
    dDescricao = request.form["descricao"]
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc.query.filter_by(id = iUc).first()
    uc.nome = sNome
    uc.tipo = sTipo
    uc.descricao = dDescricao
    uc.fim = dFim
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))

@ucBp.route('/catalogo/delete/<uc_id>')
def delete_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_delete.html', uc=uc_query)


@ucBp.route('/catalogo/dlt', methods=["POST"])
def dlt_uc():

    iUc = request.form["id"]
    uc = Uc.query.filter_by(id = iUc).first()
    db.session.delete(uc)
    db.session.commit()

    return redirect(url_for("ucBp.uc_list"))