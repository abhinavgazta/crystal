import random
import threading
import json
from collections import deque

FILE_NAME = "rotated_file.txt"

def write_to_file(file_name, items_rotate):
	"""Writes to file."""
	with open(file_name, 'wb') as file_handle:
		value = json.dumps(items_rotate, default=str)
		file_handle.write(value)

def rotate_handle(n, r=0):
	"""Rotate and write"""
	rot = r
	if r == 0:
		rot = random.choice(range(0, n))
	elements = []
	for x in range(n):
		elements.append(x)
	items_rotate = deque(elements)
	items_rotate.rotate(rot)
	print items_rotate
	write_to_file(FILE_NAME, items_rotate)
	
def minimum_element_sorted_rot_list(items_list, low, high):
	"""List sorted, return element."""
	pass


def main():
	rotate_handle(20)

if __name__ == '__main__':
	main()