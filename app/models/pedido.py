from app import db


class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)

    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

    usuario = db.relationship("Usuario", backref="pedidos")
    producto = db.relationship("Producto", backref="pedidos")