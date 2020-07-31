# auto_api
# 接口自动化全篇

**[csdn博客](https://blog.csdn.net/qq_42795860)**

-------------------
### 整体思路

### 1、连接mysql数据库、封装数据库方法

### 2、封装requests方法

### 3、使用unittest框架编写接口测试用例

- 调用封装的数据库方法取数据库数据
- 数据传入requests封装方法中
- 断言：响应数据是否和存在数据库中的断言字段一致，判断用例是否通过依据

### 4、执行用例

### 5、HtmlTestRunner模块生成测试报告

### 6、准备数据（接口自动化前）、清理数据（接口自动化后）

-------------------

> **注意：**虽然浏览器存储大部分时候都比较可靠，但印象笔记作为专业云存储，更值得信赖。以防万一，**请务必经常及时同步到印象笔记**。
#文件目录
- **commnon文件夹**：公共使用的类
	- **base_api.py**：连接数据库，读取数据库表数据
	- **readConfig.py**：读写configfile.ini文件配置信息
	> **注意**：**读写操作时需分开进行**，不能用同一个实例，否则会重复写入之前配置文件中存在的内容。
	- **requests_api.py**：增加auto_request，更适用项目
- **logs文件夹**：存放日志系统和项目日志
	- **logsfile.py**：配置info日志和error日志存放目录和相关配置信息
- **report文件夹**：测试报告放置在这里
- **template文件夹**：存放用例中用到的文件或图片
- **HtmlTestRunner_PY文件夹**：放置测试报告类
- **testcase文件夹**：测试用例文件存放
- **configfile.ini**：项目相关配置文件 
- **run.py**：程序运行主文件，运行main函数


## base_api.py

``` python 
@logger.catch()
    def select_one(self, table_name=None, field_name=None, value_name=None):
        cursors = self.creat_connect()
        sql = 'select * from %s where %s = "%s"' % (table_name, field_name, value_name)
        try:
            cursors.execute(sql)
            logger.success('执行查询SQL语句:{sql}', sql=sql)
        except BaseException as e:
            logger.warning('SQL语句执行异常，请检查SQL语句:{sql},异常:{e}', sql=sql, e=e)
        else:
            result = cursors.fetchall()
            logger.success('数据库返回查询数据:{result}', result=result)
            return result
        finally:
            cursors.close()
            self.close_base() 
```