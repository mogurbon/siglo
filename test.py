from flaskext.mysql import MySQL

mysql_1 = MySQL(app, prefix=”mysql1”, host=os.getenv(“db_host”), user=os.getenv(“db_username”),password=os.getenv(“db_pass”),db=os.getenv(“db_name), autocommit=True, cursorclass=pymysql.cursors.DictCursor) mysql_2 = MySQL(app, prefix=”mysql2”, host=”host2”, user=”UN”, passwd=”&&”, db=”DB”,autocommit=True,cursorclass=pymysql.cursors.DictCursor)

@app.route(‘/’) @app.route(‘/index’) def hello():

cursor1 = mysql_1.get_db().cursor() #… cursor2 = mysql_2.get_db().cursor() #…