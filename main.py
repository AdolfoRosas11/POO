import random
class Personaje:
    def __init__(self,avatar,salud,fuerza,agilidad,inteligencia,nombre) :
        # Se declaran los atributos de cada personaje
        self.avatar=avatar
        self.salud=salud
        self.fuerza=fuerza
        self.agilidad=agilidad
        self.inteligencia=inteligencia
        self.nombre= nombre
    def mostrar_atributos(self):
        #Se imprimen los valores de los atributos
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.salud}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Inteligencia : {self.inteligencia}")
        print(f"Avatar : {self.avatar}")

    def mostrar_eleccion(self):
        #Se crea una función para imprimir la la habilidad selecionada
        self.habilidad.eleccion()

    def enfretar(self,oponente,mundo):
        print(f"¡{self.nombre} se enfrenta a {oponente.nombre}!")
        # Simular ataque del personaje1 al personaje2
        danio = self.daño_inflingido()
        print(f"{self.nombre} ataca a {oponente.nombre} y le inflige {danio} de daño.")
        oponente.daño_recivido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = oponente.daño_inflingido()
        print(f"{oponente.nombre} ataca a {self.nombre} y le inflige {danio} de daño.")
        self.daño_recivido(danio)

        # Mostrar el estado después del enfrentamiento
        print(f"Estado después del enfrentamiento:")
        mundo.mostrar_estado_personajes()

    def desafiar(self, oponente):
        print(f"{self.nombre} desafía a {oponente.nombre} a un enfrentamiento:")
        self.enfrentar(oponente)

    # Se crea un función para saber el valor de daño inflijido
    def daño_inflingido(self):
        if self.fuerza > 15:
            return self.fuerza * 1.5
        else:
            return self.fuerza

    # Se crea un función para saber el valor de daño recivido
    def daño_recivido(self,daño):
        self.salud -= daño

        if self.salud < 0:
            self.salud = 0
            print(f"{self.nombre} ha sido derrotado!")

    def mostrar_datos(self , personaje): # esa función espera recibir un objeto
        print(f"Nombre: {personaje.nombre}")
        print(f"Avatar : {personaje .avatar}")

        personaje.mostrar_atributos()
        personaje.mostrar_habilidades()

class Habilidad:
    def __init__(self,nombre):
        self.nombre=nombre
    def eleccion(self):
        print(f"Habilidad escogida: {self.nombre}")

# Se crean las clases se los distintos tipos de Personajes
class Guerreros(Personaje):
    def __init__(self,nombre,avatar ):
        #self.nombre= nombre
        super().__init__(avatar,100,15,3,2,nombre) #parameteros del 20-0 para aisganar valores de los atributos
        self.habilidad =Habilidad("Golpe Mortal")
    def mostrar_eleccion(self):
        self.habilidad.eleccion()

    def mostrar_habilidad(self):
            print(self.habilidad.nombre)

    def enfrentar(self, oponente):
        print(f"¡{self.nombre} se enfrenta a {oponente.nombre}!")

        # Simular ataque del personaje1 al personaje2
        danio = self.daño_inflingido()
        print(f"{self.nombre} ataca a {oponente.nombre} y le inflige {danio} de daño.")
        oponente.daño_recivido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = oponente.daño_inflingido()
        print(f"{oponente.nombre} ataca a {self.nombre} y le inflige {danio} de daño.")
        self.daño_recivido(danio)

        # Mostrar el estado después del enfrentamiento
        print(f"Estado después del enfrentamiento:")
        mundo.mostrar_estado_personajes()

class Arqueros(Personaje):
    def __init__(self, nombre,avatar):
        # self.nombre= nombre
        super().__init__(avatar, 100, 10, 8, 9,nombre)  # parameteros del 20-0 para aisganar valores de los atributos
        self.habilidad=Habilidad("Golpe Mortal")
    def enfrentar(self, oponente):
        print(f"¡{self.nombre} se enfrenta a {oponente.nombre}!")

        # Simular ataque del personaje1 al personaje2
        danio = self.daño_inflingido()
        print(f"{self.nombre} ataca a {oponente.nombre} y le inflige {danio} de daño.")
        oponente.daño_recivido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = oponente.daño_inflingido()
        print(f"{oponente.nombre} ataca a {self.nombre} y le inflige {danio} de daño.")
        self.daño_recivido(danio)

        # Mostrar el estado después del enfrentamiento
        print(f"Estado después del enfrentamiento:")
        mundo.mostrar_estado_personajes()
