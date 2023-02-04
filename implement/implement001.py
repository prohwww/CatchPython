# 구현문제 - 상하좌우
# N x N 크기, L,R,U,D 방향 계획서

n = int(input("정사각형의 크기: "))
# plan = list(map(str, input("계획서: ").split()))
plan = input("계획서: ").split()

def whereRU(n, plan):
    width = 1
    height = 1
    for direc in plan:
        direc.upper()
        if direc == "R":
            width = width + 1 if width + 1 <= n else width
        elif direc == "L":
            width = width - 1 if width - 1 > 0 else width
        elif direc == "U":
            height = height - 1 if height - 1 > 0 else height
        else:
            height = height + 1 if height + 1 <= n else height
        # print(direc + ": " + str(width) + ", " + str(height))

    print(height, width)

def whereRU2(n, plan):
    x, y = 1, 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_type = ['L', 'R', 'U', 'D']
    
    for direc in plan:
        for i in range(len(move_type)):
            if direc == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if (nx > n or nx < 1 or ny > n or nx < 1):
            continue
        x, y = nx, ny
    
    print(x, y)

whereRU2(n, plan)