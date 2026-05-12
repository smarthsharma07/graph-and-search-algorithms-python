def dfs(adj_matrix,start):
    n = len(adj_matrix)
    if start < 0 or start >= n:
        return []  

    visited = [False] * n
    order = []
    stack = [start]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        order.append(node)
        for nbr in range(n):
            if adj_matrix[node][nbr] and not visited[nbr]:
                stack.append(nbr)

    return order
