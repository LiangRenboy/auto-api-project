import pymysql
from common.readConfig import WRConfigFile
from logs.logsfile import logger


class SQL(object):
    @logger.catch()
    def __init__(self):
        conf = WRConfigFile().read_conf
        host = conf('database', 'host')
        user = conf('database', 'user')
        password = conf('database', 'password')
        base_name = conf('database', 'base_name')
        try:
            logger.info('正在连接数据库,数据库地址={host},用户名={user},数据库密码={password},数据库名称={base_name}',
                        host=host, user=user, password=password, base_name=base_name)
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=base_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        except BaseException as e:
            logger.warning('数据库连接时发生异常:{e}', e=e)
        else:
            logger.success('连接数据库成功')
        self.cursor = None

    def creat_connect(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_base(self):
        self.connection.close()
        logger.success('关闭数据库成功')

    @logger.catch()
    def select_one(self, table_name='testcase', field_name='case_id', value_name='1'):
        cursors = self.creat_connect()
        sql = 'select * from %s where %s = "%s"' % (table_name, field_name, value_name)
        cursors.execute(sql)
        logger.success('执行查询语句:{sql}', sql=sql)
        result = cursors.fetchall()
        logger.success('返回查询数据:{result}', result=result)
        cursors.close()
        self.close_base()
        return result

    @logger.catch()
    def select_all(self, table_name='testcase'):
        cursors = self.creat_connect()
        sql = 'select * from %s' % table_name
        cursors.execute(sql)
        logger.success('执行查询sql语句:{sql}', sql=sql)
        all_result = cursors.fetchall()
        logger.success('返回查询数据:{all_result}', all_result=all_result)
        cursors.close()
        self.close_base()
        return all_result


if __name__ == '__main__':
    SQL().select_one(field_name='url', value_name='/api/user/stu_info')
    SQL().select_all()[2]
