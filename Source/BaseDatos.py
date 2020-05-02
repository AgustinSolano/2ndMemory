import time

class BaseDatos:
    def __init__(self):
        self.file_path = " "
        self.tag_dict, self.mem_dict = self.leer_file(self.file_path)

    def leer_file(self, file_path):
        """ Leo el file con todos los datos para crear un diccionario
         con tags y numero de registro/memoria (tag_dict), y crear tambien otro
         diccionario con todos los registros (mem_dict)"""
        tag_dict = {"articulo": [0, 2, 4],
                    "software": [1, 3, 4]}

        mem_dict = {0: {"nombre": "papanata", "link": " ", "fecha": time.localtime(), "tags": ["articulo"]},
                    1: {"nombre": "agus", "link": " ", "fecha": time.localtime(), "tags": ["software"]},
                    2: {"nombre": "adolf", "link": " ", "fecha": time.localtime(), "tags": ["articulo"]},
                    3: {"nombre": "pipi", "link": " ", "fecha": time.localtime(), "tags": ["software"]},
                    4: {"nombre": "agus", "link": " ", "fecha": time.localtime(), "tags": ["articulo", "software"]}}

        return tag_dict, mem_dict

    def buscar(self,tags):
        """Esta funcion va a recibir una lista de tags y tiene que buscar
        cuales son los registros/memorias que estan asociados a ese tag"""

        #Primero busco los numero de registro/memoria asociados a TODOS los tags
        found = []
        for elem in tags:
            num_list = self.tag_dict.get(elem) #busco tag en tag_dict
            found.append(num_list) #lista con los indices
        print(found)
        if found.__contains__(None): #si contiene al menos un None no hay registro que pertenezca a todos los tags
            print("No cumple con todos los requisitos")
        else:
            res = list(set.intersection(*map(set, found))) #esto me permite buscar elementos comunes estre las listas
            print(res)

            #Luego busco los registros para esos tags
            if len(res) != 0:
                for num in  res:
                    print(self.mem_dict[num])


"""    def guardar(self, memoria):

    def borrar(self):

    def do_buckup(self):"""

bd = BaseDatos()
bd.buscar(["articulo"])
bd.buscar(["articulo", "twitter"])
#
bd.buscar(["articulo", "software"])