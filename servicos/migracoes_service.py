from .conector_service import ConectorMySQL


class MigracoesService:

    def __init__(self):
        self.__conector = ConectorMySQL("cinema")

    def criar_tabela_sala(self):
        sql = """
            CREATE TABLE IF NOT EXISTS salas(
                numero_sala INTEGER(3) AUTO_INCREMENT PRIMARY KEY,
                capacidade INTEGER NOT NULL
            )
        """

        self.__conector.executar(sql)

    def criar_tabela_funcionario(self):
        sql = """
            CREATE TABLE IF NOT EXISTS funcionarios(
                carteira_trabalho VARCHAR(15) PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                data_admissao TIMESTAMP NOT NULL,
                salario DECIMAL(10, 2) NOT NULL
            )
        """

        self.__conector.executar(sql)

    def criar_tabela_funcao(self):
        sql = """
            CREATE TABLE IF NOT EXISTS funcoes(
                nome_funcao VARCHAR(30) PRIMARY KEY
            )
        """

        self.__conector.executar(sql)

    def criar_tabela_horario(self):
        sql = """
            CREATE TABLE IF NOT EXISTS horarios(
                horario TIME PRIMARY KEY
            )
        """

        self.__conector.executar(sql)

    def criar_tabela_filme(self):
        sql = """
            create table if not exists filmes(
                id bigint auto_increment,
                nome_original varchar(50) not null,
                diretor varchar(50) not null,
                tipo varchar(20) not null,
                sinopse text,
                primary key (id)
            )
        """
        self.__conector.executar(sql)

        sql = """
            create table if not exists nome_portugues_ano_lancamento_filmes(
                nome_portugues varchar(50) not null,
                ano_lancamento int(4) not null,
                filme_id bigint not null,
                primary key (nome_portugues, ano_lancamento),
                foreign key (filme_id) references filmes(id)
            )
        """
        self.__conector.executar(sql)

    def criar_tabela_indicacao(self):
        sql = """
            create table if not exists indicacoes(
                id bigint auto_increment,
                nome varchar(50) not null,
                categoria varchar(30) not null,
                ano int(4) not null,
                premiado bool default(false),
                filme_id bigint not null,
                primary key (id),
                foreign key (filme_id) references filmes(id)
            )
        """
        self.__conector.executar(sql)

    def criar_tabela_trabalha(self):
        sql = """
            create table if not exists trabalha(
                id bigint auto_increment,
                chave_funcao varchar(20) not null,
                carteira_trabalho varchar(15) not null,
                horario time not null,
                primary key (id),
                foreign key (chave_funcao) references funcoes(nome_funcao),
                foreign key (carteira_trabalho) references funcionarios(carteira_trabalho),
                foreign key (horario) references horarios(horario)
            )
        """
        self.__conector.executar(sql)

    def criar_tabela_sessao(self):
        sql = """
            create table if not exists sessoes(
                id bigint auto_increment,
                horario time not null,
                filme_id bigint not null,
                numero_sala int(3) not null,
                primary key (id),
                foreign key (horario) references horarios(horario),
                foreign key (filme_id) references filmes(id),
                foreign key (numero_sala) references salas(numero_sala)
            )
        """
        self.__conector.executar(sql)
