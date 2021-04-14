def ancestor(n, lst):
    if P[n]:
        lst.append(P[n])
        ancestor(P[n], lst)

def treesize(v):
    global cnt
    if v == 0 : return
    treesize(L[v])
    cnt +=1
    treesize(R[v])

def common_ancestor():
    for i in lst_n1:
        for j in lst_n2:
            if i == j:
                return i


for tc in range(1, int(input())+1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    P = [0] * (V+1)
    L = [0] * (V+1)
    R = [0] * (V+1)
    cnt = 0

    for i in range(0, len(arr)//2):
        p = arr[i*2]
        c = arr[i*2+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p

    lst_n1 = []
    lst_n2 = []
    ancestor(n1, lst_n1)
    ancestor(n2, lst_n2)
    common_anc = common_ancestor()

    cnt = 0
    treesize(common_anc)

    print('#{} {} {}'.format(tc, common_anc, cnt))

