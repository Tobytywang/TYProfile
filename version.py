#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#"""
#Function: Get Version of Python\Go\Node\PHP\Ruby\Java
#"""

import os
import subprocess
import re

def get_result_of_cmd(cmd):
	"""获得指定命令的回显"""
	f = subprocess.check_output(cmd)
	return f

def get_version_of_test():
	"""测试函数"""
	ret = get_result_of_cmd(['which', 'python'])
	print(ret)

def get_version_of_python():
	"""解析python的脚本"""
	ret = get_result_of_cmd(['pwd']).decode()
	ret = get_result_of_cmd(['which', 'python']).decode()
	ret = get_result_of_cmd(['python', '--help']).decode()
	ret = get_result_of_cmd(['python2', '--version', '2>&1']).decode()
	print(type(ret))
	version = re.search(r'\d+(\.\d+)+', ret).group()
	version_python = type(version)
	print(version_python)
	# print(version)

def get_version_of_go():
	"""解析go的脚本"""
	ret = get_result_of_cmd(['go', 'version'])
	print(ret)

def get_version_of_node():
	"""解析node的脚本"""
	ret_node = get_result_of_cmd(['node', '--version'])
	print(ret_node)
	ret_npm = get_result_of_cmd(['npm', '--version'])
	print(ret_npm)

def get_version_of_php():
	"""解析php的脚本"""
	ret = get_result_of_cmd(['php', '--version'])
	print(ret)

def get_version_of_java():
	"""解析java的脚本"""
	ret = get_result_of_cmd(['java', '-version'])
	print(ret)


if __name__ == '__main__':
	#get_version_of_test()
	get_version_of_python()
	get_version_of_go()
	get_version_of_node()
	#get_version_of_php()
	#get_version_of_java()
