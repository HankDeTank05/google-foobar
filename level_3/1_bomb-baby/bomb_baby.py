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

def solution(m, f):
    tm, tf = int(m), int(f)
    queue = []
    node = [(1, 1), 0]
    while True:

        print(node[0], node[1])

        mach = node[0][0]
        facula = node[0][1]
        level = node[1]

        found = (mach == tm and facula == tf)
        found_mirror = (mach == tf and facula == tm)
        if found or found_mirror:
            return str(level)

        level += 1

        # enqueue node's left child
        queue.append([(mach + facula, facula), level])

        # enqueue node's right child
        queue.append([(mach, facula + mach), level])

        # dequeue a node from the queue
        if len(queue) > 0:
            node = queue.pop(0)
        elif level > max(tm, tf):
            break

    return "impossible"

print(solution('4', '7'))
print(solution('2', '1'))
print(solution('10', '11'))
print(solution('13', '21'))




if __name__ == "__main__":
    tests = {
        'case1': ('4', '7', 4),
        'case2': ('2', '1', 1)
    }
    for test_case in tests.keys():
        soln = solution(tests[test_case][0], tests[test_case][1])
        print(soln == tests[test_case][2])
    print(solution('4', '7'))
    print(solution('2', '1'))
