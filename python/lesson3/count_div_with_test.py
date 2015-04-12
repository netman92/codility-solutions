def solution(A, B, K):
    new_start = A
    if (A % K) != 0:
        new_start = ((A/K)+1) * K
    new_end = B - (B % K)
    diff = new_end - new_start
    return (diff/K) + 1


def test():
    assert solution(6,11,2) == 3
    #https://codility.com/demo/results/demoNW3MQS-SJG/


if __name__ == "__main__":
    test()