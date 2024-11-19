from neo4j import GraphDatabase

uri = "neo4j+s://9ade03c8.databases.neo4j.io"
username = "neo4j"
password = "OgFvReUAhVviI14zMSm02zwp12sLBvLTd4qeZKybRqk"

# Estabelecendo a conexão com o banco de dados
driver = GraphDatabase.driver(uri, auth=(username, password))

def historico_escolar_por_nome(tx, nome_aluno):
    query = """
    MATCH (a:Aluno {name: $nome_aluno})-[:CURSOU]->(d:Disciplina)
    UNWIND d.dates AS data 
    WITH a, d, data, d.final_grade AS nota_final 
    RETURN d.id AS codigo_disciplina, 
           d.name AS nome_disciplina, 
           data AS semestre_ano, 
           nota_final  
    ORDER BY data
    """
    result = tx.run(query, nome_aluno=nome_aluno)
    return [{"codigo_disciplina": record["codigo_disciplina"],
             "nome_disciplina": record["nome_disciplina"],
             "semestre_ano": record["semestre_ano"],
             "nota_final": record["nota_final"]}
            for record in result]

def historico_disciplinas_professor_func(tx, id_professor):
    query = """
    MATCH (p:Professor {idProf: $id_professor})-[:LECIONA]->(d:Disciplina)
    RETURN d.id AS codigo, d.name AS nome, d.data AS semestre_ano
    """
    result = tx.run(query, id_professor=id_professor)
    return [{"codigo": record["codigo"], "nome": record["nome"], "semestre_ano": record["semestre_ano"]} for record in result]

def alunos_formadoss(tx):
    query = """
    MATCH (a:Aluno)
    WHERE a.completion_date IS NOT NULL 
    RETURN a.name AS nome_aluno, a.completion_date AS data_formacao
    ORDER BY a.completion_date
    """
    result = tx.run(query)
    return [{"nome_aluno": record["nome_aluno"], "data_formacao": record["data_formacao"]}
            for record in result]


def professores_chefes_func(tx):
    query = """
    MATCH (p:Professor)
    WHERE p.isBoss = true
    RETURN p.name AS nome, p.nameDepartamento AS departamento
    """
    result = tx.run(query)
    return [{"nome": record["nome"], "departamento": record["departamento"]} for record in result]

def alunos_tcc_orientadorr(tx):
    query = """
    MATCH (p:Professor)-[:ORIENTA_TCC]->(a:Aluno)
    MATCH (a:Aluno)-[:FAZ_PAR_DE]->(tcc:TCC)
    RETURN a.name AS nome_aluno, p.name AS nome_professor_orientador, tcc.title AS titulo_tcc
    ORDER BY a.name
    """
    result = tx.run(query)
    return [{"nome_aluno": record["nome_aluno"],
             "nome_professor_orientador": record["nome_professor_orientador"],
             "titulo_tcc": record["titulo_tcc"]}
            for record in result]

def executar_consultas():
    with driver.session() as session:
        # Exemplo de uso da função 1
        historico_aluno = session.execute_read(historico_escolar_por_nome, "Maria")  # RA do aluno
        print("Histórico Escolar:", historico_aluno)

        # Exemplo de uso da função 2
        historico_disciplinas = session.execute_read(historico_disciplinas_professor_func, 35534)  # ID do professor
        print("Histórico de Disciplinas Ministradas:", historico_disciplinas)

        # Exemplo de uso da função 3
        alunos_formados = session.execute_read(alunos_formadoss)  # Semestre e Ano
        print("Alunos Formados:", alunos_formados)

        # Exemplo de uso da função 4
        professores_chefes = session.execute_read(professores_chefes_func)
        print("Professores Chefes:", professores_chefes)

        # Exemplo de uso da função 5
        alunos_tcc_orientador = session.execute_read(alunos_tcc_orientadorr)
        print("Alunos e seus TCCs:", alunos_tcc_orientador)

# Chama a função para executar as consultas no banco de dados Neo4j
executar_consultas()
