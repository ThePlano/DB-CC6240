from insertExamples import historico_aluno1,historico_aluno2, historico_prof1, historico_prof2
from querrys import um,dois,tres,quatro,cinco
from MongoConnection import MongoDB

mongoCLient = MongoDB()

# inserindo

mongoCLient.insert("Historico_aluno",historico_aluno1)
mongoCLient.insert("Historico_aluno",historico_aluno2)
mongoCLient.insert("Historico_prof", historico_prof1)
mongoCLient.insert("Historico_prof", historico_prof2)

# rodando as querrys

um(mongoCLient,"Maria")
dois(mongoCLient,"Pablo")
tres(mongoCLient,"232045")
quatro(mongoCLient)
cinco(mongoCLient)