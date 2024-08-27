
# 12分でクリア

s = input()

dream = "dream"
dreamer = "dreamer"
erase = "erase"
eraser = "eraser"

ans = ""
while True:

    if s[-len(eraser):] == eraser:
        s = s[:-len(eraser)]

    elif s[-len(erase):] == erase:
        s = s[:-len(erase)]

    elif s[-len(dreamer):] == dreamer:
        s = s[:-len(dreamer)]

    elif s[-len(dream):] == dream:
        s = s[:-len(dream)]
    else:
        ans = "NO"
        break

    if s == "":
        ans = "YES"
        break

print(ans)
