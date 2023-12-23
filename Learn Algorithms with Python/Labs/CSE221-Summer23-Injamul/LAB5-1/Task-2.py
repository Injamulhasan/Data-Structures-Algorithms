import math
def titan(graph, source, end):
  store =  [math.inf]*len(graph)
  p = [None]*len(graph)
  store[source] = 0
  queue = [source]

  
file = open('input2.txt', 'r')
output=open("output2.txt","w")
T = int(file.readline())

for i in range(T):
  place, road = map(int, file.readline().strip().split())
  graph = [[0 for a in range(place+1)] for a in range(place+1)]
  erenLoc = 1
  erenDest = place
  if road == 0:
    output.write("0"+"\n")
  elif road == 1:
    vertex1, vertex2, titans= map(int, file.readline().strip().split())
    output.write(str(titans)+"\n")
  else:
    for i in range(road):
      vertex1, vertex2, titans= map(int, file.readline().strip().split())
      graph[vertex1][vertex2] = titans
      graph[vertex2][vertex1] = titans
    
    total = titan(graph, erenLoc, erenDest)
    output.write(str(total))