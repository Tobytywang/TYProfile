#!/usr/local/bin/python
# -*- encoding: utf-8 -*-

"""
功能：获得系统中安装的python\go\node\php\ruby\java六种主要语言的版本
"""

import os

def get_result_of_cmd(cmd):
	"""获得指定命令的回显"""
	f = os.popen(cmd)
	return f.read()

def get_version_of_python():
	"""解析python的脚本"""
	ret = get_result_of_cmd('python --version')
	print(ret)

def get_version_of_go():
	"""解析go的脚本"""
	ret = get_result_of_cmd('go version')
	print(ret)

def get_version_of_node():
	"""解析node的脚本"""
	ret_node = get_result_of_cmd('node --version')
	print(ret_node)
	ret_npm = get_result_of_cmd('npm --version')
	print(ret_npm)

def get_version_of_php():
	"""解析php的脚本"""
	ret = get_result_of_cmd('php --version')
	print(ret)

def get_version_of_java():
	"""解析java的脚本"""
	ret = get_result_of_cmd('java -version')
	print(ret)


if __name__ == '__main__':
	get_version_of_python()
	get_version_of_go()
	get_version_of_node()
	get_version_of_php()
	get_version_of_java()
