def solution(A):
    A.sort()

    for i in xrange(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0


def test():
    assert solution([10,2,5,1,8,20]) == 1
    assert solution([10,50,5,1]) == 0
    #https://codility.com/demo/results/demo59AWXX-M5P/

if __name__ == "__main__":
    test()