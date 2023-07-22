from itertools import combinations
import sys
input=sys.stdin.readline

def get_distance(a,b):
    dy,dx=a[0]-b[0],a[1]-b[1]
    if dy<0: dy*=-1
    if dx<0: dx*=-1
    return dy+dx

n,m=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(n)]
houses=[[y,x] for y in range(n) for x in range(n) if city[y][x]==1]
chickens=[[y,x] for y in range(n) for x in range(n) if city[y][x]==2]
cases=combinations(chickens,m)
result=1e9

for case in cases:
    distance=0
    for house in houses:
        house_distance=1e9
        for chicken in case:
            house_distance=min(house_distance,get_distance(house,chicken))
        distance+=house_distance
    result=min(result,distance)

print(result)