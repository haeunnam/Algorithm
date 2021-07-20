def solution(w,h):
    total = w * h
    gcd = w + h
    while (w!=h):
        if w > h :
            w -= h
        else:
            h -= w
        if w == 1 or h == 1:
            gcd -= 1
            break
    else:
        gcd -= w
    return total - gcd