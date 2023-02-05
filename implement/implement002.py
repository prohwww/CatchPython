# 시각 
# 00:00:00 부터 N:59:59 까지 3이 들어가는 모든 경우의 수 찾기

n = int(input("시각: "))

def GetTime(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                time = str(i) + str(j) + str(k)
                if time.find("3") >= 0:
                    count += 1
    return count;

def GetTime2(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count

result = GetTime2(n)
print("result: " + str(result))