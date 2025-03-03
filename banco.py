import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect("dados.db")
cursor = conn.cursor()

# Criar uma tabela se não existir
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL,
#     cidade TEXT NOT NULL
# )
# """)

# # Inserir um dado
# cursor.execute("INSERT INTO usuarios (nome, idade, cidade) VALUES ('Alice', 25, 'São Paulo')")

# # Salvar e fechar conexão
# conn.commit()
# conn.close()

# print("Banco de dados criado com sucesso!")





# Buscar todos os usuários
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Exibir os dados
for usuario in usuarios:
    print(usuario)

# Fechar a conexão
conn.close()
