from pymongo import MongoClient
from bson.objectid import ObjectId

# Schema para validação dos documentos JSON
livro_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": ["integer", "string"]},
        "titulo": {"type": "string"},
        "autor": {"type": "string"},
        "ano": {"type": "integer"},
        "preco": {"type": "number"},
    },
    "required": ["_id", "titulo", "autor", "ano", "preco"],
}

class LivroModel:
    def __init__(self, database):
        self.db = database
        self.collection = self.db['livros']

    def create_livro(self, livro_data):
        try:
            # Valida o documento JSON usando o schema
            jsonschema.validate(instance=livro_data, schema=livro_schema)
            
            res = self.collection.insert_one(livro_data)
            print(f"Livro criado com ID: {res.inserted_id}")
            return res.inserted_id
        except InvalidDocument as e:
            print(f"Erro de validação: {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id):
        try:
            res = self.collection.find_one({"_id": id})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def update_livro(self, id, livro_data):
        try:
            # Valida o documento JSON usando o schema
            jsonschema.validate(instance=livro_data, schema=livro_schema)
            
            res = self.collection.update_one({"_id": id}, {"$set": livro_data})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except InvalidDocument as e:
            print(f"Erro de validação: {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id):
        try:
            res = self.collection.delete_one({"_id": id})
            print(f"Livro excluído: {res.deleted_count} documento(s) excluídos")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir o livro: {e}")
            return None