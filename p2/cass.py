import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definir as variáveis a partir do ambiente
secure_connect_bundle_path = os.getenv('ASTRA_BUNDLE_PATH')
client_id = os.getenv('ASTRA_CLIENT_ID')
client_secret = os.getenv('ASTRA_CLIENT_SECRET')

# Verificar se as variáveis de ambiente estão definidas corretamente
if not all([secure_connect_bundle_path, client_id, client_secret]):
    raise ValueError("Verifique se todas as variáveis de ambiente estão configuradas corretamente.")

# Configuração do Astra DB com autenticação e pacote de conexão seguro
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud={'secure_connect_bundle': secure_connect_bundle_path}, auth_provider=auth_provider)
session = cluster.connect()

# Defina o keyspace que você vai usar
keyspace_name = 'fei'
session.set_keyspace(keyspace_name)

# Criar tabela historico_aluno
create_historico_aluno = """
CREATE TABLE IF NOT EXISTS historico_aluno (
    ra INT PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone_number TEXT,
    birth_date TEXT,
    course INT,
    curriculum_matrix INT,
    completion_date TEXT,
    subjects LIST<FROZEN<MAP<TEXT, TEXT>>>,
    tcc_group MAP<TEXT, TEXT>
);
"""
session.execute(create_historico_aluno)
print("Tabela historico_aluno criada com sucesso.")

# Criar tabela historico_prof
create_historico_prof = """
CREATE TABLE IF NOT EXISTS historico_prof (
    idProf INT PRIMARY KEY,
    name TEXT,
    departamento INT,
    nameDepartamento TEXT,
    isBoss BOOLEAN,
    orientadorTCC LIST<INT>,
    disciplinas LIST<FROZEN<MAP<TEXT, LIST<INT>>>>  -- Lista de disciplinas com as datas
);
"""
session.execute(create_historico_prof)
print("Tabela historico_prof criada com sucesso.")


# Função para inserir histórico do aluno
def inserir_historico_aluno(aluno):
    query = """
    INSERT INTO historico_aluno (ra, name, email, phone_number, birth_date, course, curriculum_matrix, 
                                completion_date, subjects, tcc_group)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    subjects = aluno["subjects"]
    tcc_group = aluno["tcc_group"]

    # Inserindo aluno com todas as informações
    session.execute(query, (
        aluno["RA"], aluno["name"], aluno["contact"]["email"], str(aluno["contact"]["phone_number"]),
        aluno["birth_date"], aluno["course"], aluno["curriculum_matrix"], aluno["completion_date"],
        subjects, tcc_group
    ))

    print(f"Histórico do aluno {aluno['name']} inserido com sucesso.")


# Função para inserir histórico do professor
def inserir_historico_aluno(aluno):
    query = """
    INSERT INTO historico_aluno (ra, name, email, phone_number, birth_date, course, curriculum_matrix, 
                                completion_date, subjects, tcc_group)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Ajustar os subjects para serem um formato compatível com FROZEN<MAP<TEXT, TEXT>>
    subjects = [
        {"name": subject["name"], "final_grade": str(subject["final_grade"])}
        for subject in aluno["subjects"]
    ]

    # Ajustar a estrutura do tcc_group para se tornar um MAP<TEXT, TEXT> (exemplo simples)
    tcc_group = {"title": aluno["tcc_group"]["title"], "advisor_name": aluno["tcc_group"]["advisor_name"]}

    # Inserindo aluno com todas as informações
    session.execute(query, (
        aluno["RA"], aluno["name"], aluno["contact"]["email"], str(aluno["contact"]["phone_number"]),
        aluno["birth_date"], aluno["course"], aluno["curriculum_matrix"], aluno["completion_date"],
        subjects, tcc_group
    ))

    print(f"Histórico do aluno {aluno['name']} inserido com sucesso.")

# Dados dos alunos
historico_aluno1 = {
    "RA": 23232,
    "name": "Maria",
    "contact": {"email": "jose@gmail.com", "phone_number": 119898533},
    "birth_date": "010330",
    "course": 1,
    "curriculum_matrix": 2,
    "subjects": [
        {"id": 3232, "name": "Calculus 1", "final_grade": 3, "dates": ["020424"]},
        {"id": 323222, "name": "Calculus 2", "final_grade": 2, "dates": ["020724"]},
        {"id": 32332, "name": "Calculus 3", "final_grade": 6, "dates": ["050624"]},
        {"id": 3432, "name": "Calculus 4", "final_grade": 6, "dates": ["050624"]}
    ],
    "tcc_group": {"id": 8998, "title": "Salary Expectations", "advisor_id": 43434, "advisor_name": "Jose",
                  "group_members": [
                      {"id": 34232, "name": "Lucas"},
                      {"id": 36232, "name": "Jose"},
                      {"id": 37232, "name": "Ronaldo"}
                  ]},
    "completion_date": "232045"
}

historico_aluno2 = {
    "RA": 23265,
    "name": "Jose",
    "contact": {"email": "jose@gmail.com", "phone_number": 119898533},
    "birth_date": "010330",
    "course": 1,
    "curriculum_matrix": 2,
    "subjects": [
        {"id": 3232, "name": "Calculus 1", "final_grade": 3, "dates": ["020424"]},
        {"id": 323222, "name": "Calculus 2", "final_grade": 2, "dates": ["020724"]},
        {"id": 32332, "name": "Calculus 3", "final_grade": 6, "dates": ["050624"]},
        {"id": 3432, "name": "Calculus 4", "final_grade": 6, "dates": ["050624"]}
    ],
    "tcc_group": {"id": 8998, "title": "Salary Expectations", "advisor_id": 43434, "advisor_name": "Jose",
                  "group_members": [
                      {"id": 34232, "name": "Lucas"},
                      {"id": 36232, "name": "Jose"},
                      {"id": 37232, "name": "Ronaldo"}
                  ]},
    "completion_date": "232045"
}

# Dados dos professores
historico_prof1 = {
    "idProf": 35534,
    "name": "Pablo",
    "departamento": 4343,
    "nameDepartamento": "Matematica",
    "isBoss": True,
    "OrientadorTCC": [234234, 42342, 646345, 645645],
    "diciplinas": [
        {"id": 313232, "name": "CALCULO 1", "data": [203045, 60723]},
        {"id": 3232, "name": "CALCULO 2", "data": [203045, 60723]},
        {"id": 7667, "name": "CALCULO 3", "data": [203045, 60723]}
    ]
}

historico_prof2 = {
    "idProf": 5689,
    "name": "Lari",
    "departamento": 4343,
    "nameDepartamento": "Matematica",
    "isBoss": True,
    "OrientadorTCC": [234234, 42342, 646345, 645645],
    "diciplinas": [
        {"id": 313232, "name": "CALCULO 1", "data": [203045, 60723]},
        {"id": 3232, "name": "CALCULO 2", "data": [203045, 60723]},
        {"id": 7667, "name": "CALCULO 3", "data": [203045, 60723]}
    ]
}

# Inserir históricos de alunos e professores
inserir_historico_aluno(historico_aluno1)
inserir_historico_aluno(historico_aluno2)
