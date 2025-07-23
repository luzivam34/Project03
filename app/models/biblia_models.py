from app import db

class BibliaModel(db.Model):
    __tablename__ = 'biblia'
    
    id = db.Column(db.Integer, primary_key=True)
    testamento = db.Column(db.String(50), nullable=False)
    livro = db.Column(db.String(50), nullable=False)
    capitulo = db.Column(db.Integer, nullable=False)
    versiculo = db.Column(db.Integer, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Biblia {self.testamento} {self.livro} {self.capitulo}:{self.versiculo}>'