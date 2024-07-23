nums = [54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57, 235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288]

s = []
for num in nums:
    s.append(num % 37)

print(s)

alph = 'abcdefghijklmnopqrstuvwxyz'
n = '0123456789'

ans = ""

for num in s:
    if num < 26:
        ans += alph[num]
    elif num > 25 and num < 36:
        ans += n[num - 26]
    else:
        ans += '_'

print(ans)