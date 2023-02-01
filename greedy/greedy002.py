# 큰 수의 법칙
# 주어진 수를 M번 더하고 연속횟수 K번 제한을 따라 만들 수 있는 가장 큰 수 구하기

n, m, k = map(int, input("n m k: ").split()) # 2 <= N <= 1000, 1 <= M <= 10000, 1 <= K <= 10000
data = list(map(int, input("n개의 숫자 입력: ").split())) # 1 <= n <= 10000

def CalcBigOne(n, m, k, data):
    data.sort(reverse=True)
    bigCnt = 0
    result = 0
    first = data[0]
    second = data[1]
    
    for i in range(0, m):
        if (bigCnt == k):
            result += second
            bigCnt = 0
            print(i, " result + second(", second, ") = ", result)
            continue;
        result += first
        bigCnt += 1
        print(i, " result + first(", first, ") = ", result, " [BigCnt: ", bigCnt)
        
    return result

def CalcBigOne2(n, m, k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    result = 0
    while True:
        for i in range(k):
            if (m == 0):
                break;
            result += first
            m -= 1
        if (m == 0):
            break
        result += second
        m -= 1
    return result

def CalcBigOne3(n, m, k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    
    count = int(m / (k + 1)) * k
    count += m % (k + 1)
    
    result = first * count
    result += second * (m - count)
    
    return result

result = CalcBigOne3(n, m, k, data)
print("Result: ", result)