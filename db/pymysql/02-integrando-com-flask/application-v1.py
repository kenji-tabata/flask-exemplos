# coding: utf-8
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    import pymysql
    conn = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='mysql')

    cur = conn.cursor()

    users_total = cur.execute('SELECT Host, User FROM user')

    class User():
        pass

    users = []
    for row in cur:
        user = User()
        user.host  = row[0]
        user.login = row[1]
        users.append(user)

    cur.close()
    conn.close()

    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug = True)