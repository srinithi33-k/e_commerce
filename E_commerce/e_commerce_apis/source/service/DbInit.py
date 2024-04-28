from mysql.connector import connect



class DbInit():
    def __init__(self,data_base,database_username,password,host="localhost"):
        self.database=data_base
        self.db_username=database_username
        self.password=password
        # self.port_no=port_no
        self.host=host
    def db_connector(self):
        """Title : db_connector
           Args : db object
           Returns : This function is to connect db 
                     with the creted object attributes"""
        try:
            connector=connect(database=self.database,user=self.db_username,password=self.password,host=self.host)
            return connector
        except Exception as error:
            raise Exception(error)