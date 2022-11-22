'''Dentro de except coloque um print descritivo falando que você não se conectou
Logo em seguida faça um if recebendo a variável conn se ela não for nula entre no bloco if com um print descritivo informando que sua conexão está estável
Crie uma variável chamada cursor recebendo a variável conn e o methodo interno do python .cursor()
Chame a variável cursor  e o methodo interno do python .execute()
E faça a criação de uma tabela com id nome sobre nome 
Chame a variavel conn e o methodo .commit()
Chame a variável cursor e a função interna do python .close()
Chame a variável conn e a função interna do python .close()
'''

import psycopg2
# criando conexao com o banco
try:
    conn = psycopg2.connect(host = 'localhost', database = 'postgres', port = '5433', user = 'felipeweiss', password = '1234')
    print('Conexão realizada')

except:
    print('Conexao não realizada')

#condicao de conexao
if conn is not None:
    print('Conexao Estavel')

    # referencia pra manipular o banco de dados
    cursor = conn.cursor()

    

    #criando tabelas DDL
    cursor.execute('CREATE TABLE maiara (nome VARCHAR(30), sobrenome VARCHAR(30))')

    
    nome = (input('Digite seu Nome:'))
    sobrenome = (input('Digite seu sobrenome: '))

    #inserindo dados no BD DML
    cursor.execute('INSERT INTO felipe (nome, sobrenome) values (%s, %s)', (nome, sobrenome))

    # selecionando dados DQL
    
    cursor.execute('SELECT * FROM felipe')
    
    # variavel refencia para impressao
    rs = cursor.fetchall()
    print(rs)
    
    conn.commit()
    cursor.close()
    conn.close()
    



