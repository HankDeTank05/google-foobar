def solution(n):
    def max_steps(num_bricks):
        bricks_remaining = num_bricks
        num_steps = 0
        step_num = 1
        bricks_remaining -= step_num
        while bricks_remaining >= 0:
            num_steps += 1
            step_num += 1
            bricks_remaining -= step_num

        return num_steps

    count = 0

    return max_steps(n)

print(solution(20))