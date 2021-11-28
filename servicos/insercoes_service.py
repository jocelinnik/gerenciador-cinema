from random import randint, choice
from datetime import date

from .planilha_service import PlanilhaService
from .conector_service import ConectorMySQL


class InsercoesService:

    def __init__(self):
        self.__conector = ConectorMySQL("cinema")
        self.__service = PlanilhaService("planilhas/BASE_CINEMA.xlsx")

    def inserir_dados_tabela_funcionarios(self):
        funcionarios = self.__service.ler_aba("funcionario")
        funcionarios = funcionarios[1:]

        for funcionario in funcionarios:
            nome, data_admissao, salario, cpts = funcionario
            cpts = cpts.replace("-", "")
            salario = float(salario)

            sql = """
                INSERT INTO funcionarios (carteira_trabalho, nome, data_admissao, salario)
                VALUES (%s, %s, %s, %s)
            """
            valores = (cpts, nome, data_admissao, salario)

            self.__conector.executar_insercao(sql, valores)

    def inserir_dados_tabela_salas(self):
        salas = self.__service.ler_aba("sala")
        salas = salas[1:]

        for sala in salas:
            nome, capacidade = sala
            numero_sala = nome.split(" ")[1]

            sql = """
                INSERT INTO salas (numero_sala, capacidade)
                VALUES (%s, %s)
            """
            valores = (numero_sala, capacidade)

            self.__conector.executar_insercao(sql, valores)

    def inserir_dados_tabela_horarios(self):
        horarios = self.__service.ler_aba("horario")
        horarios = horarios[1:]

        for horario in horarios:
            if horario[0] is not None:
                sql = """
                    INSERT INTO horarios (horario)
                    VALUES (%s)
                """

                self.__conector.executar_insercao(sql, horario)

    def inserir_dados_tabela_filmes(self):
        filmes = self.__service.ler_aba("filme")
        filmes = filmes[1:]

        for filme in filmes:
            if None not in filme:
                nome_portugues, tipo, sinopse, nome_original, ano_lancamento, diretor = filme

                sql = """
                    INSERT INTO filmes (nome_original, diretor, tipo, sinopse)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (nome_original, diretor, tipo, sinopse)
                filme_id = self.__conector.executar_insercao_retornando_id(sql, valores)

                sql = """
                    INSERT INTO nome_portugues_ano_lancamento_filmes (nome_portugues, ano_lancamento, filme_id)
                    VALUES (%s, %s, %s)
                """
                valores = (nome_portugues, ano_lancamento, filme_id)
                self.__conector.executar_insercao(sql, valores)

    def inserir_dados_tabela_indicacoes(self):
        indicacoes = self.__service.ler_aba("indicação")
        indicacoes = indicacoes[1:]
        sql = """
            SELECT id FROM filmes
        """
        filmes = self.__conector.executar_selecao(sql)

        for filme in filmes:
            total_indicacoes = randint(0, len(indicacoes))
            filme_id = filme[0]

            for cont in range(0, total_indicacoes):
                indicacao = randint(0, len(indicacoes) - 1)
                indicacao = indicacoes[indicacao]
                nome, categoria = indicacao
                ano = randint(2016, date.today().year)
                ganhou = choice([True, False])

                sql = """
                    INSERT INTO indicacoes (nome, categoria, ano, premiado, filme_id)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (nome, categoria, ano, ganhou, filme_id)
                self.__conector.executar_insercao(sql, valores)

    def inserir_dados_tabela_funcoes(self):
        funcoes = self.__service.ler_aba("função")
        funcoes = funcoes[1:]

        for funcao in funcoes:
            if funcao[0] is not None:
                sql = """
                    INSERT INTO funcoes (nome_funcao)
                    VALUES (%s)
                """

                self.__conector.executar_insercao(sql, funcao)

    def inserir_dados_tabela_trabalha(self):
        sql = """
            SELECT carteira_trabalho FROM funcionarios
        """
        funcionarios = self.__conector.executar_selecao(sql)
        sql = """
            SELECT nome_funcao FROM funcoes
        """
        funcoes = self.__conector.executar_selecao(sql)
        sql = """
            SELECT horario FROM horarios
        """
        horarios = self.__conector.executar_selecao(sql)

        for horario in horarios:
            trabalhadores_no_horario = set()
            qtd_trabalhadores = len(funcoes)

            while len(trabalhadores_no_horario) < qtd_trabalhadores:
                funcionario = randint(0, len(funcionarios) - 1)
                funcionario = funcionarios[funcionario]
                trabalhadores_no_horario.add(funcionario)

            for funcao in funcoes:
                sql = """
                    INSERT INTO trabalha (chave_funcao, carteira_trabalho, horario)
                    VALUES (%s, %s, %s)
                """
                valores = (funcao[0], trabalhadores_no_horario.pop()[0], horario[0])

                self.__conector.executar_insercao(sql, valores)

    def inserir_dados_tabela_sessoes(self):
        sql = """
            SELECT horario FROM horarios
        """
        horarios = self.__conector.executar_selecao(sql)
        sql = """
            SELECT id FROM filmes
        """
        filmes = self.__conector.executar_selecao(sql)
        sql = """
            SELECT numero_sala FROM salas
        """
        salas = self.__conector.executar_selecao(sql)

        for horario in horarios:
            filmes_no_horario = []
            qtd_filmes_no_horario = len(salas)

            for cont in range(qtd_filmes_no_horario):
                filme = randint(0, len(filmes) - 1)
                filme = filmes[filme]
                filmes_no_horario.append(filme)

            cont = 0
            for sala in salas:
                sql = """
                    INSERT INTO sessoes (horario, filme_id, numero_sala)
                    VALUES (%s, %s, %s)
                """
                valores = (horario[0], filmes_no_horario[cont][0], sala[0])

                self.__conector.executar_insercao(sql, valores)
                cont += 1
