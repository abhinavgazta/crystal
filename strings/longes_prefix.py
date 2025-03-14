
def longest_prefix(strs):
    if not strs:
        return ""
    prefix_arr = []
    # iterate over a set of tuple.. zip(*strs) =
    '''
        ('f', 'f', 'f')
        ('l', 'l', 'l')
        ('o', 'o', 'i')
        ('w', 'w', 'g')
    '''
    for char in zip(*strs):
        if len(set(char)) == 1:
            prefix_arr.append(char[0])
        else:
            # break on mismatch as prefix array is to be found..
            break
    ans = ''.join(prefix_arr)
    print("prefix ans -: \t", ans)



if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    tops = ["cliwer", "dliw", "llight"]
    longest_prefix(tops)