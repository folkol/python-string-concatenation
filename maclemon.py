#!/usr/bin/python 

from io import StringIO
import time, subprocess, os
from sys import argv

def method1():
	out_str = ''
	for num in range(loop_count):
		out_str += repr(num)
	return out_str

def method2():
	from collections import MutableString
	out_str = MutableString()
	for num in range(loop_count):
		out_str += repr(num)
	return out_str

def method3():
	from array import array
	char_array = array('c')
	for num in range(loop_count):
		char_array.fromstring(repr(num))
	return char_array.tostring()

def method4():
	str_list = []
	for num in range(loop_count):
		str_list.append(repr(num))
	out_str = ''.join(str_list)
	return out_str

def method5():
	file_str = StringIO()
	for num in range(loop_count):
		file_str.write(repr(num))
	out_str = file_str.getvalue()
	return out_str

def method6():
	out_str = ''.join([repr(num) for num in range(loop_count)])
	return out_str


def ps_stats():
	global process_size
	process_size = subprocess.getoutput('ps -o rss= -p ' + repr(pid))
	# ps = commands.getoutput('ps -up ' + `pid`)
	# process_size = ps.split()[15]

def call_method(num):
	global process_size
	start = time.time()
	z = eval('method' + str(num))()
	end = time.time()
	ps_stats()
	print("method", num)
	print("time", float((end-start) * 1000), "ms")
	print("output size ", len(z) / 1024, "kb")
	print("process size", process_size, "kb")
	print()
	
loop_count = 20000
pid = os.getpid()

if len(argv) == 2:
	call_method(argv[1])
else:
	print("Usage: python stest.py <n>\n" \
		"  where n is the method number to test")
