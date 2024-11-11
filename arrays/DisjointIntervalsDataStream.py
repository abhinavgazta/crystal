'''

Problem statement
You are given a stream of 'n' non-negative integers as the input,
and you have to group the stream of integers in the form of disjoint intervals.



Your task is to Implement the ‘DisjointIntervals’ class having the two functions:



1) The first function is ‘addInteger(int val)’, which takes an integer ‘val’ as an argument and adds it to the stream.

2) The second function is ‘getDisjointIntervals()’, which returns a summary of the integers in the stream currently as a list of disjoint intervals.


Example:

Input: 'n' = 5 , stream =  [
                  [1, 1],
                  [1, 3],
                  [2],
                  [1, 2],
                  [2],
                ]

Output: [
          [ [1, 1],  [3, 3] ],
          [ [1,3] ]
        ]

Explanation: First of all, 1 is added to the stream,
and the disjoint interval will be {1, 1}.
When 3 will be added to the stream,
then the disjoint intervals will be {1, 1}, {3, 3}.
But when 2 is added to the stream then the disjoint interval
will be {1, 3} as 2 lies between these two sets of disjoint intervals,
and both the intervals {1, 1} and {3, 3} merge.


'''

from typing import List


class DisjointIntervals:
    def __init__(self):
        # Intialise your data structures here.
        self.stream = []
        self.track_map = {}

    def addInteger(self, val) -> None:
        # Add the integer to the stream.
        self.stream.append(val)

    def getDisjointIntervals(self) -> List[List[int]]:
        # Return the disjoint intervals.
        pass


if __name__ == '__main__':
    dj = DisjointIntervals()
    stream = [
        [1, 1],
        [1, 3],
        [2],
        [1, 2],
        [2],
    ]
    # flatten out the data stream.....
    new_data_stream = [data
                       for d in stream
                       for data in d
                       ]
    print("new data stream \t", new_data_stream)
    # for data in stream:
    #     dj.addInteger(data)
