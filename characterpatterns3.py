cases = int(input())
out = ''
WIDTH = 2
HEIGHT = 2

def printast():
    out = ''
    global WIDTH
    for _ in range(columns):
        out = out + ('*' * (WIDTH + 1))
    out = out + '*\n'
    return out

def printrow():
    out = ''
    out = out + '*'
    for _ in range(columns):
        out = out + '..*'
    out = out + '\n'
    return out

for _ in range(cases):
    lines, columns = [int(x) for x in input().split(' ')]
    out = out + printast()
    for _ in range(lines):
        for _ in range(HEIGHT):
            out = out + printrow()
        out = out + printast()
    out = out + '\n'
print(out, end='')
