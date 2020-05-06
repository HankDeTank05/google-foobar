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

def solution(x, y):
    class Node:
        def __init__(self, mach: int, facula: int, dna='r', visited=False, left=None, right=None):
            self.mach = mach
            self.facula = facula
            self.dna = dna
            self.visited = visited
            self.left = left
            self.right = right

        def __str__(self):
            return '({}m, {}f) at {}'.format(self.mach, self.facula, self.dna)

        def generate_left_child(self):
            # left increases mach
            self.left = Node(self.mach + self.facula, self.facula, dna=self.dna + 'L')

        def generate_right_child(self):
            # right increases facula
            self.right = Node(self.mach, self.facula + self.mach, dna=self.dna + 'R')

        def generate_children(self):
            """generate the two possible versions of the next generation"""
            self.generate_left_child()
            self.generate_right_child()

        def bfs(self, tm, tf):
            if tm == 1 and tf == 1:
                return 0
            else:
                depth = 1
                self.generate_left_child()
                current_node = self.left
                while True:
                    cm = current_node.mach
                    cf = current_node.facula
                    sum = cm+cf
                    if sum < max(tm, tf):
                        current_node.generate_children()
                    else:
                        break

        def populate_subtree_in_range(self, tm, tf):
            answer = None
            sum = self.mach + self.facula
            if sum <= max(tm, tf):
                if sum == max(tm, tf):
                    self.generate_children()
                    #print('{}\'s sum == max(tm, tf)'.format(self.dna))
                    self.generate_children()
                    target = None
                    actual = None
                    tv = None
                    av = None
                    if tm == self.mach:
                        target = 'tm'
                        actual = 'self.mach'
                        tv = tm
                        av = self.mach
                        answer = self.right
                    elif tm == self.facula:
                        target = 'tm'
                        actual = 'self.facula'
                        tv = tm
                        av = self.facula
                        answer = self.left
                        #return self.left
                    elif tf == self.mach:
                        target = 'tf'
                        actual = 'self.mach'
                        tv = tf
                        av = self.mach
                        answer = self.left
                    elif tf == self.facula:
                        target = 'tf'
                        actual = 'self.facula'
                        tv = tf
                        av = self.facula
                        answer = self.right
                    if answer is not None:
                        #print('ANSWER? {}'.format(answer))
                        if min(answer.mach, answer.facula) == min(tm, tf) and max(answer.mach, answer.facula) == max(tm, tf):
                            #print('I think this is the answer: {}'.format(answer))
                            return answer
                    #print('{}:{} == {}:{}'.format(target, tv, actual, av))

                self.generate_children()
                if answer is None:
                    answer = self.left.populate_subtree_in_range(tm, tf)
                if answer is None:
                    answer = self.right.populate_subtree_in_range(tm, tf)
            elif sum == sum + min(tm, tf):
                #print('possible with min(tm, tf) at {}'.format(self.dna))
                pass
            elif sum == sum + max(tm, tf):
                #print('possible with max(tm, tf) at {}'.format(self.dna))
                pass
            return answer

        def recursive_print(self):
            #print(self)
            if self.left is not None:
                self.left.recursive_print()
            if self.right is not None:
                self.right.recursive_print()

            return

    root = Node(1, 1)
    root.generate_left_child()

    start = root.left
    node = start.populate_subtree_in_range(int(x), int(y))
    start.recursive_print()
    depth = len(node.dna)-1

    return depth




if __name__ == "__main__":
    tests = {
        'case1': ('4', '7', 4),
        'case2': ('2', '1', 1)
    }
    for test_case in tests.keys():
        soln = solution(tests[test_case][0], tests[test_case][1])
        print(soln == tests[test_case][2])
    #print(solution('4', '7'))
    #print(solution('2', '1'))
