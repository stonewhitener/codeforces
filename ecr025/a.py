n = int(input())
s = input()

count = 0

for c in s:
  if c == '1':
    count += 1
  else:
    print(count, end='')
    count = 0

print(count)
