import unittest
import bomb_baby_reverse as bbr


class TestBBR(unittest.TestCase):

    def test_solution(self):
        for m in range(1, 101):
            for f in range(1, 101):
                print(bbr.solution(m, f))
        '''
        cases = [
            [4, 7, 4],
            [2, 1, 1],
            [2, 4, 'impossible'],
            [10**50, 1, 10**50-1],
            [10**50, 10**50-1, 10**50-1],
            [1, 1, 0]
        ]
        for case in cases:
            if len(case) == 3:
                # assign the values to variables
                m = case[0]  # number of mach bombs needed
                f = case[1]  # number of facula bombs needed
                ans = str(case[2])  # the expected outcome of bbr.solution(m, f)

                # make sure the actual outcome matches the expected outcome
                self.assertEqual(bbr.solution(m, f), ans)

                # if m and f are unique values, test the solution with mirrored input (f, m) instead of (m, f)
                if m != f:
                    self.assertEqual(bbr.solution(f, m), ans)'''


if __name__ == "__main__":
    unittest.main()
