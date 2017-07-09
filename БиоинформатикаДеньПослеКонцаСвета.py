def graf2(mas,visited,ways,i):
    from collections import deque
    queue = deque()
    queue.append(i)
    result = 0
    while queue:
        # print(stack)
        current = queue.popleft()
        visited[current] = True
        for neighbour in ways[current]:
            if not visited[neighbour] and neighbour not in queue:
                queue.append(neighbour)
        if mas[current] > result:
            result = mas[current]
    return result
def graf1(mas,visited,ways,i):
    stack = [i]
    result = 0
    while stack:
        current = stack.pop()
        visited[current] = True
        for neighbour in ways[current]:
            if not visited[neighbour] and neighbour not in stack:
                stack.append(neighbour)
        if mas[current] > result:
            result = mas[current]
    return result
choice=input('В ширь или не в ширь(1 или 2):')
mas=input("Значения высот графа:")
ways=input('Словарь(от графа):')
start=int(input('Координта начала:'))
visited=[]
for i in mas:
    visited.append(False)
if choice=='1':
    print(graf2(mas,visited,ways,start))
else:
    print(graf1(mas, visited, ways, start))
