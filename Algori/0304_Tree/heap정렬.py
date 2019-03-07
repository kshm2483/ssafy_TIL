last = 0

def enq(n):
    global last
    last += 1
    c = last
    p = c // 2
    q[last] = n
    while c > 1 and q[p] > q[c]:
        t = q[p]
        q[p] q[c]
        q[c] = t
        c = p
        p = p // 2