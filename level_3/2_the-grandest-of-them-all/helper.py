import itertools
import csv
import time
import pickle


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
    for i in range(1, n + 1):
        usable_nums.append(i)

    while num_steps <= max_steps_possible:
        combos_iter = itertools.combinations(usable_nums, num_steps)
        while True:
            try:
                combo = combos_iter.next()
            except StopIteration:
                break
            valid_combo = True
            for i in range(len(combo) - 1):
                if combo[i] >= combo[i + 1]:
                    valid_combo = False
            if sum(combo) == n and valid_combo:
                print(combo)
                combos.append(combo)
        num_steps += 1
    with open('combos_{}.csv'.format(n), mode='w') as csvfile:
        csvfile = csv.writer(csvfile)

        for row in combos:
            csvfile.writerow(row)


def combo_counts_to_csv(n_start, n_stop):
    n = n_start
    combo_counts = [['n', 'num steps', 'num combos with num steps']]
    count_index = 1
    while n < n_stop:
        num_steps = 2
        max_steps_possible = max_steps(n)
        usable_nums = []
        for i in range(1, n + 1):
            usable_nums.append(i)
        while num_steps <= max_steps_possible:
            combos_iter = itertools.combinations(usable_nums, num_steps)
            combo_counts.append([n, num_steps, 0])
            while True:
                try:
                    combo = combos_iter.next()
                except StopIteration:
                    break
                valid_combo = True
                for i in range(len(combo) - 1):
                    if combo[i] >= combo[i + 1]:
                        valid_combo = False
                if sum(combo) == n and valid_combo:
                    combo_counts[count_index][2] += 1
            count_index += 1
            num_steps += 1
        print('done calculating n={}'.format(n))
        n += 1
    with open('combo_count_data.csv'.format(n), mode='a') as csvfile:
        csvfile = csv.writer(csvfile)

        for row in combo_counts:
            csvfile.writerow(row)

    print('Done')


if __name__ == "__main__":
    """for n in range(3, 10):
        print('Calculating combos for n = {}'.format(n))
        combos_to_csv(n)"""
    combo_counts_to_csv(3, 45)
