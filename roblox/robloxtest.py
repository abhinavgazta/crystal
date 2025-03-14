'''
q1. read in a csv file of ratings and get the minimum threshold where the ratings are above 75%
q2.  First 2 requires you to play a game in Roblox, 25 min each.
They provide a tutorial with unlimited timing.
First game you have to design as many combinations of a car that can clear a given track with obstacles - 2 rounds in 25 min.
The second game you have to optimize generating money in a factory with just one 25 min round.
The third assessment was 30 questions of answering work-based scenarios and ranking 2 of 4 options as least effective and most effective.

You are given a binary tree T. Write a program to print the right view of the tree.
You’re given a binary tree T. Write a code to print the height of the binary tree.
For a given binary tree, write a program to connect the nodes of the binary tree that are at the same level.
For a binary search tree with unique values, two node values are given. Write a program to find the lowest common ancestors of the two nodes.
Write a code to convert a given binary tree to a Doubly Linked List (DLL) in place. The left and right pointers in the nodes are to be used as previous and next pointers, respectively, in the converted DLL.
Write a code to count the leaves in a given binary search tree BT.
Write a program function to implement the serialize and deserialize functions for a given binary search tree.
Given an array of integers, write a program to return the next greater element for each element in the array. The array comprises all distinct numbers. If a greater element doesn’t exist to the right of a given element, the value returned in that position should be -1.
You are given a linked list “L,” Write a program function to pick a random node from the linked list.
You are given a positive array with n positive integers. Write a program to determine the inversion count of the array
'''

import csv
import os
import unittest

def csv_file_works(min_arr):
    # min_arr = [2, 3, 1, 4, 5]
    # fileName = csv.reader(file)
    sort_arr = sorted(min_arr)
    n = len(min_arr)
    required_count = int(0.75 * n)
    print("cnt", required_count)
    threshold_index = n - required_count
    print("threshold", threshold_index)
    output = []
    for idx, data in enumerate(sort_arr):
        if idx > threshold_index:
            print(data)
            output.append(data)
    # print(sort_arr[threshold_index])
    return output

# class TestCSVFileWorks(unittest.TestCase):
#     def test_csvworking(self):
#         input = [2, 3, 1, 4, 5, 2, 4]
#         output = [3, 4, 4, 5]
#         self.assertEquals(csv_file_works(input), output)

if __name__ == '__main__':
    # deep test here.
    # csv_file_works(new_file)
    min_arr = [2, 3, 1, 4, 5, 2, 4]
    csv_file_works(min_arr)
    # unittest.main()
    assert csv_file_works(min_arr) == [3, 4, 4, 5], "Failed print this"
    assert csv_file_works(min_arr) == [3, 4, 4, 5], "Failed print this"
