space=[]
def makeSpace(space, fileName):
    with open(fileName, "r") as f:
        for line in f:
            space.append(list(line[:-1]))
makeSpace(space, "day7.ip")        
for i in space:
    print(i)
w, h=len(space[0]), len(space)
# most important is this visited set
visited=set()
sp=(1,w//2)
def findBottom(space,r,c,h):
    for i in range(r,h):
        if(space[i][c]=='^'):
            return [1,i,c]
    return [0]

def recur(space,r,c,h):
    if c < 0 or c >= len(space[0]):
        return 0
    fb=findBottom(space,r,c,h)
    if(fb[0]==0):
        return 0
    if (fb[1], fb[2]) in visited:
        return 0

    visited.add((fb[1], fb[2]))
    
    
    return 1+recur(space,fb[1],fb[2]-1,h)+recur(space,fb[1],fb[2]+1,h)
    
r,c=sp
print(recur(space,r,c,h))
    
# number of times splitter recieves a beam (splitter is encountered)
