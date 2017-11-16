#config=utf8
import os
import configparser as cparser
import pymysql.cursors

#--------读取配置文件-----------
#获取当前脚本的路径
base_dir = os.path.dirname(os.path.dirname(__file__))
base_dir = str(base_dir)
base_dir = base_dir.replace('\\','/')
file_path = base_dir + '/db_conf.ini'
print(file_path)
#读取配置文件
cf = cparser.ConfigParser()
cf.read(file_path)
host = cf.get("mysql_conf",'host')
port = cf.get("mysql_conf",'port')
user = cf.get("mysql_conf",'user')
password = cf.get("mysql_conf",'password')
db_name = cf.get("mysql_conf",'db_name')
print(host,port,user,password,db_name)

#----------python操作MySQL----------
class DB():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host = host,
                                              user = user,
                                              password = password,
                                              db = db_name,
                                              charset = 'utf8mb4',
                                              cursorclass = pymysql.cursors.DictCursor
                                              )
        except :
            print("连接失败")
    #插入数据
    def insert_data(self,test_data):
        #insert into students (id,name,sex,tall)values(3,'liyue','boy','190');
        for i in test_data:
            test_data[i] = "'" + str(test_data[i]) + "'"
        key = ",".join(test_data.keys())
        value = ",".join(test_data.values())
        sql = "insert into" + " " + "student"+ "(" + key + ")" + "values" + "(" + value+ ")" + ";"
        print(sql)
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()
        """
    #清空数据表
    def clear_table(self,table_name):
        sql = "truncate table" + " "+ table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(sql=sql)
        self.connection.commit()
    #关闭连接
    def close(self):
        self.connection.close()
if __name__ == "__main__":
    db = DB()
    test_data = {"id": "1", "name": "liyue", "sex": "boy", "tall": "190"}
    db.insert_data(test_data)

