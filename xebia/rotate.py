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
    t_obj = threading.Thread(target=write_to_file(FILE_NAME, items_rotate))
    print t_obj.getName()
    t_obj.start()
    t_obj.join()

def minimum_element_sorted_rot_list(arr, low, high):
    """List sorted, return element."""
    if (high < low):  
        return arr[0]
    if (high == low):
        return arr[low];
    mid = low + (high - low)/2
    if (mid < high and  arr[mid+1] < arr[mid]):
       return arr[mid+1]
 
    if (mid > low and arr[mid] < arr[mid - 1]):
       return arr[mid]
 
    if (arr[high] > arr[mid]):
       return minimum_element_sorted_rot_list(arr, low, mid-1)
    return minimum_element_sorted_rot_list(arr, mid+1, high)

def find_min(items_list):
    """Find list elems.."""
    low = 0
    high = len(items_list)-1
    min_elemnt = minimum_element_sorted_rot_list(items_list, low, high)
    print "\nthe minimum element\t -->\t", min_elemnt

def main():
    rotate_handle(10)
    l = [3, 4, 5, 6, 7]
    find_min(l)

if __name__ == '__main__':
    main()