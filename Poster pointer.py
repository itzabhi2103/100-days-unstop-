def can_print(n, s):
  segment = ""
  for ch in s:
    if ch=='W':
      if segment:
        if len(segment)==1 or len(set(segment))==1:
          return "NO"
      segment = ""
    else:
      segment+=ch
  if segment:
    if len(segment)==1 or len(set(segment))==1:
      return 'NO'
  return 'YES'
t = int(input())
for _ in range(t):
  n = int(input())
  s = input().strip()
  print(can_print(n, s))
