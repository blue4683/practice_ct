import sys
input=sys.stdin.readline

n,m=map(int,input().split())
row,col=[0],[0]
for _ in range(int(input())):
    rc,pos=map(int,input().split())
    if rc:
        row.append(pos)
    else:
        col.append(pos)
row=sorted(row)
col=sorted(col)
row.append(n)
col.append(m)
max_row,max_col=0,0
for idx in range(1,len(row)):
    tmp=row[idx]-row[idx-1]
    if tmp>max_row:
        max_row=tmp
for idx in range(1,len(col)):
    tmp=col[idx]-col[idx-1]
    if tmp>max_col:
        max_col=tmp
print(max_col*max_row)