from ..extensions import db

class Uc(db.Model):
    __tablename__ ="ucs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    tipo = db.Column(db.String(50))
    descricao = db.Column(db.String(150))
    fim = db.Column(db.Date)

    def __repr__(self):
        return "<Uc(titulo={}, tipo={}, descricao{}, fim={})>".format(self.titulo, self.tipo, self.descricao, self.fim)
