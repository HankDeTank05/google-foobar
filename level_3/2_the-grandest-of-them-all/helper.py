import itertools
import csv
import time

def max_steps(bricks):
    steps = 0
    step_number = 1
    bricks_remaining = bricks
    bricks_remaining -= step_number
    while bricks_remaining >= 0:
        steps += 1
        step_number += 1
        bricks_remaining -= step_number
    return steps

def combos_to_csv(n):
    num_steps = 2
    max_steps_possible = max_steps(n)
    usable_nums = []
    combos = []
    for i in range(1, n+1):
        usable_nums.append(i)

    while num_steps <= max_steps_possible:
        combos_iter = itertools.combinations(usable_nums, num_steps)
        while True:
            try:
                combo = combos_iter.next()
            except StopIteration:
                break
            valid_combo = True
            for i in range(len(combo)-1):
                if combo[i] >= combo[i+1]:
                    valid_combo = False
            if sum(combo) == n and valid_combo:
                print(combo)
                combos.append(combo)
        num_steps += 1

    with open('combos_{}.csv'.format(n), mode='w') as csvfile:
        csvfile = csv.writer(csvfile)

        for row in combos:
            csvfile.writerow(row)

if __name__ == "__main__":
    for i in range(26, 50):
        print('Calculating combos for n = {}'.format(i))
        combos_to_csv(i)
