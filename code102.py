import sys

class Graphs:

    def __init__(self):
        self.nodes = []
        self.graphs = []
        self.nodeCount = 0

    def addNode(self, v):

        if v in self.nodes:
            print(v, "node already exists")

        else:
            self.nodeCount += 1
            self.nodes.append(v)

            for x in self.graphs:
                x.append(0)

            temp = []

            for x in range(self.nodeCount):
                temp.append(0)

            self.graphs.append(temp)

            print(v, "is added")

    def addEdge_Undirected_Unweighted(self):

        v1 = input("Enter first vertex: ")
        v2 = input("Enter second vertex: ")

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")

        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = 1
            self.graphs[index2][index1] = 1

            print("Edge added successfully")

    def addEdge_Undirected_weighted(self):

        v1 = input("Enter first vertex: ")
        v2 = input("Enter second vertex: ")
        w = int(input("Enter weight: "))

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")

        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = w
            self.graphs[index2][index1] = w

            print("Undirected weighted edge added")

    def addEdge_directed_weighted(self):

        v1 = input("Enter source vertex: ")
        v2 = input("Enter destination vertex: ")
        w = int(input("Enter weight: "))

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")

        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = w

            print("Directed weighted edge added")

    def deleteGraph(self, v):

        if v not in self.nodes:
            print(v, "not present")

        else:
            self.nodeCount -= 1

            index1 = self.nodes.index(v)

            self.nodes.pop(index1)
            self.graphs.pop(index1)

            for x in self.graphs:
                x.pop(index1)

            print(v, "deleted")

    def printGraph(self):

        print("\nAdjacency Matrix:")

        print("   ", end="")

        for node in self.nodes:
            print(node, end=" ")

        print()

        for i in range(self.nodeCount):

            print(self.nodes[i], end="  ")

            for j in range(self.nodeCount):
                print(self.graphs[i][j], end=" ")

            print()


if __name__ == "__main__":

    obj = Graphs()

    while True:

        print("\n========== GRAPH MENU ==========")
        print("1. Add Node")
        print("2. Add Edge (Undirected Unweighted)")
        print("3. Add Edge (Undirected Weighted)")
        print("4. Add Edge (Directed Weighted)")
        print("5. Print Graph")
        print("6. Delete Vertex")
        print("0. Exit")

        n = int(input("Enter your choice: "))

        if n == 1:

            v = input("Enter vertex: ")
            obj.addNode(v)

        elif n == 2:

            obj.addEdge_Undirected_Unweighted()

        elif n == 3:

            obj.addEdge_Undirected_weighted()

        elif n == 4:

            obj.addEdge_directed_weighted()

        elif n == 5:

            obj.printGraph()

        elif n == 6:

            v = input("Enter vertex to delete: ")
            obj.deleteGraph(v)

        elif n == 0:

            print("Program terminated")
            sys.exit(0)

        else:

            print("Invalid choice")