#!/usr/bin/python 

from cStringIO import StringIO
import time, commands, os
from sys import argv

def method1(ss):
	out_str = ''
	for s in ss:
		out_str += s
	return out_str

def method2(ss):
	from UserString import MutableString
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


def ps_stats():
	global process_size
	process_size = commands.getoutput('ps -o vsz= -p ' + `pid`)
	# process_size = ps.split()[15]

def call_method(num):
	global process_size
	ss = [`n` for n in range(loop_count)]
	start = time.time()
	z = eval('method' + str(num))(ss)
	end = time.time()
	ps_stats()
	print "method", num
	print "time", float((end-start) * 1000), "ms"
	print "output size ", len(z) / 1024, "kb"
	print "process size", process_size, "kb"
	print
	
loop_count = 20000
pid = os.getpid()

if len(argv) == 2:
	call_method(argv[1])
else:
	print "Usage: python stest.py <n>\n" \
		"  where n is the method number to test"
