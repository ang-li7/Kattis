class equation():
        b = "( 3 + ( 5 - 6 )"
        bb = b.split(" ")
        a = []
        math = 0
        for c in bb:
            if (c == '(') or (c == '['):
                a.append(c)
            elif c == ')' or c == ']':
                if c == ')' and a[-1] == '(':
                    a.pop(-1)
                elif c == ']' and a[-1] == '[':
                    a.pop(-1)
                else:
                    math = 1
        if len(a) is 0 and math is 0:
            print("yes")
        else:
            print("no")
