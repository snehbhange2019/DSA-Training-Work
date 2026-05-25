
import sys
class Graphs: 
    def __init__(self):
      self.nodes=[]
      self.graphs=[]
      self.nodeCount=0
      
    def addNode(self,v):
      if v in self.nodes:
        print(v,"node already exist")
      else:
        self.nodeCount+=1
        self.nodes.append(v)
        for x in self.graphs:
          x.append(0)
        temp=[]
        for x in range(self.nodeCount):
          temp.append(0) #temp[]=0
        self.graphs.append(temp)
        print(v," is added")


    def addEdge_directed_weighted(self):
      pass

    def addEdge_Undirected_Unweighted(self):
      pass

    def addEdge_Undirected_weighted(self):
      pass

    def addEdge_Undirected_weighted(self):
      pass

    def printGraph(self):
      print(*self.nodes)
      for i in range(self.nodeCount):
        for j in range(self.nodeCount):
          print(self.graphs[i][j],end=" ")
        print("")

    def deletGraph(self):
      pass

if __name__=="__main__":
  obj=Graphs()

  while True:

    print("\n1. (insertion) add a node using adjacency matrix representation")
    print("2. (insertion) add an edge using adjacency matrix representation")
    print("3. (insertion)add a edge undirected weighted graph")
    print("4. (insertion) add a edge directed weighted graph")
    print("5. print graph")
    print("6. delet operation")
    print("0. exit")

    n=int(input("enter any choice: "))

    if n==1:
      v=input("enter vertex")
      obj.addNode(v)

    elif n==2:
      obj.addEdge_Undirected_Unweighted()

    elif n==3:
      obj.addEdge_Undirected_weighted()

    elif n==4:
      obj.addEdge_directed_weighted()

    elif n==5:
      obj.printGraph()

    elif n==6:
      obj.deletGraph()

    elif n==0:
      sys.exit(0)

    else:
      print("invalid choice")