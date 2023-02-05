# 왕실의 나이트
# 8 x 8 체스판에서 왕은 'L'자 형태로 이동하는데 이동가능한 경우의 수
# 수평 2칸 + 수직 1칸 / 수직 2칸 + 수평 1칸

location = input("왕의 현재 위치: ")

def GetMethodCnt(location):
    # TODO
    count = 0;
    xl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = 0
    for i in range(xl):
        if xl[i] in location:
            x = i + 1

    while True:
        break

def GetMethodCnt2(location):
    row = int(location[1])
    column = int(ord(location[0])) - int(ord('a')) + 1
    
    steps = [(-2,-1), (-1,-2), (2,-1), (-2,1), (-1,2), (1,-2), (2,1), (1,2)]
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1
    
    return result

result = GetMethodCnt2(location)
print("rocation: " + str(result))