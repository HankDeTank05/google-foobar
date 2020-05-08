"""
THIS IS MEANT TO BE THE REVERSE OF bomb_baby.py's SOLUTION
instead of starting from 1,1 and searching downwards, start from tm, tf and work backwards towards 1,1
If 1,1 is reachable, return the shortest number of moves to get there
If 1,1 is NOT reachable, return "impossible"
"""
import copy
import time
#import numpy as np
import logging
logging.basicConfig(filename='bomb_baby_reverse_log', level=logging.DEBUG)


def solution(m, f):
    tm = long(m)
    tf = long(f)

    '''# if one of the targets (m or f) is greater than the other by one, it exists.
    # it exists in the tree at the level of the smaller target value
    if tm == tf - 1 or tf == tm - 1:
        return str(min(tm, tf))

    # otherwise, if both values are 1, it exists at 0 depth of the tree
    elif tm == tf and tf == 1:
        return str(0)

    # otherwise, if one of the values equal to half of the other, it will not exist in the tree
    elif tm == tf / 2 or tf == tm / 2:
        return "impossible"

    # otherwise if one of the values is 1, and the other is any number greater than it, it exists
    # at depth level of (larger value)-1
    elif min(tm, tf) == 1 and max(tm, tf) > 1:
        return str(max(tm, tf) - 1)'''

    # the initial depth limit of the IDDFS is 0
    depth_limit = 0

    # the root of the tree to be generated in the search is the target value pair (depth=0)
    root = ((tm, tf), 0)

    # initialize the "failed" boolean flag to False
    failed = False

    '''BEGIN ITERATIVE-DEEPENING DEPTH-FIRST SEARCH'''
    # this list will be used to store the unique values at the maximum depth level of a given
    # depth-limited DFS
    first_encounters = []

    while not failed:
        # print()
        # print('depth_limit = {}'.format(depth_limit))
        # time.sleep(2)

        '''BEGIN DEPTH-BOUNDED DEPTH-FIRST SEARCH'''
        # perform a depth-bounded search
        if depth_limit == 0:
            # if depth limit is zero, check if the input == 1,1
            if (1, 1) == root[0]:
                # if the input == 1,1 return 0 as the depth
                return root[1]
        else:
            if depth_limit == 1:
                # if the depth limit is 1, set the first_encounters list to contain only the root
                first_encounters = [root]

            # the previous_first_encounters list keeps track of all of the newly encountered sets from the last
            # iteration of the loop, which will be used (in the following loop) to calculate the values in the next
            # depth layer of the tree
            previous_first_encounters = copy.deepcopy(first_encounters)

            # empty out first_encounters in preparation for beginning to search a new depth layer
            first_encounters = []

            # use the newly encountered values from the previous depth layer to generate the values in this current
            # depth layer

            # while there are still values left to process, do the following for each...
            while len(previous_first_encounters) > 0:

                # remove a tree node from the stack, to be processed
                node = previous_first_encounters.pop()

                # assign the values to their own variables for easy access later
                mach = long(node[0][0])
                facula = long(node[0][1])

                # assign the depth value to its own variable, for easy access later
                node_depth = node[1]

                '''DETERMINE WHETHER OR NOT A NODE IS THE GOAL NODE'''
                # the goal node is (1,1)
                if (mach, facula) == (1, 1):
                    # if this node is the goal node, return the depth at which it was found within the tree as a string
                    return str(node_depth)
                else:
                    # if this is not the goal node, do the following...

                    # if the node is not at the deepest point allowed in the search...
                    if node_depth < depth_limit:
                        # increment the node_depth
                        # this variable now represents the depth of the soon-to-be-generated child nodes
                        node_depth += 1

                        # keep track of how many of the child nodes will be pushed to the stack
                        # (0 <= pushed_nodes <= 2)
                        pushed_nodes = 0

                        '''LEFT CHILD NODE'''
                        # if the left child's smallest value will be >= 1  (if the child node's values are valid) AND...
                        # if the depth of the left child is equal to the depth_limit (if the node is in the newest,
                        # and therefore un-explored depth layer)...
                        if mach - facula >= 1 and node_depth == depth_limit:
                            # generate the left child node
                            node_to_push = ((mach - facula, facula), node_depth)

                            # push the left child node to the stack of newly encountered nodes
                            first_encounters.append(node_to_push)

                            # increment the pushed_nodes counter by one, because a node was pushed to the stack
                            pushed_nodes += 1

                            # delete the node_to_push to save on memory
                            del node_to_push

                        '''RIGHT CHILD NODE'''
                        # if the right child's smallest value will be >= 1  (if the child node's values are valid) AND...
                        # if the depth of the right child is equal to the depth_limit (if the node is in the newest,
                        # and therefore un-explored depth layer)...
                        if facula - mach >= 1 and node_depth == depth_limit:
                            # generate the right child node
                            node_to_push = ((mach, facula - mach), node_depth)

                            # push the right child node to the stack of newly encountered nodes
                            first_encounters.append(node_to_push)

                            # increment the pushed_nodes counter by one, because a node was pushed to the stack
                            pushed_nodes += 1

                            # delete the node_to_push to save on memory
                            del node_to_push

                # if there were no VALID newly encountered nodes, stop searching.
            if len(first_encounters) == 0:
                failed = True
        '''END DEPTH-BOUNDED SEARCH'''

        depth_limit += 1
    return "impossible"

def solution2(M, F):
    def trace_backwards(mach, facula, depth):
        print(mach, facula)
        if mach == 1 and facula > 1:
            return str(depth + facula - 1)
        elif mach > 1 and facula == 1:
            return str(depth + mach - 1)
        elif mach == 1 and facula == 1:
            return str(depth)
        elif mach == facula or max(mach, facula) % min(mach, facula) == 0:
            return 'impossible'
        else:
            if mach > facula:
                goes_into_times = mach//facula
                return trace_backwards(mach-facula*goes_into_times, facula, depth+goes_into_times)
            elif facula > mach:
                goes_into_times = facula//mach
                return trace_backwards(mach, facula-mach*goes_into_times, depth+goes_into_times)

    tm, tf = long(M), long(F)
    return trace_backwards(tm, tf, 0)

print(solution2('8', '3'))


'''print('4, 7...')
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
print(solution(str(10 ** 5), str((10 ** 5 - 1))))
time.sleep(2)
print('10**50, (10**50)-1')
print(solution(str(10 ** 50), str((10 ** 50) - 1)))
time.sleep(2)
print('10**50, 10**5')
print(solution(str(10 ** 50), str(10 ** 5)))'''
