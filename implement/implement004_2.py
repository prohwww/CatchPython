# 게임 개발
n,m = map(int, input().split())
x,y,direction = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서
dx = [0,-1,1,0]
dy = [-1,0,0,1]

visit = [[0] * m for _ in range(n)]
visit[x][y] = 1
visit[x][y] = 1

def Turn_Left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

count = 1
turn_cnt = 1
while True:
    if turn_cnt < 4:
        Turn_Left()
        turn_cnt += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if visit[nx][ny] == 0 and array[nx][ny] == 0:
            visit[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_cnt = 0
            continue
        else:
            turn_cnt += 1 
            continue
    elif turn_cnt == 4:
        temp_direc = direction - 1
        if temp_direc < 0: temp_direc = 3
        nx = x - dx[temp_direc]
        ny = y - dy[temp_direc]
        if array[nx][ny] == 0:
            count += 1
            turn_cnt = 0
        else:
            break

print("count: " + str(count))