# import mysql.connector
# from mysql.connector import Error


# class MySQLDatabase:
  
#   _cursor = None  # เก็บอินสแตนซ์เดียวของคลาส
#   @property
#   _connection = None  # เก็บการเชื่อมต่อ MySQL

#   def __init__(self,host = "localhost",user = "root",password = "alcoholshop123@",database="alcoholshop") -> None:
#       self.connection = None
#       if MySQLDatabase._connection is None:
#         try:
#           MySQLDatabase._connection = mysql.connector.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=database
#           )
#           if MySQLDatabase._connection.is_connected():
#               print("Database connection create object.")
#               MySQLDatabase._cursor = MySQLDatabase._connection.cursor()
#         except mysql.connector.Error as e:
#           print(f"Error connecting to MySQL: {e}")
#           raise
#       else:
#         print("Reusing existing connection.")
  
#   @classmethod
#   def connect(self) -> bool:
#       try:
#           self.connection = mysql.connector.connect(
#               host=self.host,
#               user=self.user,
#               password=self.password,
#               database=self.database,
#           )
#           if self.connection.is_connected():
#               print("Connected to MySQL database")
#               return True
#       except Error as e:
#           print(f"Error: {e}")
#           raise ("Error Database is not connect")
#   @staticmethod
#   def execute_query(self,query, params=None):
#       """
#       ใช้สำหรับ execute คำสั่ง SQL
#       :param query: คำสั่ง SQL
#       :param params: ค่าพารามิเตอร์ (optional)
#       :return: ผลลัพธ์ (สำหรับ SELECT) หรือ None
#       """
#       self._connection.
#       self.connection.commit()
              
#   @staticmethod
#   def close(self) -> None:
#     if self.connection and self.connection.is_connected():
#       self.connection.close()
#       print("MySQL connection closed")