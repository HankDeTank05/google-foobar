"""
THIS IS MEANT TO BE THE REVERSE OF bomb_baby.py's SOLUTION
instead of starting from 1,1 and searching downwards, start from tm, tf and work backwards towards 1,1
If 1,1 is reachable, return the shortest number of moves to get there
If 1,1 is NOT reachable, return "impossible"
"""
import copy
import time
import numpy as np
def solution(m, f):
    tm = long(m)
    tf = long(f)
    if tm == tf-1 or tf == tm-1:
        return str(min(tm, tf))
    elif tm == tf and tf == 1:
        return str(0)
    elif tm == tf/2 or tf == tm/2:
        return "impossible"
    elif min(tm, tf) == 1 and max(tm, tf) > 1:
        return str(max(tm, tf)-1)
    depth_limit = 0
    root = ((tm, tf), 0)
    found = False
    failed = False
    repeat_comparison = None
    # perform iterative depth search
    first_encounters = []
    while not failed:
        #print()
        print('depth_limit = {}'.format(depth_limit))
        #time.sleep(2)
        # perform a depth-bounded search
        if depth_limit == 0:
            if (1, 1) == root[0]:
                return root[1]
        else:
            depth = 0
            if depth_limit == 1:
                first_encounters = [root]
            previous_first_encounters = copy.deepcopy(first_encounters)
            first_encounters = []

            while len(previous_first_encounters) > 0:
                #time.sleep(1)
                #print('stack size: {}'.format(len(frontier_stack)))
                # remove node from the stack
                node = previous_first_encounters.pop()

                # make sure we aren't infinitely repeating ourselves
                #if repeat_comparison is not None and node == repeat_comparison:
                    #print('REPEAT FOUND')
                    #break

                mach = long(node[0][0])
                facula = long(node[0][1])

                node_depth = node[1]
                #print('node {}'.format(node))
                # determine if node is the goal or not
                if (mach, facula) == (1, 1):
                    found = True
                    return str(node_depth)
                else:
                    if node_depth < depth_limit:
                        node_depth += 1

                        pushed_nodes = 0

                        # generate left child
                        if mach-facula >= 1:
                            pushed_nodes += 1
                            node_to_push = ((mach-facula, facula), node_depth)
                            #frontier_stack.append(node_to_push)
                            if node_depth == depth_limit:
                                first_encounters.append(node_to_push)

                        # generate right child
                        if facula-mach >= 1:
                            pushed_nodes += 1
                            node_to_push = ((mach, facula-mach), node_depth)
                            #frontier_stack.append(node_to_push)
                            if node_depth == depth_limit:
                                first_encounters.append(node_to_push)
            #previous_first_encounters = copy.deepcopy(first_encounters)
            out_of_range = long(0)
            for node in first_encounters:
                mach = long(node[0][0])
                facula = long(node[0][1])
                if mach < 1 and facula < 1:
                    out_of_range += 1
            if out_of_range == long(len(first_encounters)):
                failed = True
            #first_encounters = []
        depth_limit += 1
    return "impossible"

print('4, 7...')
print(solution('4', '7'))
time.sleep(2)
print('2, 1...')
print(solution('2', '1'))
time.sleep(2)
print('2, 4...')
print(solution('2', '4'))
time.sleep(2)
print('10, 12...')
print(solution('10', '12'))
time.sleep(2)
print('10, 11...')
print(solution('10', '11'))
time.sleep(2)
print('13, 21...')
print(solution('13', '21'))
time.sleep(2)
print('123, 456...')
print(solution('123', '456'))
time.sleep(2)
print('1234, 567...')
print(solution('1234', '567'))
print('1234, 5678...')
print(solution('1234', '5678'))
time.sleep(2)
print('10000, 10000')
print(solution('10000', '10000'))
time.sleep(2)
print('10000, 9999')
print(solution('10000', '9999'))
time.sleep(2)
print('10**5, (10**5)-1')
print(solution(str(10**5), str((10**5-1))))
time.sleep(2)
print('10**50, (10**50)-1')
print(solution(str(10**50), str((10**50)-1)))
time.sleep(2)
print('10**50, 10**5')
print(solution(str(10**50), str(10**5)))
