import configparser
import os


class WRConfigFile(object):
    def __init__(self):
        """
        配置ini文件路径
        strict: 是否允许单一配置文件中有相同的section或同一section中有相同option
        """
        self.config_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\configfile.ini'
        self.conf = configparser.ConfigParser(strict=False)

    def read_conf(self, section, option):
        """
        读取ini文件的section和option，判断section和option是否存在，返回option字段的值
        :param section:ini文件的section字段
        :param option:ini文件section下的option字段
        :return: 返回option字段的值
        """
        self.conf.read(self.config_file, encoding='utf-8')
        if self.conf.has_section(section=section):
            if self.conf.has_option(section=section, option=option):
                result = self.conf.get(section=section, option=option)
                return result

    def write_conf(self, option, value, section='test'):
        """
        读取ini文件追加写入section、option、values值
        :param section:ini文件的section字段
        :param option:ini文件section下的option字段
        :param value:option字段的值
        确定section字段是否存在时只能读取当次文件操作时是否存在相同section字段，
        save_conf文件之后，第二次操作读取不了section字段，需要read配置文件才能读取，read配置文件读写时又会写入之前配置文件中存在的内容。
        因为技术菜，看不懂源码，所以就这样写了
        """
        # self.conf.read(self.config_file, encoding='utf-8')
        section_values = self.conf.has_section(section)
        print(section_values)
        if not section_values:
            self.conf.add_section(section)
        self.conf.set(section=section, option=option, value=value)
        # self.conf.clear()

    def sava_conf(self):
        """
        保存修改的ini文件
        """
        fp = open(self.config_file, 'a', encoding='utf-8')
        self.conf.write(fp=fp)
        fp.close()


if __name__ == '__main__':
    print(WRConfigFile().read_conf('database', 'host'))
    print(WRConfigFile().read_conf('test', 'name'))
    print(WRConfigFile().read_conf('test', 'sex'))
    wrc = WRConfigFile()
    wrc.write_conf('name', '小红')
    wrc.write_conf('sex', '小白')
    wrc.write_conf('age', '小黑')
    wrc.write_conf('phone', '小绿')
    wrc.sava_conf()


