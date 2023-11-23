import mysql.connector
import credenciales
from Curso import Curso

class DAO:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
    
    def conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()
        
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()
    
        
    def registrarCurso(self, c: Curso):
        self.conectar()
        sql = "INSERT INTO curso(nombre, sala, valor, docente, tamanio_sala, seccion, duracion, tipo_sala, disponibilidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (c.get_nombre(), c.get_sala(), c.get_valor(), c.get_docente(), c.get_tamanio_sala(), c.get_seccion(), c.get_duracion(), c.get_tipo_sala(), c.get_disponibilidad())
        self.__cursor.execute(sql, values)
        self.cerrar()
    
    
    def eliminarCurso(self, id: int):
        self.conectar()
        sql = "DELETE FROM curso WHERE id = %s"
        values = (id,)
        self.__cursor.execute(sql, values)
        self.cerrar()
        
    def modificarCurso(self, c: Curso):
        self.conectar()
        sql = "UPDATE curso SET nombre = %s, sala = %s, valor = %s, docente = %s, tamanio_sala = %s, seccion = %s, duracion = %s, tipo_sala = %s, disponibilidad = %s WHERE id = %s"
        values = (c.get_nombre(), c.get_sala(), c.get_valor(), c.get_docente(), c.get_tamanio_sala(), c.get_seccion(), c.get_duracion(), c.get_tipo_sala(), c.get_disponibilidad(), c.get_id())
        self.__cursor.execute(sql, values)
        self.cerrar()

    def obtenerCursos(self):
        self.conectar()
        sql = "SELECT * FROM curso"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        self.cerrar()
        cursos = []
        for r in registros:
            cursos.append(Curso(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[0]))
        return cursos

    def obtenerCurso(self, id: int):
        self.conectar()
        sql = "SELECT * FROM curso WHERE id = %s"
        values = (id,)
        self.__cursor.execute(sql, values)
        curso = self.__cursor.fetchone()
        self.cerrar()
        if curso:
            return Curso(curso[1], curso[2], curso[3], curso[4], curso[5], curso[6], curso[7], curso[8], curso[9], curso[0])
        return None

    def obtenerCursosPorDocente(self, docente_nombre: str):
        self.conectar()
        sql = "SELECT * FROM curso WHERE docente = %s"
        values = (docente_nombre,)
        self.__cursor.execute(sql, values)
        registros = self.__cursor.fetchall()
        self.cerrar()
        cursos = []
        for r in registros:
            cursos.append(Curso(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[0]))
        return cursos

    def obtenerCursosPorDisponibilidad(self, disponibilidad: str):
        self.conectar()
        sql = "SELECT * FROM curso WHERE LOWER(disponibilidad) = LOWER(%s)"
        values = (disponibilidad,)
        self.__cursor.execute(sql, values)
        registros = self.__cursor.fetchall()
        self.cerrar()
        cursos = []
        for r in registros:
            cursos.append(Curso(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[0]))
        return cursos


    
