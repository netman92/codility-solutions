def solution(X, Y, D):
    distance = Y - X

    if distance % D == 0:
        return int(distance/D)
    else:
        return int(distance/D + 1)


def test():
    assert solution(10, 85, 30) == 3
    assert solution(10, 10, 30) == 0
    assert solution(10, 11, 30) == 1
    assert solution(10, 10001, 10) == 1000

if __name__ == "__main__":
    test()