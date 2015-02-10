def solution(A):
    length = len(A)
    first_part = A[0]
    second_part = sum(A[1:])

    min_solution = abs(first_part - second_part)

    for i in range(1, length-1):
        first_part = first_part + A[i]
        second_part = second_part - A[i]
        difference = abs(first_part-second_part)

        if difference < min_solution:
            min_solution = difference

    return min_solution


def test():
    assert solution([3, 1, 2, 4, 3]) == 1

if __name__ == "__main__":
    test()