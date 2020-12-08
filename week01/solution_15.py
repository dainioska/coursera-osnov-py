a = int(input())
h = a // 3600 % 24
m = a // 60 % 60
s = a % 60
print('{0:d}:{1:02d}:{2:02d}'.format(h, m, s))
print()
