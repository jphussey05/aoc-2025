FILEPATH = 'day1.txt'

with open(FILEPATH) as fin:
    contents = [line.strip() for line in fin]

pos = 50
cnt = 0

for rot in contents:
    change = int(rot[1:])

    if rot[0] == 'L':
        change = 100 - (change % 100)

    pos = (pos + change) % 100
    if pos == 0:
        cnt += 1

print(cnt)
