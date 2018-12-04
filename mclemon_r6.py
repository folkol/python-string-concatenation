#!/usr/bin/python
import gc

from io import StringIO
import time, subprocess, os
from sys import argv

def method1(ss):
	out_str = ''
	for s in ss:
		out_str += s
	return out_str

def method2(ss):
	from collections import MutableString
	out_str = MutableString()
	for s in ss:
		out_str += s
	return out_str

def method3(ss):
	from array import array
	char_array = array('c')
	for s in ss:
		char_array.fromstring(s)
	return char_array.tostring()

def method4(ss):
	str_list = []
	for s in ss:
		str_list.append(s)
	out_str = ''.join(str_list)
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


def call_method(num):
	global process_size
	ss = [repr(n) for n in range(loop_count)]
	gc.disable()
	start = time.time()
	z = eval('method' + str(num))(ss)
	end = time.time()
	print(float((end-start) * 1000))
	
loop_count = 20000
pid = os.getpid()

if len(argv) == 2:
	call_method(argv[1])
elif len(argv) == 3:
	loop_count = int(argv[2])
	call_method(argv[1])
else:
	print("Usage: python stest.py <n>\n" \
		"  where n is the method number to test")
