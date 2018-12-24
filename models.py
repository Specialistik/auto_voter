from peewee import MySQLDatabase
mysql_db = MySQLDatabase('business_gazeta', user='root', password='1f53601c',host='localhost', port=3306)

#db = SqliteDatabase('people.db')
#pg_db = PostgresqlDatabase('my_app', user='postgres', password='secret', host='10.1.0.9', port=5432)

class UserAgent(Model):
    user_agent = CharField(unique=True)

    class Meta:                                           
        database = mysql_db
        db_table = 'user_agents'     

class Proxy(Model):
    host_port = CharField(unique=True)
    login_pass CharField(NULL = True)

    class Meta:
        database = mysql_db
        db_table = 'proxies'
