# from itertools import iterlen
t,ip=10,137
tt=[]
for i in range(ip):
    tt.append([0]*ip)
# print(tt)
dept=[]
# perRow=[5,1,1,0,2,0,0,1,0,3]
ans=0
with open("day4.ip","r") as f:
    for line in f:
        dept.append(line[:-1])
# print(dept)
for i in range(0,ip):
    for j in range(0,ip):
        if dept[i][j]=='@':
            # print("-"*10)
            # print(i,j,"\n---\n")
            dr=[1,0,1, 0, 1,-1,-1,-1]
            dc=[0,1,1,-1,-1,-1, 0, 1]
            for k in range(len(dc)):
                nr=i+dr[k]
                nc=j+dc[k]
                if(0<=nr<ip and 0<=nc<ip):
                    if(dept[nr][nc]=='@'):
                        tt[i][j]+=1
                        # print(nr,nc)
                        # tt[nr][nc]+=1
            ans+=(tt[i][j]<4)
        else:
            tt[i][j]=4
# print (i for i in tt)
print(ans)




