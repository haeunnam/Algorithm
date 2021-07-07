# 가중치 인접행렬  # 바로 연결이 안돼있는 경우 INF(무한대)
N = 4

INF = float('inf')
adj = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]

print('가중치 인접 행렬')
for row in adj:
    print(row)
print()

# 거쳐가는 정점 k를  기준으로
for k in range(N):
    # 출발 정점 i 에서
    for i in range(N):
        # 도착 정점 j 까지
        for j in range(N):
            # i에서 k를 거쳐 j 까지 가는 것과 i에서 j까지 바로가는 것중 값이 더 작은 것으로 갱신
            adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

print('결과')
for row in adj:
    print(row)