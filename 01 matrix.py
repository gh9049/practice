import collections
mat = [[0,0,0],[0,1,0],[1,1,1]]
rows,cols=len(mat),len(mat[0])
visit=set()
q=collections.deque()

for r in range(rows):
    for c in range(cols):
        if mat[r][c]==0:
            visit.add((r,c))
            q.append((r,c))
while q:
    r,c=q.popleft()
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        row,col=r+dr,c+dc
        if 0<=row<rows and 0<=col<cols and (row,col) not in visit:
            mat[row][col] = mat[r][c]+1
            visit.add((row,col))
            q.append((row,col))
print(mat)
