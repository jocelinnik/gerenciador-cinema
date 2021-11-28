from servicos.insercoes_service import InsercoesService
from servicos.migracoes_service import MigracoesService


def rodando_migracoes():
    migracoes = MigracoesService()

    migracoes.criar_tabela_sala()
    migracoes.criar_tabela_funcionario()
    migracoes.criar_tabela_funcao()
    migracoes.criar_tabela_horario()
    migracoes.criar_tabela_filme()
    migracoes.criar_tabela_indicacao()
    migracoes.criar_tabela_trabalha()
    migracoes.criar_tabela_sessao()


def rodando_insercoes():
    insercoes = InsercoesService()

    insercoes.inserir_dados_tabela_funcionarios()
    insercoes.inserir_dados_tabela_salas()
    insercoes.inserir_dados_tabela_horarios()
    insercoes.inserir_dados_tabela_filmes()
    insercoes.inserir_dados_tabela_indicacoes()
    insercoes.inserir_dados_tabela_funcoes()
    insercoes.inserir_dados_tabela_trabalha()
    insercoes.inserir_dados_tabela_sessoes()


if __name__ == "__main__":
    rodando_migracoes()
    rodando_insercoes()
