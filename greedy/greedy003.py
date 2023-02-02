# 숫자 카드 게임
# 여러 개의 숫자 카드 중  가장 높은 숫자가 쓰인 카드 한 장 뽑기
# N x M

n, m = map(int, input("N x M: ").split())

def ChoiceCard(n, m):
    cardList = [[0] * n for _ in range(m)]

    for i in range(n):
        cardList[i] = map(int, input().split())

    result = -1
    for i in range(n):
        temp = list(cardList[i])
        temp.sort()
        if (result <= temp[0]):
            result = temp[0]
    return result

def ChoiceCard2(n, m):
    result = 0
    for _ in range(n):
        data = list(map(int, input().split()))
        minVar = min(data)
        result = max(result, minVar)
    return result

def ChoiceCard3(n, m):
    result = 0
    
    for _ in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)
    
    return result
    
result = ChoiceCard3(n, m)

print("result: " + str(result))
