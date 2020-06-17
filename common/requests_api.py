import requests
import configparser
import os

config_path = os.getcwd()
file_path = os.path.dirname(config_path)
config_file = file_path + '\\configfile.ini'
conf = configparser.ConfigParser()
conf.read(config_file)

url_head = conf.get('requests_setting','url_head')
User_Agent = conf.get('requests_setting','User-agent')
Host = conf.get('requests_setting','Host')
Accept = conf.get('requests_setting','Accept')
Content_Type = conf.get('requests_setting','Content-Type')

class request_method():
	def __init__(self):
		self.headers_default = (
			"'Accept':'%s','Host':'%s','Content-Type':'%s','User-Agent':'%s',"
			% (Accept,Host,Content_Type,User_Agent))

	def auto_get(self,url='',headers=''):
		all_url = str(url_head) + str(url)
		all_headers = "{" + self.headers_default +"%s }" % (headers)

		print(all_url)
		print(all_headers)

	def auto_post(self):
		pass

if __name__ == '__main__':
	print(request_method().auto_get())


