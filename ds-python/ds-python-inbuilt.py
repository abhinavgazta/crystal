# list ds..
first = [1, 2, 3]
first.append(1)
first.sort()
first.index(2)

# tuple -> hashmap..
top = tuple
fruits = ("apple", "banana", "cherry")
fruits += ("guava",)
fruits += ("mango",)
fruits += ("apple",)
print("the tuple of fruits", fruits)

rock = set()
rock.add(10)
rock.add(15)
print("set of rocks", rock)

test = {}
test["one"] = 1
test["two"] = 2
for k, v in test.items():
    print("the k , v", k, v)
rat = dict(on="boost", off="call", test="good")
for k , v in rat.items():
    print('new rat..', k, v)

for k, v in rat.items():
    print("th ek , v ", k, v)
rat.get(1)

from collections import defaultdict
bat = defaultdict(list)
bat["one"].append(100)
bat["one"].append(300)
bat["two"].append(200)
print("the bat default", bat)

# sets in python
top = {10, 20, 30} # set([10])
top.add(10)
top.add(20)
bot = {50}
bot.add(40)
print("result is here", top.isdisjoint(bot), top, bot)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addNodeBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# writing more code here..
