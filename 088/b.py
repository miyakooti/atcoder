_ = input()
l = map(int, input().split())
l = list(l)


alice = []
bob = []

while True:

    # alice

    max_value = max(l)
    alice.append(max_value)
    l.remove(max_value)
    if l == []:
        break

    # bob

    max_value = max(l)
    bob.append(max_value)
    l.remove(max_value)
    if l == []:
        break

ans = sum(alice) - sum(bob)
print(ans)
