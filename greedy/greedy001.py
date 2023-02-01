# 거스름돈 주기
# 500, 100, 50, 10 가장 적은 동전 총 개수 구하기

def CalcCoinCount1(balance):
    count = 0
    
    if (balance >= 500):
        count = balance // 500
        balance = balance % 500
    if (balance >= 100):
        count = balance // 100
        balance = balance % 100
    if (balance >= 50):
        count = balance // 50
        balance = balance % 50
    if (balance >= 10):
        count = balance // 10
        balance = balance % 10
        
    return count

def CalcCoinCount2(balance):
    count = 0
    coin_arr = [500, 100, 50, 10]
    
    for coin in coin_arr:
        cnt += balance // coin
        balance = balance % coin
        
    return count

print("받아야 할 거스름돈을 입력하세요")
balance = int(input("거스름돈: "))

result = CalcCoinCount1(balance)
result2 = CalcCoinCount2(balance)

print("Coin Count: ", result2)