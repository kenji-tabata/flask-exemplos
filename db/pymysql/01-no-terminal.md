pymysql
===

Experimentando [pymysql](https://github.com/PyMySQL/PyMySQL) no terminal.

Você deve ter o __pymysql__ devidamente instalado `pip install pymysql`.


Iniciamos o Python e importamos a biblioteca.
    $ python
    >>> import pymysql

Conectamos com o banco de dados através da função `connect()`.

    >>> conn = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='mysql')
    >>> type(conn)
    <class 'pymysql.connections.Connection'>

Obtemos o cursor.

    >>> cur = conn.cursor()
    >>> type(cur)
    <class 'pymysql.cursors.Cursor'>

Executamos um SQL.

    >>> users_total = cur.execute('SELECT Host, User FROM user')

A função `execute()` retorna um inteiro com o total de registros encontrados.

    >>> type(users_total)
    <class 'int'>
    >>> users_total
    6

Também temos a propriedade `rowcount` com o mesmo valor.

    >>> cur.rowcount == users_total
    True

Avançando com o cursor, podemos ver o resultado

    >>> for row in cur:
    ...   row
    ... 
    """ mostra os resultados """

Detalhe: Se quisermos percorrer novamente a consulta devemos executá-la, faz
sentido pois havíamos avançado com o curso e agora ele está no fim do arquivo.

    >>> users_total = cur.execute('SELECT Host, User FROM user')
    >>> for row in cur:
    ...   type(row)
    ... 
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
