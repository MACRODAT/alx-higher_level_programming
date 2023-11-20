#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	for e in my_list:
		try:
			print(e)
		except e:
			break
