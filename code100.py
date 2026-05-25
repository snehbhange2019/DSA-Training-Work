
def addEdge_Undirected_Unweighted(self, v1, v2):
    if v1 not in self.nodes:
        print(v1, "not present")
        return
    if v2 not in self.nodes:
        print(v2, "not present")
        return
    index1 = self.nodes.index(v1)
    index2 = self.nodes.index(v2)
    self.graph[index1][index2] = 1
    self.graph[index2][index1] = 1

def addEdge_Undirected_Weighted(self):
    pass

def addEdge_Directed_Weighted(self):
    pass

