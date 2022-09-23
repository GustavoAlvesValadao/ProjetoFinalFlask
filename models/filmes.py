from ..extensions import db

class Filmes(db.Model):
    __tablename__ ="filmes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    tipo = db.Column(db.String(50))
    temporada = db.Column(db.String(50))
    episodio = db.Column(db.String(50))
    data = db.Column(db.Date)

    def __repr__(self):
        return "<Filmes(titulo={}, tipo={}, temporada{}, episiodio{}, data={})>".format(self.titulo, self.tipo, self.temporada, self.episodio, self.data)
