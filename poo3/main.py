from Curso import Curso
from DAO import DAO

def registrarCurso():
    nombre = input("Ingrese nombre del curso: ")
    docente = input("Ingrese nombre del docente: ")
   
    while True:
        try:
            sala = int(input("Ingrese número de la sala: "))
            break
        except:
            print("debes ingresar un valor numerico")

    while True:
        try:
            valor = int(input("Ingrese el valor del curso: "))
            break
        except:
            print("debes ingresar un valor numerico")
 
    while True:
        try:
            tamanio_sala = float(input("Ingrese tamaño de la sala: "))
            break
        except:
            print("debes ingresar un valor numerico")

    seccion = input("Ingrese la sección: ")

    while True:
        try:
            duracion = int(input("Ingrese duración del curso (en horas): "))
            break
        except:
            print("debes ingresar un valor numerico")

    while True:
        try:
            tipo_sala = input("Ingrese tipo de sala (laboratorio/aula): ").lower()
            if tipo_sala in ["laboratorio", "aula"]:
                break
        except:
            print("el tipo de sala debe ser laboratorio o aula")

    while True:
        try:
            disponibilidad = input("Ingrese disponibilidad (ej: ocupado o disponible): ").lower()
            if disponibilidad in ["ocupado", "disponible"]:
                break
        except:
            print("La disponibilidad debe ser ocupado o disponible")

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
        
        if input("¿quieres cambiar el número de sala? (s/n): ").lower() == 's':
            curso.set_sala(int(input("Ingrese nuevo número de sala: ")))
        
        if input("¿quieres cambiar el nombre del docente? (s/n): ").lower() == 's':
            curso.set_docente(input("Ingrese nuevo docente: "))

        if input("¿cambiar el valor del curso? (s/n): ").lower() == 's':
            curso.set_valor(int(input("Ingrese nuevo valor del curso: ")))

        if input("¿quieres cambiar el tamaño de la sala? (s/n): ").lower() == 's':
            curso.set_tamanio_sala(float(input("Ingrese nuevo tamaño de sala: ")))

        if input("¿cambiar la seccion? (s/n): ").lower() == 's':
            curso.set_seccion(input("Ingrese nueva seccion: "))

        if input("¿quieres cambiar la duracion del curso? (s/n): ").lower() == 's':
            curso.set_duracion(int(input("Ingresa la nueva duracion del curso: ")))
        
        if input("¿deseas cambiar el tipo de sala? (s/n): ").lower() == 's':
            curso.set_tipo_sala(input("Ingresa el nuevo tipo de sala: "))

        if input("¿quieres cambiar la disponibilidad? (s/n): ").lower() == 's':
            curso.set_disponibilidad(input("Ingresa la disponibilidad: "))

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