from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'gerardo'
app.config['MYSQL_PASSWORD'] = 'petra123'
app.config['MYSQL_DB'] = 'siglo'

mysql = MySQL(app)



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route


@app.route('/usuarios', methods=['GET'])
def usuarios():


    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM mysql.usuarios''')
    rv = cursor.fetchall()
    return str(rv)


if __name__ == '__main__':
    app.run()



