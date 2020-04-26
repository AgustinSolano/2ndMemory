import time

class Memoria:
    def __init__(self, nombre = " ", link= " ", fecha = " ", tags = []):
        self.nombre = nombre
        self.link = link
        self.fecha = fecha
        self.tags = tags
        self.posible_tags = ("articulo", "software", "twitter", "persona", "laboratorio", "paper")

    def set_memory(self, nombre, link, fecha, tags):
        self.nombre = nombre
        self.link = link
        self.fecha = fecha
        self.tags = tags
        return True

    def get_memoria(self):
        return [self.nombre, self.link, self.fecha, self.tags]

    def print_memoria(self):
        print("Nombre: {}\nLink: {}\nFecha: {}\nTags: {}".
              format(self.nombre, self.link, time.strftime('%Y-%m-%d', self.fecha), self.tags))
        return True

    def check_tags:
        






nombre = "articulo interesante sobre suenio"
link = "www.articulo.com"
fecha = time.localtime()
tags = ["articulo", "ciencia"]
##
mem1 = Memoria(nombre, link, fecha, tags)
mem1.print_memoria()
'''print(nombre)
print(link)
print(time.strftime('%Y-%m-%d', fecha))
print(tags)'''