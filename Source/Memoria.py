import time

class Memoria:
    def __init__(self):
        self.nombre = " "
        self.link = " "
        self.fecha = " "
        self.tags = []
        self.datos_ok = False
        self.posible_tags = ("articulo", "software", "twitter", "persona", "laboratorio", "paper")


    def set_memory(self, nombre, link, fecha, tags):

        #primero chequeo que el tag este bien
        if self.check_tags(tags):
            self.nombre = nombre
            self.link = link
            self.fecha = fecha
            self.tags = tags
            self.datos_ok = True
            output = True
        else:
            print("Alguno de los tags no esta permitido!")
            output = False
        return output

    def get_memoria(self):
        return [self.nombre, self.link, self.fecha, self.tags]

    def print_memoria(self):
        if self.datos_ok:
            print("Nombre: {}\nLink: {}\nFecha: {}\nTags: {}".
                  format(self.nombre, self.link, time.strftime('%Y-%m-%d', self.fecha), self.tags))
            output = True
        else:
            print("El objeto no contiene datos correctos")
            output = False
        return output

    def check_tags(self, tags):
        #Chequeo si todos los tags pertenece a posible_tags
        check = [self.posible_tags.__contains__(elem) for elem in tags]
        output = all(check) #check if all elements are true
        return output
        



'''nombre = "articulo interesante sobre suenio"
link = "www.articulo.com"
fecha = time.localtime()
tags = ["articulo", "twitter"]
##
mem1 = Memoria()
mem1.set_memory(nombre, link, fecha, tags)
mem1.print_memoria()

print(mem1.check_tags(["ciencia", "articulo"]))
print(mem1.check_tags(["articulo", "twitter"]))'''
'''print(nombre)
print(link)
print(time.strftime('%Y-%m-%d', fecha))
print(tags)'''