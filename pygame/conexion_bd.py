import sqlite3
import re

def crear_database():
    with sqlite3.connect("ejercicios.py/pygame/database_carreras.db") as conexion:
        try:
            sentencia = ''' create table ranking
            (
            id integer primary key autoincrement,
            nombre text,
            score integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla ranking")                       
        except sqlite3.OperationalError:
            print("La tabla ranking ya existe")
        finally:
            print("Ver ranking")


def guardar_puntaje(nombre_usuario, score):
    with sqlite3.connect("ejercicios.py/pygame/database_carreras.db") as conexion:
        sentencia = "INSERT INTO ranking (nombre, score) VALUES (?,?)"
        conexion.execute(sentencia, (nombre_usuario, score))
        conexion.commit()


# def mostrar_puntaje():
#     with sqlite3.connect("ejercicios.py/pygame/database_carreras.db") as conexion:
#         ranking = []
#         nombres = conexion.execute("SELECT nombre FROM ranking ORDER BY score DESC LIMIT 10")
#         scores = conexion.execute("SELECT score FROM ranking ORDER BY score DESC LIMIT 10")
#         for nombre, score in zip(nombres, scores):
#             ranking_usuario = {}
#             ranking_usuario['nombre'] = nombre
#             ranking_usuario['score'] = score
#             ranking.append(ranking_usuario)
#         return ranking

def mostrar_puntaje():
    with sqlite3.connect("ejercicios.py/pygame/database_carreras.db") as conexion:
        ranking = []
        puntaje = conexion.execute("SELECT * FROM ranking ORDER BY score DESC LIMIT 10")
        for puntos in puntaje:
            ranking_usuario = {}
            ranking_usuario['nombre'] = puntos[1]
            ranking_usuario['score'] = puntos[2]
            ranking.append(ranking_usuario)
        return ranking


