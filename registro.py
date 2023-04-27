import random

descripciones = ('Cania', 'Anzuelo', 'Indumentaria', 'Caza', 'Pesca', 'Bote', 'Gorros')


class Articulo:
    def __init__(self, identificacion, desc, precio, origen, tipo):
        self.identificacion = identificacion
        self.descripcion = desc
        self.precio = precio
        self.origen = origen
        self.tipo = tipo


def to_string(reg):
    return f'Id: {reg.identificacion:<3} | Descripcion: {reg.descripcion:<13} | Precio: {reg.precio:<7} ' \
           f'| Origen: {reg.origen:<3} | Tipo: {reg.tipo}'


def generar_articulo():
    ide = random.randint(1, 99)
    desc = random.choice(descripciones)
    pre = round(random.uniform(1, 500), 2)
    origen = random.randint(0, 24)
    tipo = random.randint(0, 29)
    return Articulo(ide, desc, pre, origen, tipo)


