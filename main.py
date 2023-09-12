import random
class Personaje:
    def __init__(self, avatar, salud, fuerza, agilidad, inteligencia, nombre) :
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

    def enfrentar(self, oponente, mundo):
        print(f"¡{self.nombre} se enfrenta a {oponente.nombre}!")
        # Simular ataque del personaje1 al personaje2
        danio = self.daño_inflingido()
        print(f"{self.nombre} ataca a {oponente.nombre} y le inflige {danio} de daño.")
        oponente.daño_recibido(danio)

        # Simular ataque del personaje2 al personaje1
        danio = oponente.daño_inflingido()
        print(f"{oponente.nombre} ataca a {self.nombre} y le inflige {danio} de daño.")
        self.daño_recibido(danio)

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
        #personaje.mostrar_habilidades()

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


def elegir_avatar():
    avatares = ["Guerrero", "Mago", "Arquero", "Info de los avatares:"]
    print("Elige el avatar de tu personaje:")

    for i, a in enumerate(avatares):
        print(f"{i + 1}. {a}", end="   ")

    avatar = int(input("\n> "))

    if avatar == 4:
        print("""Guerrero -> HP: 200    Fuerza: 10      Agilidad: 5      Inteligencia: 4\n
Mago -> HP: 100    Fuerza: 4      Agilidad: 6      Inteligencia: 12\n
Guerrero -> HP: 150    Fuerza: 6      Agilidad: 10    Inteligencia: 6\n""")
        print("Elige el avatar de tu personaje:")
        avatar = int(input("> "))
    return avatares[avatar - 1]

def elegir_habilidad():
    habilidades = ["Fuerza", "Magia", "Precisión"]

    print("Elige la habilidad de tu personaje:")

    for i, h in enumerate(habilidades):
        print(f"{i + 1}. {h}")

    habilidad = int(input("> "))
    return habilidades[habilidad - 1]


def crear_personaje(nombre, avatar, habilidades):
    if avatar == "Guerrero":
        personaje = Guerreros(nombre, avatar)

    elif avatar == "Mago":
        personaje = Magos(nombre, avatar)

    elif avatar == "Arquero":
        personaje = Arqueros(nombre, avatar)

    return personaje


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




def main():
    print("Bienvenido al ring de Batalla!")
    mundo = MundoDelJuego()
    num_personajes = int(input("Ingrese el numero de jugadores: "))

    for i in range(num_personajes):
        nombre = input(f"Jugador {i+1} ingresa tu nombre: ")
        avatar = elegir_avatar()
        habilidad = elegir_habilidad()

        personaje = crear_personaje(nombre, avatar, habilidad)

        #personaje1 = crear_personaje(nombre, avatar, habilidad)
        #personaje2 = crear_personaje()

        mundo.agregar_personajes(personaje)
        #mundo.agregar_personaje(personaje2)
    mundo.saber_personajes()



    # Creación de Objetos y agregado al mundo
    #guerrero1 = Guerreros("Guerrero1", "Espada afilada")
    #arquero1 = Arqueros("Arquero1", "Arco elegante")
    #mago1 = Magos("Mago1", "Varita mágica")

    #mundo.agregar_personajes()
    #mundo.agregar_personajes()
    #mundo.agregar_personajes()

    #mundo.saber_personajes()

    # Elegir dos personajes para el desafío
    #personaje1 = guerrero1  # Puedes cambiar esto para elegir otro personaje
    #personaje2 = arquero1  # Puedes cambiar esto para elegir otro personaje

    # Simular un desafío entre personaje1 y personaje2
    #mundo.enfrentamientos(personaje1, personaje2)

    # Mostrar estado de los personajes después del desafío
    #mundo.mostrar_estado_personajes()



    #guerrero1.mostrar_atributos()
    #arquero1.mostrar_atributos()
    #mago1.mostrar_atributos()

if __name__ == "__main__":
    main()
