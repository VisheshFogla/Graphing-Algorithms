import csv
    
    
#taking input and populating the edges list with the all edges and their weights.    
with open('fordfulkerson-deliverable1.txt', 'r') as csv_file:
    file_handle = csv.reader(csv_file)
    data = next(file_handle)
    
number_of_vertices = int(data[0])
graph = [ [ 0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
edges = []

spanning_tree = []

k = 0

for i in range(0, len(data)):
    data[i] = int(data[i])    
    

for i in range(0, number_of_vertices):
    for j in range(0, number_of_vertices):
        k += 1
        graph[i][j] = int(data[k])
        if (int(data[k]) != 0):
            edges.append((int(data[k]),i,j))
edges.sort()

def selectPath(pathList, lastVertex, reached):
    
    while pathList:
        
        element = pathList.pop(0)
        
        for i in range(len(graph[element])):
            
            if reached[i] is False:
                if graph[element][i] > 0:
                    pathList.append(i)
                    reached[i] = True
                    lastVertex[i] = element
    
    


def searchPath(graph, source, sink, lastVertex):
    
    total_number = len(graph)
    
    #Set all the values in the reached array is set to false.
    reached = [False] * total_number
    
    list = []
    list.append(source)
    
    reached[source] = True
    
    selectPath(list, lastVertex, reached)
    
    if(reached[sink]):
        return True
    else:
        return False
 
 
def fordAlgo(graph, source, sink):
    
    lastVertex = [-1] * (len(graph))
    
    max_flow = 0
    
    while searchPath(graph, source, sink, lastVertex):
        
        min_flow = 999999999
        a = sink
        
        while a != source:
            
            min_flow = min(min_flow, graph[lastVertex[a]][a])
            a = lastVertex[a]
 
        max_flow = max_flow + min_flow
        
 
        list = trackFlowValue(graph, source, sink, lastVertex, min_flow)
            
        print("")
        print("Augmenting Path found: ", end =" ")
        
        i = len(list) - 1;
        
        while i >= 0:
            print(list[i], end =" ")
            i = i - 1
        
        print("with flow: " + str(min_flow), end=" ")
        
    print(" ")
    print("Total flow: " + str(max_flow))    
    return max_flow

def trackFlowValue(graph, source, sink, lastVertex, min_flow):
    
    vertexList = []
    vertexList.append(sink)
    
    temp1 = sink
    
    while temp1 != source:
        
        temp2 = lastVertex[temp1]
        
        vertexList.append(temp2)
        
        graph[temp2][temp1] = graph[temp2][temp1] - min_flow
        graph[temp1][temp2] = graph[temp1][temp2] + min_flow
        
        temp1 = lastVertex[temp1]
    
    return vertexList

fordAlgo(graph, 0, len(graph) - 1)
    
    
    