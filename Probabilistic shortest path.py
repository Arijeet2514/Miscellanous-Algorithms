NODES=int(input('Enter no. of Nodes- '))

graph=[[-1 for j in range(NODES)] for i in range(NODES)]

print('Enter initial, final nodes and distance between them')
print('Each values must be separated by space')
print('Assume nodes are zero-indexed')
print('To terminate enter -1 -1 -1')

while(True):
    n1,n2,d=map(int,input().split())
    if n1==-1:
        break
    graph[n1][n2]=d

source=int(input('Enter source node'))
dest=int(input('Enter destination node'))

paths=[]
visited=set()
visited.add(source)
nodestack=list()
indexstack=list()
current_node=source

def next_node(n):
    nxt=[]
    for i in range(NODES):
        if graph[n][i]!=-1:
            nxt.append(i)
    return nxt

i=0
while(True):
    #Find neighbor to the current_node
    neighbors=next_node(current_node)

    #find the next unvisited node
    while i<len(neighbors) and neighbors[i] in visited:
        i+=1
    #if all neighbor nodes are traversed
    if i>=len(neighbors):
        visited.remove(current_node)
        #It means no more node to traverse
        if len(nodestack)==0:
            break
        current_node=nodestack.pop()
        i=indexstack.pop()
    #If destination is reached, append to paths
    elif neighbors[i]==dest:
        paths.append(nodestack+[current_node,dest])
        i+=1
    #Add to nodestack, update visited and current_node
    #Indexstack keep track of indexes such that same path are not repeated
    else:
        nodestack.append(current_node)
        indexstack.append(i+1)
        visited.add(neighbors[i])
        current_node=neighbors[i]
        i=0

dist=[]
ts=0
for i in range(len(paths)):
    s=0
    for j in range(1,len(paths[i])):
        s+=graph[paths[i][j-1]][paths[i][j]]
    dist.append(s)
    ts+=s
dist[:]=[x/(ts*1.0) for x in dist]

p=1
p_index=0
for i in range(len(dist)):
    if dist[i]<p:
        p=dist[i]
        p_index=i
p_path=paths[p_index]

print("Shortest path- ",end=' ')
print(p_path)


