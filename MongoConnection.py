from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


class MongoDB:
    def __init__(self):
        load_dotenv()
        uri = os.getenv("DB_URI")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["Clusters"]
        self.col_hist_aluno = self.db["Historico_aluno"]
        self.col_hist_prof = self.db["Historico_prof"]

    def find(self, collection, pesquisa, projection=None):
        try:
            cursor = self.db[collection].find(pesquisa, projection)
            result = list(cursor)
            return result if result else "não encontrado."
        except Exception as e:
            return f"Erro ao buscar: {e}"

    def insert(self,collections, obj):
        try:
            self.db[collections].insert_one(obj)
        except Exception as e:
            return f"Erro ao buscar: {e}"
    def getMOngo(self):
        return self.client
