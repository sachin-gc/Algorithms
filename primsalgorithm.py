import heapq
graph={
    "A":[('B',5),('C',10)],
    "B":[('A',5),('C',4),('D',11)],
    "C":[('A',10),('B',4),('D',5)],
    "D":[('B',11),('C',5)]
}
def prims(graph,start):
    mst=[]
    visited=set()
    pq=[(0,start,None)]
    total=0
    while pq:
        weight,currnode,prevnode=heapq.heappop(pq)
        if currnode in visited:
            continue
        visited.add(currnode)
        total+=weight
        if prevnode is not None:
            mst.append((prevnode,currnode,weight))
        for neighbour,edgeweight in graph[currnode]:
            if neighbour not in visited:
                heapq.heappush(pq,(edgeweight,neighbour,currnode))
    return mst,total
start="A"
mst,cost=prims(graph,start)
print(mst)
print(cost)

