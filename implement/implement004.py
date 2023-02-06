# 게임 개발

n, m = map(int, input("N x M: ").split())
x, y, direction = map(int, input().split())

map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

place = [[0] * m for _ in range(n)]
place[x][y] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_cnt = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if map_list[nx][ny] == 0 and place[nx][ny] == 0:
        place[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    
    if turn_cnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
            # count += 1
        else:
            break
        turn_cnt = 0

print("count = " + str(count))
                