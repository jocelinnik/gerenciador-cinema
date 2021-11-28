from utils.leitor_planilhas import LeitorDePlanilhas


class PlanilhaService:

    def __init__(self, caminho):
        self.__leitor_planilhas = LeitorDePlanilhas(caminho)

    def ler_aba(self, nome_aba):
        dados = self.__leitor_planilhas.retorna_dados_de_uma_aba_da_planilha(nome_aba)

        return dados
