poly = [
	(225,431), (50,176), (136,19), (225,158), (314,19),
	(400,176), (225,431)
]

p = (220,100)

n = len(poly)
count = 0
x, y = p[0], p[1]

for i in range(n-1):
    ax, ay = poly[i][0], poly[i][1]
    bx, by = poly[i+1][0], poly[i+1][1]
    if ((y > ay) != (y > by)) and (x < (y-ay)*(ax-bx)/(ay-by)+ax):
        count += 1
ans =  count%2 != 0

print(ans)

# EOF #
