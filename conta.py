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

    #referencia pra manipular o banco de dados
    cursor = conn.cursor()

    #criando tabelas DDL
    #cursor.execute('CREATE TABLE felipe (id int primary key generated always as identity, nome VARCHAR(30), sobrenome VARCHAR(30), idade int)')

    #inserindo dados na tabela DML
    #nome = str(input('Digite seu Nome:'))
    #sobrenome = str(input('Digite seu sobrenome: '))
    #idade = int(input('Digite sua Idade: '))

    #cursor.execute('INSERT INTO felipe (nome, sobrenome, idade) VALUES(%s, %s, %s)' , (nome, sobrenome, idade))

    #Apagando tabelas
    #cursor.execute('DROP TABLE felipe')

    #Adicionando e Apagando colunas
    #cursor.execute('ALTER TABLE felipe add COLUMN sobrenome VARCHAR(30)')
    #cursor.execute('ALTER TABLE felipe DROP COLUMN sobrenome')

    #deletando linha da tabela
    idd = (input('Digite o ID para deletar: '))
    cursor.execute('DELETE FROM felipe WHERE id = %s', (idd))
    count = cursor.rowcount
    print(count, "Deletado com sucesso")

    #editando linha da tabela
    #idd = int(input('Digite o ID para alteração: '))
    #nome = (input('Digite seu Nome:'))
    #sobrenome = (input('Digite seu sobrenome: '))
    #idade = (input('Digite sua Idade: '))

    #cursor.execute('UPDATE felipe SET nome = %s, sobrenome = %s, idade = %s WHERE id = %s', (nome, sobrenome, idade, idd))
    
    #selecionando dados DQL
    #cursor.execute('SELECT * FROM felipe')

    # variavel refencia para impressao
    #rs = cursor.fetchall()
    #print(rs)
    
    conn.commit()
    cursor.close()
    conn.close()
    