class Magos(Personaje):
    def __init__(self, nombre,avatar):
        # self.nombre= nombre
        super().__init__(avatar, 100, 8, 9, 18,nombre)  # parameteros del 20-0 para aisganar valores de los atributos
        self.habilidad=Habilidad("Bola de fuego ")

    def enfrentar(self, oponente):
        print(f"¡{self.nombre} se enfrenta a {oponente.nombre}!")

        # Simular ataque del personaje1 al personaje2
        danio = self.daño_inflingido()
        print(f"{self.nombre} ataca a {oponente.nombre} y le inflige {danio} de daño.")
        oponente.daño_recivido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = oponente.daño_inflingido()
        print(f"{oponente.nombre} ataca a {self.nombre} y le inflige {danio} de daño.")
        self.daño_recivido(danio)

        # Mostrar el estado después del enfrentamiento
        print(f"Estado después del enfrentamiento:")
        mundo.mostrar_estado_personajes()


class MundoDelJuego:
    def __init__(self):
        self.personajes=[] # Para almacenar la lista de jugadores dentro del mundo
    # Funcion para tener varios personajes
    def agregar_personajes(self,personaje):
        self.personajes.append(personaje) #se utiliza .appenes para agregar elementos a un arreglo
    #Función para saber que personajes se encuentran en el mundo
    def saber_personajes(self):

        print(f"Los siguientes personajes se encuentran en el mundo")
        for personaje in self.personajes:
            print(f"{personaje.nombre}- Apariencia {personaje.avatar}")

    def enfrentamientos(self, personaje1, personaje2):
        print(f"Enfrentamiento entre {personaje1.nombre} y {personaje2.nombre}:")

        # Simular ataque del personaje1 al personaje2
        danio = personaje1.daño_inflingido()
        print(f"{personaje1.nombre} ataca a {personaje2.nombre} y le inflige {danio} de daño.")
        personaje2.daño_recivido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = personaje2.daño_inflingido()
        print(f"{personaje2.nombre} ataca a {personaje1.nombre} y le inflige {danio} de daño.")
        personaje1.daño_recivido(danio)

        # Mostrar el estado después del enfrentamiento
        print(f"Estado después del enfrentamiento:")
        self.mostrar_estado_personajes()


    def desafio(self):
        if len(self.personajes) < 2:
            print("No hay suficientes personajes para un desafío.")
            return

        # Elegir dos personajes aleatorios para el desafío
        personaje1, personaje2 = random.sample(self.personajes, 2)

        print(f"Desafío entre {personaje1.nombre} y {personaje2.nombre}!")
        self.enfrentamiento(personaje1, personaje2)

    def mostrar_estado_personajes(self):
        for personaje in self.personajes:
            print(f"{personaje.nombre}: Salud={personaje.salud}")

    def desafio(self):
        if len(self.personajes) < 2:
            print("No hay suficientes personajes para un desafío.")
            return

        # Elegir dos personajes aleatorios para el desafío
        personaje1, personaje2 = random.sample(self.personajes, 2)

        print(f"Desafío entre {personaje1.nombre} y {personaje2.nombre}!")
        personaje1.desafiar(personaje2)

    def mostrar_estado_personajes(self):
        print("Estado de los personajes:")
        for personaje in self.personajes:
            print(f"{personaje.nombre}: Salud={personaje.salud}")

# def desafios(self):


def main():
    print("Bienvenido al ring de Batalla!")
    mundo = MundoDelJuego()

    # Creación de Objetos y agregado al mundo
    guerrero1 = Guerreros("Guerrero1", "Espada afilada")
    arquero1 = Arqueros("Arquero1", "Arco elegante")
    mago1 = Magos("Mago1", "Varita mágica")

    mundo.agregar_personajes(guerrero1)
    mundo.agregar_personajes(arquero1)
    mundo.agregar_personajes(mago1)

    mundo.saber_personajes()

    # Elegir dos personajes para el desafío
    personaje1 = guerrero1  # Puedes cambiar esto para elegir otro personaje
    personaje2 = arquero1  # Puedes cambiar esto para elegir otro personaje

    # Simular un desafío entre personaje1 y personaje2
    mundo.enfrentamientos(personaje1, personaje2)

    # Mostrar estado de los personajes después del desafío
    mundo.mostrar_estado_personajes()



    #guerrero1.mostrar_atributos()
    #arquero1.mostrar_atributos()
    #mago1.mostrar_atributos()

if __name__ == "__main__":
    main()
