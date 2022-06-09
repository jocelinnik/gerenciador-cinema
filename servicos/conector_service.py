import mysql.connector


class ConectorMySQL:

    def __init__(self, nome_banco):
        self.__conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = self.__conn.cursor()
        sql = f"CREATE DATABASE IF NOT EXISTS {nome_banco}"

        cursor.execute(sql)
        self.__conn.database = nome_banco

    def executar(self, comando_sql):
        cursor = self.__conn.cursor()

        cursor.execute(comando_sql)

    def executar_insercao(self, sql, valores):
        cursor = self.__conn.cursor()

        cursor.execute(sql, valores)
        self.__conn.commit()

    def executar_insercao_retornando_id(self, sql, valores):
        cursor = self.__conn.cursor()

        cursor.execute(sql, valores)
        self.__conn.commit()

        return cursor.lastrowid

    def executar_selecao(self, sql, valores = ()):
        cursor = self.__conn.cursor()
        cursor.execute(sql, valores)

        return cursor.fetchall()
