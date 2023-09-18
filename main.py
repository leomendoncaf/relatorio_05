from database import Database
from writeAJson import writeAJson
from livroModel import LivroModel
from cli import LivroCLI

db = Database(database="relatorio_05", collection="livros")
personModel = LivroModel(database=db)


# Criar uma instância do modelo de livros
livro_model = LivroModel(db)

# Criar uma instância do CLI de Livros
livro_cli = LivroCLI(livro_model)

# Executar o CLI de Livros
livro_cli.run()
