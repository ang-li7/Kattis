
turns = {
    '/':{
        'U':'R',
        'D':'L',
        'R':'U',
        'L':'D'
    },
    '\\':{
        'U':'L',
        'D':'R',
        'R':'D',
        'L':'U'
    }
}

z = 1
x = input()
while (x != "0 0"):
    xx = x.split(" ")
    w = int(xx[0])
    h = int(xx[1])
    a = []
    r = -1
    c = -1
    for i in range(0, h):
        row = input()
        a.append(row)
    for i in range(0, h):
        for n in range(0, w):
            if a[i][n] == '*':
                r = int(i)
                c = int(n)
    direction = 'X'
    if r == 0:
        direction = 'D'
        r = r+1
    elif r == h-1:
        direction = 'U'
        r= r-1
    elif c == 0:
        direction = 'R'
        c = c+1
    else:
        direction = 'L'
        c = c-1
    while a[r][c] != 'x':
        if direction == 'U':
            r = r - 1
        elif direction == 'D':
            r = r + 1
        elif direction == 'R':
            c = c + 1
        else:
            c = c - 1
        if a[r][c] in turns:
            direction = turns[a[r][c]][direction]
    print("HOUSE "+str(z))
    z = z+1
    for i in range (0, h):
        for j in range (0, w):
            if i == r and j == c:
                print('&', end='')
            else:
                print(a[i][j], end='')
        print()
    x = input()
