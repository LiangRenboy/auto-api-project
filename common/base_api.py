import pymysql
import configparser
import os


config_path = os.getcwd()
file_path = os.path.dirname(config_path)
config_file = file_path + '\\configfile.ini'
conf = configparser.ConfigParser()
conf.read(config_file, encoding='utf-8')

host = conf.get('database', 'host')
user = conf.get('database', 'user')
password = conf.get('database', 'password')
base_name = conf.get('database', 'base_name')


class SQL(object):
    def __init__(self):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=base_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = None

    def creat_connect(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_base(self):
        self.connection.close()

    def select_one(self, table_name='testcase',field_name='case_id',value_name='1'):
        cursors = self.creat_connect()
        cursors.execute('select * from %s where %s = "%s"' % (table_name,field_name,value_name))
        result = cursors.fetchall()
        cursors.close()
        self.close_base()
        return result

    def select_all(self, table_name='testcase'):
        cursors = self.creat_connect()
        cursors.execute('select * from %s' % (table_name))
        all_result = cursors.fetchall()
        cursors.close()
        self.close_base()
        return all_result


if __name__ == '__main__':
    print(SQL().select_one(field_name='url',value_name='/api/user/stu_info'))
    print(SQL().select_all()[2])
