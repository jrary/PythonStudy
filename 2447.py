def draw_stars(a):
    if a == 1:
        return '*'
    stars = draw_stars(a//3)
    L = []
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(a//3)+s)
    for s in stars:
        L.append(s*3)
    return L


n = int(input())
print('\n'.join(draw_stars(n)))
