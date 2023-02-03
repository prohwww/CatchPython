# 1이 될 때 까지
# N이 1이 될 때까지 1을 빼거나 K로 나누기 선택하는 최소 횟수

n, k = map(int, input("Input N K: ").split())

def CountToOne(n, k):
    result = 0
    while(n > 1):
        if (n % k == 0):
            n /= k
            result += 1
        else:
            n -= 1
            result += 1
    return result

def CountToOne2(n, k):
    result = 0
    
    while n > k:
        while n % k != 0:
            n -= 1
            result += 1
        n /= k
        result += 1

    while n > 1:
        n -= 1
        result += 1
            
    return result


result = CountToOne2(n,k)
print("result: " + str(result))