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
    # 查询
    def select_skg_profit_record(self,sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        self.connection.commit()
        return result
    #关闭连接
    def close(self):
        self.connection.close()
if __name__ == "__main__":
    db = DB()
    # 千聊流水表
    sql = "select profit_type_ as 付费类型类型,profit_obj_ as 收费类型,profits_ as  收费比例,amount_ as 付款金额,money_ as 获利 " +\
          "from skg_profit_record ORDER BY create_time_ DESC limit 5"
    data = db.select_skg_profit_record(sql)
    for i in data:
        print(i)
    # print("付费类型类型：",data[0]['profit_type_'])
    # print("收费类型：",data[0]['profit_obj_'])
    # print("收费比例：",data[0]['profits_'])
    # print("付款金额：",data[0]['amount_'])
    # print("获利：",data[0]['money_'])

