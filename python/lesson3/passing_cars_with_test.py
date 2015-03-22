def solution(A):
    west = 0
    passing = 0
    for index in range(len(A)-1, -1, -1):
        if A[index] == 0:
            passing += west
            if passing > 1000000000:
                return -1
        else:
            west += 1
    return passing


def test():
    assert solution([0, 1, 0, 1, 1]) == 5
    #https://codility.com/demo/results/demoVAF87J-25B/


if __name__ == "__main__":
    test()