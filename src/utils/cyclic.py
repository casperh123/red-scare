# Taken from https://www.geeksforgeeks.org/dsa/detect-cycle-in-a-graph/?fbclid=IwY2xjawOBVT5leHRuA2FlbQIxMQBzcnRjBmFwcF9pZAEwAAEepK75zOx2fqdan9dwrvJHJXvnCxs1MHf_pB7kCFykZMEKdOq8q60dxO79nyw_aem_YN2zd2YQ--hPgNNjw0fKTg

# Utility DFS function to detect cycle in a directed graph
def isCyclicUtil(adj, u, visited, recStack):

    # node is already in recursion stack cycle found
    if recStack[u]:
        return True

    # already processed no need to visit again
    if visited[u]:
        return False

    visited[u] = True
    recStack[u] = True

    # Recur for all adjacent nodes
    for v in adj[u]:
        if isCyclicUtil(adj, v, visited, recStack):
            return True

    # remove from recursion stack before backtracking
    recStack[u] = False
    return False


# Function to detect cycle in a directed graph
def isCyclic(adj):
    V = len(adj)
    visited = [False] * V
    recStack = [False] * V

    # Run DFS from every unvisited node
    for i in range(V):
        if not visited[i] and isCyclicUtil(adj, i, visited, recStack):
            return True
    return False

