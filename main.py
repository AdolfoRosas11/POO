import datetime
from random import randint

class Usuarios:
    def __init__(self, cuenta, nombre):
        self.nombre = nombre
        self.cuenta = cuenta

    def mostrarMensaje(self):
        print(f"Nombre: { self.nombre}, tipo de usuario: {self.cuenta}")


class Pacientes(Usuarios):
    def __init__(self,nombre, cuenta, edad, enfermedad):
        super().__init__(cuenta, nombre)
        #se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.
        self.enfermedades = enfermedad
        self.edad = edad

    def enfermedades(self):
        enfermedades = ["tos", "fiebre", "estornudos", "vista borrosa", ]
        self.enfermedades = enfermedades

    def mostrarMensaje(self):
        super().mostrar_Mensaje()
        print(f"Enfermedades: {self.enfermedades}")


class Medicos(Usuarios):
    def __init__(self, nombre, cuenta, especialidad):
        super().__init__(nombre, cuenta)  # se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.
        self.especialidad = especialidad

    def mostrarMensaje(self):
        super().mostrar_Mensaje()
        print(f"Especialidad del doctor: {self.especialidad}")



class citas:
    def __init__(self, paciente, mes, dia,año,hora,medico):
        # super().__init__(paciente,medico)
        # se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.con el comando super() .
        self.paciente = paciente
        self.mes = mes
        self.dia = dia
        self.año = año
        self.hora = hora
        self.medico = medico

    def mostrarMensaje(self):
        print(f"La fecha de la cita del paciente:{self.paciente} con el medico {self.medico} es el  {self.dia}{self.mes}{self.año} a las {self.hora} \n ")


class Tratamiento:
    def __init__(self, paciente, prescripcion, duracion, medico):
        self.paciente = paciente
        self.prescripcion = prescripcion
        self.duracion = duracion
        self.medico = medico

    def mostrarMensaje(self):
        print(f"El tratamiento dado por el medico:{self.medico} para el paciente:{self.paciente} es de {self.prescripcion} cada  {self.duracion}  \n")


def main():
    Citas = []

    while True:
        opt = input("Bienvenide al hospital\nSelecciona una opción:\n1. Agendar cita\n2. Verificar citas\n3. Salir\n")

        if opt == "1":
            nombre = input("Ingrese su nombre: ")
            edad = input("Ingrese su edad: ")
            #enfermedad = input("")

            # Se crean los objetos
            paciente1 = Pacientes(nombre, randint(10 ** 10, 10 ** 11 - 1), edad, ["Gripe", "Fiebre"])
            medico1 = Medicos("Maria Lopez", randint(10 ** 10, 10 ** 11 - 1), "General")

            cita1 = citas(paciente1.nombre, "03", "10", "2023", "10:00", medico1.nombre)
            tratamiento1 = Tratamiento(paciente1, medico1, "Antibióticos", 5)

            tratamiento1.mostrarMensaje()
            cita1.mostrarMensaje()

        elif opt == "2":
            if citas:
                print("Citas agendadas:")
                for i, cita in enumerate(citas, 1):
                    print(f"{i}. {cita}")
            else:
                print("No hay citas agendadas.")

        elif opt == "3":
            break

        else:
            print("Opcion no valida, intente de nuevo")


if __name__ == "__main__":
    main()