from Curso import Curso
from DAO import DAO

def registrarCurso():
    nombre = input("Ingrese nombre del curso: ")
    docente = input("Ingrese nombre del docente: ")

   while True:
        try:
            sala = int(input("Ingrese número de la sala: "))
            if sala >= 0:
                break
            print("El número de la sala no puede ser negativo.")
        except:
            print("Debes ingresar un valor numérico entero.")

    while True:
        try:
            valor = int(input("Ingrese el valor del curso: "))
            if valor >= 0:
                break
            print("El valor del curso no puede ser negativo.")
        except:
            print("Debes ingresar un valor numérico entero.")

    while True:
        try:
            tamanio_sala = float(input("Ingrese tamaño de la sala: "))
            if tamanio_sala >= 0:
                break
            print("El tamaño de la sala no puede ser negativo.")
        except:
            print("Debes ingresar un valor numérico.")

    seccion = input("Ingrese la sección: ")

    while True:
        try:
            duracion = int(input("Ingrese duración del curso (en horas): "))
            if duracion >= 0:
                break
            print("La duración no puede ser negativa.")
        except:
            print("Debes ingresar un valor numérico entero.")

    seccion = input("Ingrese la sección: ")

    while True:
        try:
            duracion = int(input("Ingrese duración del curso (en horas): "))
            if duracion < 0:
                print("La duración no puede ser negativa.")
                break
        except:
            print("Debes ingresar un valor numérico entero.")

    while True:
        tipo_sala = input("Ingrese tipo de sala (laboratorio/aula): ").lower()
        if tipo_sala in ["laboratorio", "aula"]:
            break
        else:
            print("El tipo de sala debe ser laboratorio o aula.")

    while True:
        disponibilidad = input("Ingrese disponibilidad (ej: ocupado o disponible): ").lower()
        if disponibilidad in ["ocupado", "disponible"]:
            break
        else:
            print("La disponibilidad debe ser ocupado o disponible.")

    c = Curso(nombre, sala, valor, docente, tamanio_sala, seccion, duracion, tipo_sala, disponibilidad)
    dao = DAO()
    dao.registrarCurso(c)
    print("Curso registrado con éxito.")

def modificarCurso():
    id_curso = int(input("Ingrese ID del curso a modificar: "))
    dao = DAO()
    curso = dao.obtenerCurso(id_curso)

    if curso:
        print("Curso actual: ")
        print(curso)

        if input("cambiar nombre? (s/n): ").lower() == 's':
            curso.set_nombre(input("Ingrese nuevo nombre: "))

        if input("¿Quieres cambiar el número de sala? (s/n): ").lower() == 's':
            while True:
                try:
                    nuevo_numero = int(input("Ingrese nuevo número de sala: "))
                    if nuevo_numero > 0:
                        curso.set_sala(nuevo_numero)
                        break
                    else:
                     print("debes ingresar un número positivo.")
                except:
                    print("debes ingresar un número.")


        if input("¿quieres cambiar el nombre del docente? (s/n): ").lower() == 's':
            curso.set_docente(input("Ingrese nuevo docente: "))

        if input("¿Cambiar el valor del curso? (s/n): ").lower() == 's':
            while True:
                try:
                    nuevo_valor = int(input("Ingrese nuevo valor del curso: "))
                    if nuevo_valor > 0:
                        curso.set_valor(nuevo_valor)
                        break
                    else:
                        print("debes ingresar un número positivo.")
                except:
                     print("debes ingresar un número.")

        if input("¿Quieres cambiar el tamaño de la sala? (s/n): ").lower() == 's':
            while True:
                try:
                    nuevo_tamanio = float(input("Ingrese nuevo tamaño de sala: "))
                    if nuevo_tamanio > 0:
                        curso.set_tamanio_sala(nuevo_tamanio)
                        break
                    else:
                        print("Por favor, ingrese un número positivo.")
                except:
                    print("Entrada inválida. Por favor, ingrese un número.")


        if input("¿cambiar la seccion? (s/n): ").lower() == 's':
            curso.set_seccion(input("Ingrese nueva seccion: "))

        if input("¿Quieres cambiar la duración del curso? (s/n): ").lower() == 's':
            while True:
                try:
                    nueva_duracion = int(input("Ingresa la nueva duración del curso: "))
                    if nueva_duracion > 0:
                        curso.set_duracion(nueva_duracion)
                        break
                    else:
                        print("Por favor, ingrese un número positivo")
                except:
                    print("Entrada inválida. Por favor, ingrese un número")


        if input("¿Deseas cambiar el tipo de sala? (s/n): ").lower() == 's':
            while True:
                nuevo_tipo = input("Ingresa el nuevo tipo de sala (laboratorio/aula): ").lower()
                if nuevo_tipo in ['laboratorio', 'aula']:
                    curso.set_tipo_sala(nuevo_tipo)
                    break
                else:
                    print("debes ingresar si es laboratorio u aula")


        if input("¿Quieres cambiar la disponibilidad? (s/n): ").lower() == 's':
            while True:
                nueva_disponibilidad = input("Ingresa la disponibilidad (disponible/ocupado): ").lower()
                if nueva_disponibilidad in ['disponible', 'ocupado']:
                    curso.set_disponibilidad(nueva_disponibilidad)
                    break
                else:
                    print("debes ingresar si es disponible o ocupado")


        dao.modificarCurso(curso)
        print("Curso modificado con éxito.")
    else:
        print("Curso no encontrado.")

