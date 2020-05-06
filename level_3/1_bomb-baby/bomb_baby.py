"""
example:
3m, 2f
    product a: 3m, 5f
    OR
    product b: 5m, 2f

IN       OUT
3m, 2f = 3m, 5f
3m, 2f = 5m, 2f


SEQUENCE
n0 = am, bf
n1 = OPTION 1: (a+b)m, bf
     OPTION 2: am, (a+b)f
"""

import time
import timeit
"""breadth first search method"""
'''def solution(m, f):
    tm, tf = int(m), int(f)
    queue = []
    node = ((1, 1), 0)
    deepest = 0
    level_start_time = 0
    search_start_time = timeit.default_timer()
    while True:

        #print(node[0], node[1])

        mach = node[0][0]
        facula = node[0][1]
        level = node[1]

        if (mach == tm and facula == tf) or (mach == tf and facula == tm):
            #print(node[0], node[1])
            time_amt = timeit.default_timer() - search_start_time
            if time_amt > 60:
                time_amt /= 60
                time_unit = 'minutes'
            else:
                time_unit = 'seconds'
            #print('total search time: {} {}'.format(time_amt, time_unit))
            return str(level)

        level += 1

        m_new = mach+facula
        # enqueue node's left child
        if mach <= tm and facula <= tf and m_new <= max(tm, tf) and facula <= min(tf, tm):
            queue.append(((m_new, facula), level))
            if level > deepest:
                level_end_time = timeit.default_timer() - level_start_time
                #print('took {} seconds to search level {}'.format(level_end_time, deepest))
                deepest = level
                #print('reached depth {}'.format(deepest))
                level_start_time = timeit.default_timer()

        f_new = facula+mach
        # enqueue node's right child
        if level != 0 and mach <= tm and facula <= tf and f_new <= max(tm, tf) and mach <= min(tm, tf):
            queue.append(((mach, f_new), level))
            if level > deepest:
                level_end_time = timeit.default_timer() - level_start_time
                #print('took {} seconds to search level {}'.format(level_end_time, deepest))
                deepest = level
                #print('reached depth {}'.format(deepest))
                level_start_time = timeit.default_timer()

        # dequeue a node from the queue
        if level > max(tm, tf) or len(queue) == 0:
            break
        else:
            del node
            node = queue.pop(0)

    time_amt = timeit.default_timer() - search_start_time
    if time_amt > 60:
        time_amt /= 60
        time_unit = 'minutes'
    else:
        time_unit = 'seconds'
    #print('total search time: {} {}'.format(time_amt, time_unit))
    return "impossible"'''

def solution(m, f):
    tm = int(m)
    tf = int(f)
    depth_limit = 0
    root = ((1, 1), 0)
    found = False
    failed = False
    repeat_comparison = None
    # perform iterative depth search
    while not failed:
        #print()
        print('depth_limit = {}'.format(depth_limit))
        #time.sleep(2)
        # perform a depth-bounded search
        if depth_limit == 0:
            if (tm, tf) == root[0]:
                return root[1]
        else:
            depth = 0
            frontier_stack = [root]
            first_encounters = []

            while len(frontier_stack) > 0:
                #time.sleep(1)
                #print('stack size: {}'.format(len(frontier_stack)))
                # remove node from the stack
                node = frontier_stack.pop()

                # make sure we aren't infinitely repeating ourselves
                #if repeat_comparison is not None and node == repeat_comparison:
                    #print('REPEAT FOUND')
                    #break

                mach = node[0][0]
                facula = node[0][1]

                node_depth = node[1]
                #print('node {}'.format(node))
                # determine if node is the goal or not
                if (mach, facula) == (tm, tf):
                    found = True
                    return str(node_depth)
                else:
                    if node_depth < depth_limit:
                        node_depth += 1

                        pushed_nodes = 0

                        # generate left child
                        if mach+facula <= tm:
                            pushed_nodes += 1
                            node_to_push = ((mach+facula, facula), node_depth)
                            frontier_stack.append(node_to_push)
                            if node_depth == depth_limit:
                                first_encounters.append(node_to_push)

                        # generate right child
                        if mach+facula <= tf:
                            pushed_nodes += 1
                            node_to_push = ((mach, facula+mach), node_depth)
                            frontier_stack.append(node_to_push)
                            if node_depth == depth_limit:
                                first_encounters.append(node_to_push)
            out_of_range = 0
            for node in first_encounters:
                mach = node[0][0]
                facula = node[0][1]
                if mach > tm and facula > tf:
                    out_of_range += 1
            if out_of_range == len(first_encounters):
                failed = True
        depth_limit += 1
    return "impossible"


print('4, 7...')
print(solution('4', '7'))
time.sleep(2)
print('Resuming...')
print('2, 1...')
print(solution('2', '1'))
time.sleep(2)
print('Resuming...')
print('2, 4...')
print(solution('2', '4'))
time.sleep(2)
print('Resuming...')
print('10, 12...')
print(solution('10', '12'))
time.sleep(2)
print('Resuming...')
print('10, 11...')
print(solution('10', '11'))
time.sleep(2)
print('Resuming...')
print('13, 21...')
print(solution('13', '21'))
time.sleep(2)
print('Resuming...')
print('123, 456...')
print(solution('123', '456'))
time.sleep(2)
print('Resuming...')
print('1234, 567...')
print(solution('1234', '567'))
time.sleep(2)
print('Resuming...')
print('1234, 5678...')
print(solution('1234', '5678'))
time.sleep(2)
print('Resuming...')
#print(solution('10000', '10000'))
#print(solution(str(10**5), str((10**5-1))))


if __name__ == "__main__":
    tests = {
        'case1': ('4', '7', '4'),
        'case2': ('2', '1', '1')
    }
    for test_case in tests.keys():
        soln = solution(tests[test_case][0], tests[test_case][1])
        #print(soln == tests[test_case][2])
    #print(solution('4', '7'))
    #print(solution('2', '1'))'''
