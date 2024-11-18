from MongoConnection import MongoDB

mongo = MongoDB()
# 1 queery

def um(mongo,nome):
    resultado = mongo.find(
            "Historico_aluno",
            {"name": nome},  # Filtra pelo RA fornecido
            {
                "_id": 0,
                "RA": 1,
                "name":1,
                "subjects.id": 1,
                "subjects.name": 1,
                "subjects.dates": 1,
                "subjects.final_grade": 1
            }
        )
    print(resultado)

def dois(mongo,nome):
    # Querry 2
    query = {
                "name": nome,
            }

    resultado = mongo.find("Historico_prof", query)
    print(resultado)

def tres(mongo,data):

    # 3 querry


    query = {
        "completion_date":data,
    }
    resultado = mongo.find("Historico_aluno",query,{
                "name":1,
            })
    print(resultado)

def quatro(mongo):
    # Querry 4
    query = {
        "isBoss": True,
    }

    resultado = mongo.find("Historico_prof", query)
    print(resultado)

def cinco(mongo):
    # Querry 5
    query = {
    "tcc_group": {
        "$exists": True,
        "$ne": None
        }
    }

    resultado = mongo.find("Historico_aluno", query,{
                "name":1,
                "tcc_group": 1
            })
    print(resultado)


