import random
from collections import deque


def rotate(n, r=0, **kwargs):
	"""Rotate and write"""
	if r == 0:
		pass
	elements = []
	for x in range(n):
		elements.append(x)
	items_rotate = deque(x)
	with open("rotatedfile.txt", 'a') as file_handle:
		file_handle.write(items_rotate)



def main():
	rotate()

if __name__ == '__main__':
	main()