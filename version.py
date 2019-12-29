#!/usr/local/bin/python
# -*- encoding: utf-8 -*-

#"""
#Function: Get Version of Python\Go\Node\PHP\Ruby\Java
#"""

import os
import re

def get_result_of_cmd(cmd):
	"""Get Echo"""
	f = os.popen(cmd)
	return f.read()

def get_version_of_python():
	"""Get Python Version"""
	ret = get_result_of_cmd('python --version')
	ver = re.search(r'\d+\.\d+\.\d+', ret).group()
	print("Python Version: \t" + ver)

def get_version_of_go():
	"""Get Go Version"""
	ret = get_result_of_cmd('go version')
	ver = re.search(r'\d+\.\d+\.\d+', ret).group()
	print("Go Version: \t" + ver)

def get_version_of_node():
	"""Get Node Version"""
	ret_node = get_result_of_cmd('node --version')
	ver = re.search(r'\d+\.\d+\.\d+', ret_node).group()
	print("Node Version: \t" + ver)
	ret_npm = get_result_of_cmd('npm --version')
	ver = re.search(r'\d+\.\d+\.\d+', ret_npm).group()
	print("Npm Version: \t" + ver)

def get_version_of_php():
	"""Get PHP Version"""
	ret = get_result_of_cmd('php --version')
	ver = re.search(r'\d+\.\d+\.\d+', ret).group()
	print("PHP Version: \t" + ver)

def get_version_of_java():
	"""Get Java Version"""
	ret = get_result_of_cmd('java -version')
	ver = re.search(r'\d+\.\d+\.\d+', ret).group()
	print("Java Version: \t" + ver)


if __name__ == '__main__':
	get_version_of_python()
	get_version_of_go()
	get_version_of_node()
	#get_version_of_php()
	#get_version_of_java()
