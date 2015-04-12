def solution(A):
    nums = dict()
    for num in A:
        try:
            nums[str(num)] += 1
        except:
            nums[str(num)] = 1
    return len(nums)

def test():
    assert solution([2,2,1,1,3,1]) == 3
    #https://codility.com/demo/results/demoSW4ETB-7EZ/

if __name__ == "__main__":
    test()