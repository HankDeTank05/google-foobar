"""Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2
<= b <= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above
starting with n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212
would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1. """

"""
-- Python cases --
Input:
solution.solution('1211', 10)
Output:
    1

Input:
solution.solution('210022', 3)
Output:
    3
"""


def solution(n, b):
    # sequence = a list to keep track of every calculated value
    # this will be checked every run of the main loop (S2 -> S3 -> S4) to see if we are re-encountering any numbers
    sequence = [n]
    # print(len(sequence))
    # print(sequence)

    # this will be the index that gets incremented when verifying that we have, indeed, reached the end of the
    # third occurrence of the end_cycle
    end_cycle_check = 0

    # end_cycle = a list containing every value already encountered in the 'sequence' list
    # if a number is encountered for a third time (aka, you've encountered it once in 'sequence' and once in
    # 'end_cycle'), break out of the loop, and return len(end_cycle)
    end_cycle = []

    '''STEP 1 - Start with random minion ID n which is a nonnegative int of length k in base b'''

    # n = string representation of a number in base b
    # b = the base of number n

    # length of number n
    k = len(n)

    while True:
        # print('loop run: {}'.format(len(sequence)))
        #print('PRE STEP 2 - n = {}'.format(n))
        '''STEP 2 - Define x and y as integers of length k'''
        # x_lst = a list containing the digits of n in descending (big-->small) order
        # y_lst = a list containing the digits of n in ascending (small-->big) order
        # print('n = {}'.format(n))
        x_lst = []
        for d in range(k):
            x_lst.append(int(n[d]))
        x_lst = sorted(x_lst, reverse=True)
        y_lst = sorted(x_lst)

        # print('x_lst = {}'.format(x_lst))
        # print('y_lst = {}'.format(y_lst))

        # x_int = an integer representation of x_lst
        # y_int = an integer representation of y_lst
        '''NOTE: these begin as strings so we can easily add the digits in the following loop'''
        x_int = ''
        y_int = ''

        for d in range(len(x_lst)):
            x_int += str(x_lst[d])
            y_int += str(y_lst[d])

        # convert ?_int to an integer of the proper base
        x_int = int(x_int, base=b)
        y_int = int(y_int, base=b)

        #print('PRE STEP 3')
        #print('x_int = {}'.format(x_int))
        #print('y_int = {}'.format(y_int))

        '''STEP 3 - Define z = x - y. Add leading zero's to z to maintain length k if necessary'''

        z_int = x_int - y_int

        # if numbers are not in base 10, must convert from base 10 back to base b
        z_str = str(z_int)
        if b != 10:
            z_str = ''
            # rems = a list of remainders when repeatedly saving the remainder of z_int/b
            rems = []
            # repeatedly divide z_int by b, saving the remainders each time
            # (to form the number in base b from base 10)
            while z_int > 0:
                rem = z_int % b
                rems.append(rem)
                z_int //= b
                # print(rems)
            for d in range(len(rems)):
                digit = str(rems.pop())
                # print(digit)
                z_str += str(digit)
                # print(z_str)

        # print('z_int = {}'.format(z_int))

        # add leading zero's to z to maintain length k if necessary
        # z_str = str(z_int)
        while len(z_str) != k:
            z_str = '0' + z_str

        #print('PRE STEP 4 - z_str = {}'.format(z_str))
        #print('z_str is {}'.format(int(z_str, base=b) == x_int-y_int))
        #print()

        '''STEP 4 - Set n = z to get the next minion ID. Return to step 2'''
        n = z_str

        # check if the new n has been encountered once before
        if n not in sequence:
            # print('NEW ENCOUNTER: {}'.format(n))
            # if it hasn't been encountered before, append it to sequence
            sequence.append(n)
        elif n in sequence and n not in end_cycle:
            # print('SECOND ENCOUNTER: {}'.format(n))
            # if it has been encountered once before, append it to end_cycle
            end_cycle.append(n)
        elif n in sequence and n in end_cycle:
            # print('THIRD ENCOUNTER: {}\n***BREAKING LOOP***'.format(n))
            # if it has been encountered twice before, you're about to enter
            # the second repetition (aka the third occurrence) of the end cycle, so break out of the main loop
            if n == end_cycle[end_cycle_check]:
                end_cycle_check += 1
                if end_cycle_check >= len(end_cycle):
                    break
            else:
                end_cycle_check = 0
                end_cycle = []

    # return the length of the ending cycle of the algorithm (starting with n)
    return len(end_cycle)


'''if __name__ == "__main__":
    testmap = {
        'base3': [7789235, 112122201211012],
        '2base3': [814965465, 2002210111112110010],
        'base4': [7789235, 131231222303],
        '2base4': [814965465, 300210312023121],
        'base5': [7789235, 3443223420],
        '2base5': [814965465, 3132112343330],
        'base6': [7789235, 434541135],
        '2base6': [814965465, 212511312133],
        'base7': [7789235, 123131066],
        '2base7': [814965465, 26124043416],
        'base9': [7789235, 15581735],
        '2base9': [814965465, 2083445403]
    }
    for key in testmap.keys():
        b = int(key[-1])
        failed = False
        z_str = ''
        z_int = testmap[key][0]
        # rems = a list of remainders when repeatedly saving the remainder of z_int/b
        rems = []
        # repeatedly divide z_int by b, saving the remainders each time
        # (to form the number in base b from base 10)
        while z_int > 0:
            rem = z_int % b
            rems.append(rem)
            z_int //= b
            # print(rems)
        for d in range(len(rems)):
            digit = str(rems.pop())
            # print(digit)
            z_str += str(digit)
            # print(z_str)
        if z_str != testmap[key][1]:
            failed = True
        #print('{} test {}'.format(key, failed))'''

print(solution('1211', 10))
print(solution('210022', 3))
