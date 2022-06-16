import pymysql.cursors
from contextlib import contextmanager
"""
CRUD COM MYSQL
"""
# GERENCIADOR DE CONTEXO - USADO PARA NÃO PRECISAR FICAR FECHANDO A CONEXÃO.
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


# INSERINDO UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 111, 220))
#         conexao.commit()

# INSERINDO UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('SILVA','CESAR',1221,2121),
#             ('CESAR', 'SILVA', 11, 222),
#             ('JOAO', 'CESAR', 22, 321)
#         ]
#         # EXECUTEMANY - INSERE VÁRIOS DADOS DE UMA VEZ
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id= %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# DELETA UMA QUANTIDADE DETERMINADA DE REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# DELETA REGISTRO ENTRE UM INTERVALO
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (1,3))
#         conexao.commit()

# ATUALIZANDO UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Mariane', 5))
#         conexao.commit()


# SELECIONA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM clientes ORDER BY id ASC LIMIT 100')  # ASC ORDEM CRESCENTE (DESC - ORDEM DECRESCENTE)
        resultado = cursor.fetchall()

        for item in resultado:
            print(item)
