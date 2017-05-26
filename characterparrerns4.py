def make_asterixes(columns, width):
    ret = ''
    ret = ret + '*'
    for _ in range(columns):
        ret = ret + ('*' * (width + 1))
    ret = ret + '\n'
    return ret

def make_col_line(columns, width):
    ret = '*'
    for _ in range(columns):
        ret = ret + '-' * width
        ret = ret + '*'
    return ret

def main():
    cases = int(input())
    out = ''
    for _ in range(cases):
        rows, columns, height, width = [int(x) for x in input().split(' ')]
        if not rows * columns * height * width:
            continue
        out = out + make_asterixes(columns, width)
        for _ in range(rows):
            for _ in range(height):
                out = out + make_col_line(columns, width) + '\n'
            out = out + make_asterixes(columns, width)
        if not _ == cases - 1:
            out = out + '\n'
    print(out, end='')

if __name__ == '__main__':
    main()
