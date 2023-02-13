import sys
input = sys.stdin.readline

def check_last(value):
    global a_cnt,c_cnt,g_cnt,t_cnt
    if value=='A':
        a_cnt+=1
    elif value=='C':
        c_cnt+=1
    elif value=='G':
        g_cnt+=1
    elif value=='T':
        t_cnt+=1

def check_first(value):
    global a_cnt,c_cnt,g_cnt,t_cnt
    if value=='A':
        a_cnt-=1
    elif value=='C':
        c_cnt-=1
    elif value=='G':
        g_cnt-=1
    elif value=='T':
        t_cnt-=1

def check_pwd():
    global cnt,a_cnt,c_cnt,g_cnt,t_cnt
    if a_cnt>=a and c_cnt>=c and g_cnt>=g and t_cnt>=t:
        cnt+=1

s,p=map(int,input().split())
dna = list(input())
a,c,g,t=map(int,input().split())
cnt=0
a_cnt,c_cnt,g_cnt,t_cnt=0,0,0,0
for idx in range(p):
    check_last(dna[idx])
check_pwd()
for i in range(p,s):
    j=i-p
    check_last(dna[i])
    check_first(dna[j])
    check_pwd()
print(cnt)

# 2차
# s,p=map(int,input().split())
# dna = list(input())
# a,c,g,t=map(int,input().split())
# cnt=0
# a_cnt,c_cnt,g_cnt,t_cnt=0,0,0,0
# start=0
# for idx in range(p):
#     check_last(dna[idx])
# check_pwd()
# while start+p<=s:
#     check_first(dna[start])
#     start+=1
#     check_last(dna[start+p-1])
#     check_pwd()
# print(cnt)

# 1차
# s,p=map(int,input().split())
# dna = list(input())
# a,c,g,t=map(int,input().split())
# cnt=0
# a_cnt,c_cnt,g_cnt,t_cnt=0,0,0,0
# start=0
# arr=dna[start:start+p]
# for idx in range(len(arr)):
#     check_last(arr[idx])
# check_pwd()
# while start+p<=s:
#     check_first(arr[0])
#     start+=1
#     arr=dna[start:start+p]
#     check_last(arr[-1])
#     check_pwd()
# print(cnt)