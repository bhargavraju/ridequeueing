from mysql.connector import pooling, connect
import os

# username: bfb9722e26306a

# password: 2d633907

# host_name: us-cdbr-iron-east-04.cleardb.net

host_name = os.environ.get('HOST_NAME', 'localhost')
db_name = os.environ.get('DB_NAME', 'app_db')
db_user = os.environ.get('DB_USER', 'root')
db_pass = os.environ.get('DB_PASS', 'disisjbr')
# db_port = os.environ.get('DB_PORT', 3306)
# mongo_URI = os.environ.get("MONGO_URI", 'mongodb://localhost:27017')


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MySQLConnection(metaclass=Singleton):

    def __init__(self):
        self.host = host_name
        # self.port = db_port
        self.user = db_user
        self.passwd = db_pass
        self.db = db_name
        # self.connection_pool = pooling.MySQLConnectionPool(pool_name="conn_pool",
        #                                                    pool_size=5,
        #                                                    pool_reset_session=True,
        #                                                    host=self.host,
        #                                                    database=self.db,
        #                                                    user=self.user,
        #                                                    password=self.passwd)

    def get_connection(self):
        db_connection = connect(
            host=self.host,
            user=self.user,
            password=self.passwd,
            database=self.db
        )
        return db_connection


def execute_read_query(query):
    cnx = MySQLConnection().get_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    sql_result = cursor.fetchall()
    cnx.close()
    return sql_result


def execute_modify_query(query):
    cnx = MySQLConnection().get_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    row_id = cursor.lastrowid
    cnx.commit()
    cnx.close()
    return row_id


if __name__ == '__main__':
    # cnx = MySQLConnection().get_connection()
    # cursor = cnx.cursor()
    # import datetime
    # now = datetime.datetime.now()
    # query = """insert into requests (customer_id, request_time) VALUES ({}, "{}")""".format(5, now)
    # cursor.execute(query)
    # cnx.commit()
    # cnx.close()
    pass
