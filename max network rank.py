n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
max_rank=0
connections={i:set() for i in range(n)}
for i, j in roads:
    connections[i].add(j)
    connections[j].add(i)
for i in range(n):
    for j in range(i+1,n):
        max_rank = max(max_rank,len(connections[i])+len(connections[j])-(j in connections[i]))
print(max_rank)