from neo4j import GraphDatabase

# Dados de exemplo
historico_aluno1 = {
    "RA": 23232,
    "name": "Maria",
    "contact": {
        "email": "jose@gmail.com",
        "phone_number": 119898533
    },
    "birth_date": "010330",
    "course": 1,
    "curriculum_matrix": 2,
    "subjects": [
        {
            "id": 3232,
            "name": "Calculus 1",
            "final_grade": 3,
            "dates": ["020424"]
        },
        {
            "id": 323222,
            "name": "Calculus 2",
            "final_grade": 2,
            "dates": ["020724"]
        },
        {
            "id": 32332,
            "name": "Calculus 3",
            "final_grade": 6,
            "dates": ["050624"]
        },
        {
            "id": 3432,
            "name": "Calculus 4",
            "final_grade": 6,
            "dates": ["050624"]
        }
    ],
    "tcc_group": {
        "id": 8998,
        "title": "Salary Expectations",
        "advisor_id": 43434,
        "advisor_name": "Jose",
        "group_members": [
            {
                "id": 34232,
                "name": "Lucas"
            },
            {
                "id": 36232,
                "name": "Jose"
            },
            {
                "id": 37232,
                "name": "Ronaldo"
            }
        ]
    },
    "completion_date": "232045"
}

historico_aluno2 = {
    "RA": 23265,
    "name": "jose",
    "contact": {
        "email": "jose@gmail.com",
        "phone_number": 119898533
    },
    "birth_date": "010330",
    "course": 1,
    "curriculum_matrix": 2,
    "subjects": [
        {
            "id": 3232,
            "name": "Calculus 1",
            "final_grade": 3,
            "dates": ["020424"]
        },
        {
            "id": 323222,
            "name": "Calculus 2",
            "final_grade": 2,
            "dates": ["020724"]
        },
        {
            "id": 32332,
            "name": "Calculus 3",
            "final_grade": 6,
            "dates": ["050624"]
        },
        {
            "id": 3432,
            "name": "Calculus 4",
            "final_grade": 6,
            "dates": ["050624"]
        }
    ],
    "tcc_group": {
        "id": 8998,
        "title": "Salary Expectations",
        "advisor_id": 43434,
        "advisor_name": "Jose",
        "group_members": [
            {
                "id": 34232,
                "name": "Lucas"
            },
            {
                "id": 36232,
                "name": "Jose"
            },
            {
                "id": 37232,
                "name": "Ronaldo"
            }
        ]
    },
    "completion_date": "232045"
}

historico_prof1 = {
    "idProf" : 35534,
    "name": "robert",
    "departamento":4343,
    "nameDepartamento":"MAtematia",
    "isBoss":True,
    "OrientadorTCC":[234234,42342,646345,645645],
    "diciplinas":
            [
                {
                    "id": 313232,
                    "name":"CALCULO 1",
                    "data":[203045, 60723]
                },
                {
                    "id": 3232,
                    "name":"CALCULO 2",
                    "data":[203045, 60723]

                },
                {
                    "id": 7667,
                    "name":"CALCULO 3",
                    "data":[203045, 60723]

                }
            ]
}

historico_prof2 = {
    "idProf" : 5689,
    "name": "Saouti",
    "departamento":4343,
    "nameDepartamento":"MAtematia",
    "isBoss":True,
    "OrientadorTCC":[234234,42342,646345,645645],
    "diciplinas":
            [
                {
                    "id": 313232,
                    "name":"CALCULO 1",
                    "data":[203045, 60723]
                },
                {
                    "id": 3232,
                    "name":"CALCULO 2",
                    "data":[203045, 60723]

                },
                {
                    "id": 7667,
                    "name":"CALCULO 3",
                    "data":[203045, 60723]

                }
            ]
}

# Configuração do banco de dados
uri = "neo4j+s://9ade03c8.databases.neo4j.io"
username = "neo4j"
password = "OgFvReUAhVviI14zMSm02zwp12sLBvLTd4qeZKybRqk"

# Estabelecendo a conexão com o banco de dados
driver = GraphDatabase.driver(uri, auth=(username, password))


# Função para criar os nós no banco de dados Neo4j
def criar_aluno(tx, aluno):
    # Criando o nó do aluno
    aluno_query = """
    CREATE (a:Aluno {RA: $RA, name: $name, birth_date: $birth_date, completion_date: $completion_date})
    """
    tx.run(aluno_query, RA=aluno["RA"], name=aluno["name"], birth_date=aluno["birth_date"],
           completion_date=aluno["completion_date"])

    # Criando os nós das disciplinas e os relacionamentos com o aluno
    for disciplina in aluno["subjects"]:
        tx.run("""
        MERGE (d:Disciplina {id: $id, name: $name})
        CREATE (a)-[:CURSOU]->(d)
        SET d.final_grade = $final_grade, d.dates = $dates
        """, id=disciplina["id"], name=disciplina["name"], final_grade=disciplina["final_grade"],
               dates=disciplina["dates"])

    # Criando o nó do grupo de TCC e relacionando com o aluno
    tcc_group = aluno["tcc_group"]
    tx.run("""
    MERGE (tcc:TCC {id: $id, title: $title, advisor_name: $advisor_name})
    CREATE (a)-[:FAZ_PAR_DE]->(tcc)
    """, id=tcc_group["id"], title=tcc_group["title"], advisor_name=tcc_group["advisor_name"])

    # Relacionando os membros do grupo de TCC
    for membro in tcc_group["group_members"]:
        tx.run("""
        MERGE (m:Aluno {id: $id, name: $name})
        CREATE (m)-[:FAZ_PAR_DE]->(tcc)
        """, id=membro["id"], name=membro["name"])


# Função para criar os nós dos professores
def criar_professor(tx, professor):
    # Criando o nó do professor
    professor_query = """
    CREATE (p:Professor {idProf: $idProf, name: $name, isBoss: $isBoss, nameDepartamento: $nameDepartamento})
    """
    tx.run(professor_query, idProf=professor["idProf"], name=professor["name"],
           isBoss=professor["isBoss"], nameDepartamento=professor["nameDepartamento"])

    # Criando os nós das disciplinas do professor e os relacionamentos
    for disciplina in professor["diciplinas"]:
        tx.run("""
        MERGE (d:Disciplina {id: $id, name: $name})
        CREATE (p)-[:LECIONA]->(d)
        SET d.data = $data
        """, id=disciplina["id"], name=disciplina["name"], data=disciplina["data"])

    # Criando os relacionamentos de orientação de TCC
    for orientando_id in professor["OrientadorTCC"]:
        tx.run("""
        MATCH (a:Aluno {RA: $RA})
        MATCH (p:Professor {idProf: $idProf})
        CREATE (p)-[:ORIENTA_TCC]->(a)
        """, RA=orientando_id, idProf=professor["idProf"])


# Função principal para inserir os dados
def inserir_dados():
    with driver.session() as session:
        # Inserindo os dados dos alunos
        session.execute_write(criar_aluno, historico_aluno1)
        session.execute_write(criar_aluno, historico_aluno2)

        # Inserindo os dados dos professores
        session.execute_write(criar_professor, historico_prof1)
        session.execute_write(criar_professor, historico_prof2)


# Chama a função para inserir os dados no banco de dados Neo4j
inserir_dados()

# Fechando a conexão com o Neo4j
driver.close()

