from collections import deque


def solution(M, F):
    goal_m, goal_f = int(M), int(F)
    queue = deque([(goal_m, goal_f)])

    generation_num = 0

    while queue:
        # First element in queue
        m, f = queue[0]

        if (m, f) == (1, 1):
            return str(generation_num)

        else:
            """
            If there is a large difference between m and f, our code is too inefficient. Let's find
            the largest multiple (k) of the difference to subtract in one go.
            """

            difference = abs(m-f)
            valid_x = lambda x: True if x > 0 else False
            n = 1

            if f > m:
                x = difference // m
                if valid_x(x):
                    n = x
                    queue.append((m, f-(n*m)))
                else:
                    queue.append((m, difference))

            elif m > f:
                x = difference // f
                if valid_x(x):
                    n = x
                    queue.append((m-(n*f), f))
                else:
                    queue.append((difference, f))

            elif m == f:
                return "impossible"

            generation_num += n
            queue.popleft()

    return "impossible"