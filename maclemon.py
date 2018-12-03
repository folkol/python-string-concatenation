#!/usr/bin/python 

from io import StringIO
import time, subprocess, os
from sys import argv

def method1(ss):
	out_str = ''
	for s in ss:
		out_str += s
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

def method4(ss):
	out_str = ''.join(ss)
	return out_str

def method5(ss):
	file_str = StringIO()
	for s in ss:
		file_str.write(s)
	out_str = file_str.getvalue()
	return out_str

def method6(ss):
	out_str = ''.join(ss)
	return out_str


def ps_stats():
	global process_size
	process_size = subprocess.getoutput('ps -o rss= -p ' + repr(pid))
	# ps = commands.getoutput('ps -up ' + `pid`)
	# process_size = ps.split()[15]

def call_method(num):
	global process_size
	ss = [repr(s) for s in range(loop_count)]
	start = time.time()
	eval('method' + str(num))(ss)
	end = time.time()
	ps_stats()
	print(float((end-start) * 1000))
	# print()
	
loop_count = 20000
pid = os.getpid()

if len(argv) == 3:
	loop_count = int(argv[2])
	call_method(argv[1])
else:
	print("Usage: python stest.py <n>\n" \
		"  where n is the method number to test")
