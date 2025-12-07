n, m = map(int,input().split())
cnt = 0
for i in range(n-1):
    print(cnt,i+1)
    if n-m>cnt:
        cnt+=1
