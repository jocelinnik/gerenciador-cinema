import openpyxl
import os


class LeitorDePlanilhas:

    def __init__(self, caminho):
        caminho_completo = os.path.join(caminho)
        print(caminho_completo)
        self.__planilha = openpyxl.load_workbook(caminho_completo)

    def retorna_dados_de_uma_aba_da_planilha(self, nome_aba):
        return list(self.__planilha[nome_aba].values)
