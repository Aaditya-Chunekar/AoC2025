t,ip=10,137
#should take dept over fileName here - dept should be modified in the counting loop 
def partOne(dept, h):
    tt=[]
    DIRS = ((1,0), (0,1), (1,1), (1,-1))
    for i in range(h):
        tt.append([0]*h)
    # print(tt)
    
    # perRow=[5,1,1,0,2,0,0,1,0,3]
    ans=0
    
    # print(dept)
    for i in range(0,h):
        for j in range(0,h):
            if dept[i][j]=='@':
                # print("-"*10)
                # print(i,j,"\n---\n")
                
                for dr,dc in DIRS:
                    nr=i+dr
                    nc=j+dc
                    if(0<=nr<h and 0<=nc<h):
                        if(dept[nr][nc]=='@'):
                            tt[i][j]+=1
                            # print(nr,nc)
                            tt[nr][nc]+=1
            else:
                tt[i][j]=4
    for i in range(h):
        for j in range(h):
            if(tt[i][j]<4):
                dept[i][j]='.'
                ans+=1
    return ans, dept

dept=[]
ans=1
with open("day4.ip","r") as f:
        for line in f:
            dept.append(list(line[:-1]))
# partOne
ansOne,dept=partOne(dept,ip)
print(ansOne)

# partTwo
ansTwo=0
while(ans):
    ans=0
    ans,dept=partOne(dept,ip)
    # print(ans,"-"*10)
    ansTwo+=ans
print(ansTwo+ansOne)




