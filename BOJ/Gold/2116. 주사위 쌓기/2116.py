def find(top, bottom):
	num = [i for i in range(1,7) if i!=top and i!=bottom]
	return max(num)

n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
rule = {0:5,1:3,2:4,3:1,4:2,5:0}
dice = dices[0]
result = 0

for idx in range(len(dice)):
	top, bottom = dice[idx], dice[rule[idx]]
	res = find(top,bottom)
	for d in dices[1:]:
		top, bottom = d[rule[d.index(top)]], d[d.index(top)]
		res += find(top, bottom)
	result = max(result, res)
print(result)