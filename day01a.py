FILEPATH = 'day1.txt'

with open(FILEPATH) as fin:
    contents = [line.strip() for line in fin]

pos = 50
cnt = 0


for rot in contents:
    change = int(rot[1:])

    modifier = 1 if rot[0] == 'R' else -1
    for _ in range(change):
        pos += modifier
        if pos == 0:
            cnt += 1
        elif pos == -1:
            pos = 99
        elif pos == 100:
            cnt += 1
            pos = 0


print(cnt)
