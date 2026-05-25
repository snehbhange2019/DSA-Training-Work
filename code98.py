import sys
if __name__ == '__main__':
    obj = Graphs()

    while True:
        print("\n1. (Insertion) Add a node using adjacency matrix representation")
        print("2. (Insertion) Add an edge using adjacency matrix representation")
        print("3. (Insertion) Add an edge in undirected weighted graph")
        print("4. (Insertion) Add an edge in directed weighted graph")
        print("5. Print Graph")
        print("6. Delete Operation")
        print("0. Exit\n")

        n = int(input("Enter any choice: "))

        if n == 1:
            obj.addNode()

        elif n == 2:
            obj.addEdge_Undirected_Unweighted()

        elif n == 3:
            obj.addEdge_Undirected_Weighted()

        elif n == 4:
            obj.addEdge_Directed_Weighted()

        elif n == 5:
            obj.printGraph()

        elif n == 6:
            obj.deleteGraph()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice!")