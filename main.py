import random
from datetime import datetime
from random import randint

class Usuarios:
    def __init__(self, cuenta, nombre):
        self.nombre = nombre
        self.cuenta = cuenta

    def mostrarMensaje(self):
        print(f"Nombre: { self.nombre}, tipo de usuario: {self.cuenta}")


class Pacientes(Usuarios):
    def __init__(self, nombre, cuenta, edad, enfermedades):
        super().__init__(cuenta, nombre)
        #se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.
        self.enfermedades = enfermedades
        self.edad = edad
        self.tratamientos = []

    def mostrarMensaje(self):
        super().mostrarMensaje()
        print(f"Enfermedades: {self.enfermedades}")


class Medicos(Usuarios):
    def __init__(self, nombre, cuenta,  especialidad):
        super().__init__(cuenta, nombre)  # se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.
        self.especialidad = especialidad

    def mostrarMensaje(self):
        super().mostrarMensaje()
        print(f"Especialidad del doctor: {self.especialidad}")



class Citas:
    def __init__(self, paciente, fecha,hora,medico):
        # super().__init__(paciente,medico)
        # se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.con el comando super() .
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.medico = medico

    def mostrarMensaje(self):
        print(f"La fecha de la cita del paciente:{self.paciente} con el medico {self.medico} es el  {self.dia}{self.mes}{self.año} a las {self.hora} \n ")

    @staticmethod
    def validar_fecha(fecha):
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False


class Tratamiento:
    tratamientos_sintomas = {
        "Tos": ("Antibióticos", "8hrs"),
        "Fiebre": ("Antibióticos", "8hrs"),
        "Gripe": ("Antibióticos", "8hrs"),
        "Hipertension": ("Dieta", "al menos 1 mes"),
        "Diabetes": ("Dieta", "al menos 1 mes"),
        "Obesidad": ("Dieta", "al menos 1 mes"),
        "Arritmia": ("Medicamento especializado", "según indicación médica"),
        "Insuficiencia cardiaca": ("Medicamento especializado", "según indicación médica"),
        "Tiroides": ("Medicamento especializado", "según indicación médica")
    }

    def __init__(self, paciente, prescripcion, duracion, medico):
        self.paciente = paciente
        self.prescripcion = prescripcion
        self.duracion = duracion
        self.medico = medico

    def mostrarMensaje(self):
        print(f"El tratamiento dado por {self.medico.nombre} para el paciente {self.paciente.nombre} es de {self.prescripcion} cada  {self.duracion} \n")


def main():
    citas_agendadas = []
    pacientes = {}

    especialidades_medicas = {
        "Cardiologia": ["Hipertension", "Arritmia", "Insuficiencia cardiaca"],
        "Interna": ["Tos", "Gripe", "Fiebre"],
        "Endocrinologia": ["Diabetes", "Tiroides", "Obesidad"],
    }

    # Se crean los objetos Medicos
    medico1 = Medicos("Maria Lopez", 123456, "Interna")
    medico2 = Medicos("Juan Perez", 789321, "Cardiología")
    medico3 = Medicos("Miriam Jimenez", 456987, "Endocrinología")
    #medico4 = Medicos("Javier Hernandez", 432764, "Neumología")
    medico4 = Medicos("Ximena Diaz", 890203, "Pediatría")

    medicos = { "MD1": medico1, "MD2": medico2, "MD3": medico3, "MD4": medico4}

    print("Bienvenidx!")

    while True:
        opt = input("\nSelecciona una opción:\n1. Consultas\n2. Agendar cita\n3. Medico\n4. Tratamientos\n5. Salir\n")

        if opt == "1":
            # Se ingresan los datos del paciente
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            sintomas = input("Sintomas separadas por comas (ejemplo: Gripe, Fiebre): ").split(", ")
            id_paciente = input("Número de Seguridad Social: ")

            # Verificar si el ID ya existe en el diccionario de pacientes
            if id_paciente in pacientes:
                print("El ID de paciente ya existe. Intente nuevamente.")
                continue

             # Inicializar una lista de especialidades encontradas
            especialidades_encontradas = []

            # Verificar si alguno de los síntomas coincide con alguna especialidad médica
            for especialidad, lista_sintomas in especialidades_medicas.items():
                for sintoma in sintomas:
                    if sintoma in lista_sintomas and especialidad not in especialidades_encontradas:
                        especialidades_encontradas.append(especialidad)

            # Se crean los objetos Pacientes
            paciente = Pacientes(nombre, id_paciente, edad, sintomas)
            '''
            if edad <= 12:
                tratamiento = Tratamiento(paciente, "Antibioticos infantiles", "8hrs", medico4)
                paciente.tratamientos.append(tratamiento)
                tratamiento.mostrarMensaje()
            else:
                continue
            '''
            if especialidades_encontradas == ['Interna']:
                tratamiento1 = Tratamiento(paciente, "Antibióticos", "8hrs", medico1)
                paciente.tratamientos.append(tratamiento1)
                tratamiento1.mostrarMensaje()

            elif especialidades_encontradas == ['Cardiologia']:
                tratamiento = Tratamiento(paciente, "Dieta y vida saludable", "al menos 1 mes", medico2)
                paciente.tratamientos.append(tratamiento)
                tratamiento.mostrarMensaje()

            elif especialidades_encontradas == ['Endocrinologia']:
                tratamiento = Tratamiento(paciente, "Dieta", "al menos 1 mes", medico3)
                paciente.tratamientos.append(tratamiento)
                tratamiento.mostrarMensaje()

            else:
                print("No tenemos la especialidad para curar su enfermedad")

            pacientes[id_paciente] = {
                "nombre": nombre,
                "edad": edad,
                "sintomas": sintomas,
                "tratamiento": tratamiento1
            }

        elif opt == "2":
            # Se genera la cita
            cita = Citas(paciente.nombre, "03", "10", "2023", "10:00", medico1.nombre)

            citas_agendadas.append(cita)

            cita.mostrarMensaje()

        elif opt == "3":
            if citas_agendadas:
                print("Citas agendadas:")
                for i, cita in enumerate(citas_agendadas, 1):
                    print(f"{i}. {cita}")
                    print("Tratamientos:")
                    for t in paciente.tratamientos:
                        t.mostrar_info()
            else:
                print("No hay citas agendadas.")

        elif opt == "4":
            # Mostrar lista de pacientes y obtener tratamiento
            print("\nLista de pacientes:")
            for id_paciente, datos_paciente in pacientes.items():
                print(f"NSS: {id_paciente}, Nombre: {datos_paciente['nombre']}")

            id_elegido = input(
                "\nIngrese el NSS del paciente para obtener el tratamiento (o '0' para volver al menú principal): ")

            if id_elegido == "0":
                continue  # Volver al menú principal

            if id_elegido in pacientes:
                Tratamiento.mostrarMensaje()

            else:
                print("ID de paciente no válido. Intente nuevamente.")

        elif opt == "5":
            break

        else:
            print("Opcion no valida, intente de nuevo\n")


if __name__ == "__main__":
    main()