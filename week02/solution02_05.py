x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

#if (x1 - x2)**2 <= 1 and (y1 - y2)**2 <= 1:
if 0 <= abs(x1 - x2) <= 1 and 0 <= abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")
