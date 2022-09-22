from ..extensions import db

class Series(db.Model):
    __tablename__ = "filmes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    tipo = db.Column(db.String(50))
    temporada = db.Column(db.String(50))
    episodio = db.Column(db.String(50))
    dataTermino = db.Column(db.Date)
    

    def __repr__(self):
        return "<Series(nome={}, tipo={}, temporada={}, episodio{}, dataTermino={})>".format(self.nome, self.tipo, self.temporada, self.episodio, self.dataTermino)