def eliminarCurso():
    id_curso = int(input("Ingrese ID del curso a eliminar: "))
    dao = DAO()
    if dao.obtenerCurso(id_curso):
        dao.eliminarCurso(id_curso)
        print("Curso eliminado con éxito.")
    else:
        print("Curso no encontrado.")

def mostrarCursos():
    dao = DAO()
    cursos = dao.obtenerCursos()
    for curso in cursos:
        print(curso)

def obtenerCursosPorDocente():
    docente_nombre = input("Ingrese el nombre del docente para ver sus cursos: ").lower()
    dao = DAO()
    cursos = dao.obtenerCursosPorDocente(docente_nombre)
    if cursos:
        print(f"Cursos del docente {docente_nombre}:")
        for curso in cursos:
            print(curso)
    else:
        print(f"No se encontraron cursos para el docente {docente_nombre}.")

def obtenerCursosPorDisponibilidad():
    disponibilidad = input("Ingrese la disponibilidad (disponible/ocupado) para ver los cursos correspondientes: ").lower()
    if disponibilidad not in ["disponible", "ocupado"]:
        print("La disponibilidad debe ser 'disponible' o 'ocupado'.")
        return
    dao = DAO()
    cursos = dao.obtenerCursosPorDisponibilidad(disponibilidad)
    if cursos:
        print(f"Cursos con disponibilidad '{disponibilidad}':")
        for curso in cursos:
            print(curso)
    else:
        print(f"No se encontraron cursos con disponibilidad '{disponibilidad}'.")


def main():
    while True:
        print('Menú')
        print('1.-Registrar Curso')
        print('2.-Modificar Curso')
        print('3.-Eliminar Curso')
        print('4.-Mostrar Cursos')
        print('5.-Cursos Del Docente')
        print('6.-Mostrar Cursos los cuales estan disponibles o no')
        print('7.-Salir')

        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            registrarCurso()

        elif opcion == '2':
            modificarCurso()

        elif opcion == '3':
            eliminarCurso()

        elif opcion == '4':
            mostrarCursos()

        elif opcion == '5':
            obtenerCursosPorDocente()

        elif opcion == '6':
            obtenerCursosPorDisponibilidad()

        elif opcion == '7':
            print("Hasta luego.")
            break
        else:
            print("Opción no válida, inténtelo nuevamente.")

if __name__ == "__main__":
    main()
