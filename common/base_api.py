import pymysql
from common.readConfig import WRConfigFile
from logs.logsfile import logger


@logger.catch()
class SQL(object):
    # @logger.catch()
    def __init__(self):
        conf = WRConfigFile().read_conf
        host = conf('database', 'host')
        user = conf('database', 'user')
        password = conf('database', 'password')
        base_name = conf('database', 'base_name')

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

    # @logger.catch()
    def select_one(self, table_name='testcase', field_name='case_id', value_name='1'):
        cursors = self.creat_connect()
        cursors.execute('select * from %s where %s = "%s"' % (table_name, field_name, value_name))
        result = cursors.fetchall()
        cursors.close()
        self.close_base()
        return result

    # @logger.catch()
    def select_all(self, table_name='testcase'):
        cursors = self.creat_connect()
        cursors.execute('select * from %s' % table_name)
        all_result = cursors.fetchall()
        cursors.close()
        self.close_base()
        return all_result


if __name__ == '__main__':
    print(SQL().select_one(field_name='url', value_name='/api/user/stu_info'))
    logger.error('error msg')
    logger.debug('debug msg')
    logger.trace('trace msg')
    logger.success('success msg')
    logger.info('info msg')
    logger.warning('warning msg')
    logger.critical('critical msg')
    print(SQL().select_all()[2])
