from datetime import datetime

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
    def __init__(self, paciente, fecha_hora, medico):
        # super().__init__(paciente,medico)
        # se está llamando al constructor __init__ de la clase Persona y pasándole los parámetros nombre e id.con el comando super() .
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    @staticmethod
    def validar_fechahora(fecha_hora):
        try:
            datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M")
            return True
        except ValueError:
            return False

    def mostrarMensaje(self):
        fecha_hora_obj = datetime.strptime(self.fecha_hora, "%d/%m/%Y %H:%M")
        print(f"Cita registrada para {self.paciente.nombre} con el médico {self.medico.nombre} el {fecha_hora_obj.strftime('%d/%m/%Y')} a las {fecha_hora_obj.strftime('%H:%M')} \n ")

    def mostrarInfo(self):
        print(f"Cita agendada para {self.paciente.nombre} con {self.medico.nombre}")

class Tratamiento:
    def __init__(self, paciente, prescripcion, duracion, medico):
        self.paciente = paciente
        self.prescripcion = prescripcion
        self.duracion = duracion
        self.medico = medico

    def mostrarMensaje(self):
        print(f"El tratamiento dado por {self.medico.nombre} de la especialidad {self.medico.especialidad} para el paciente {self.paciente.nombre} es de {self.prescripcion} cada {self.duracion} ")


def main():
    citas_agendadas = {}
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

    #medicos = {"MD1":medico1, "MD2":medico2, "MD3":medico3, "MD4":medico4}

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

            if edad <= 12:
                tratamiento = Tratamiento(paciente, "Antibioticos infantiles", "8hrs", medico4)

            else:
                if especialidades_encontradas == ['Interna']:
                    tratamiento = Tratamiento(paciente, "Antibióticos", "8hrs", medico1)

                elif especialidades_encontradas == ['Cardiologia']:
                    tratamiento = Tratamiento(paciente, "Dieta y vida saludable", "mes", medico2)

                elif especialidades_encontradas == ['Endocrinologia']:
                    tratamiento = Tratamiento(paciente, "Dieta", "mes", medico3)

                elif edad <= 12:
                    tratamiento = Tratamiento(paciente, "Antibiotico infantil", "8hrs", medico4)

                else:
                    print("No tenemos la especialidad para curar su enfermedad")
            paciente.tratamientos.append(tratamiento)
            tratamiento.mostrarMensaje()

            pacientes[id_paciente] = {
                "nombre": nombre,
                "edad": edad,
                "sintomas": sintomas,
                "tratamiento": tratamiento
            }

        elif opt == "2":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            sintomas = input("Sintomas separadas por comas (ejemplo: Gripe, Fiebre): ").split(", ")
            id_paciente = input("Número de Seguridad Social: ")
            fecha_hora = input("Ingrese la fecha (dd/mm/yyyy HH:MM): ")

            area =  input("A que area se cita:\nInterno\nCardiología\nEndocrinologia\nPediatria\n")

            paciente = Pacientes(nombre, id_paciente, edad, sintomas)

            # Verificar si el ID ya existe en el diccionario de pacientes
            if id_paciente in citas_agendadas:
                print("El ID de paciente ya existe. Intente nuevamente.")
                continue

            # Se genera la cita
            if area == "Interno":
                cita = Citas(paciente, fecha_hora, medico1)

            elif area == "Cardiologia":
                cita = Citas(paciente, fecha_hora, medico2)

            elif area == "Endocrinologia":
                cita = Citas(paciente, fecha_hora, medico3)

            elif area == "Pediatria":
                cita = Citas(paciente, fecha_hora, medico4)

            else:
                print("No contamos con esa especialidad")

            f_h = fecha_hora
            if Citas.validar_fechahora(f_h):
                if f_h not in citas_agendadas:
                    citas_agendadas[f_h] = cita  # Agregamos la cita al diccionario
                    cita.mostrarMensaje()  # Mostramos un mensaje de confirmación
                else:
                    print("La hora no está disponible")
            else:
                print("Formato de fecha y hora incorrecto. Use dd/mm/yyyy HH:MM.")



        elif opt == "3":
            # Ordenar las citas por fecha y hora de menor a mayor
            citas_agendadas_ordenadas = sorted(citas_agendadas.items(), key=lambda x: x[0])

            if citas_agendadas_ordenadas:
                print("Citas agendadas:")
                for i, (fecha_hora, _) in enumerate(citas_agendadas_ordenadas, 1):
                    print(f"{i}. {fecha_hora}")
            else:
                print("No hay citas agendadas.")

            # Elegir cita
            cita_elegida = input("Ingrese que cita desea conocer: ")
            if cita_elegida == "0":
                continue  # Volver al menú principal

            try:
                cita_elegida = int(cita_elegida)
                if 1 <= cita_elegida <= len(citas_agendadas_ordenadas):
                    fecha_hora, cita = citas_agendadas_ordenadas[cita_elegida - 1]
                    cita.mostrarMensaje()  # Mostrar la información de la cita seleccionada
                else:
                    print("Número de cita no válido.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")

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
                tratamiento.mostrarMensaje()
            else:
                print("ID de paciente no válido. Intente nuevamente.")

        elif opt == "5":
            break

        else:
            print("Opcion no valida, intente de nuevo\n")



if __name__ == "__main__":
    main()