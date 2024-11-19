
historico_aluno1 =  {
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
historico_aluno2 =  {
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
    "name": "Pablo",
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
    "name": "Lari",
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

from MongoConnection import MongoDB

mongo = MongoDB()
mongo.insert("Historico_aluno", historico_prof1)
mongo.insert("Historico_prof", historico_aluno2)