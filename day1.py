b,l,r=50,0,99
ans=0
with open("day1.ip","r") as f:
    for line in f:
        # print('-'*10)
        v=int(line[1:])
        # print(line, v)
        if(line[0]=="L"):
            b-=v
            if(b<l):
                b%=100
                
        else:
            b+=v
            if(b>r):
                b%=100
        if(b==0):
           ans+=1
print(ans)

'''
 after the granting of star, 
 git add .; git commit -m "dayOne"; git push
 '''
