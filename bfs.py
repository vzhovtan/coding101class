from collections import deque

def bfs(struct, first, last):
  searched = []
  search_queue = deque()
  search_queue += struct[first]
  while search_queue:
    print(search_queue)
    item = search_queue.popleft()
    if not item in searched:
      if cond(item, last):
        print(f'"{last}" is reachable from "{first}"')
        return True
      else:
        search_queue += struct[item]
        searched.append(item)
  return False

def cond(item, check):
  if item == check:
    return True
  return False

# cab ---> bat
struct = {'cab': ['car', 'cat'], 'car': ['cat', 'bar'], 'cat': ['mat', 'bat'], 'bar': ['bat'], 'mat': ['bat']}
bfs(struct, 'cab', 'bat')

  