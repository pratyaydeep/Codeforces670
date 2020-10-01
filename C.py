# Author : Pratyaydeep↯Ghanta
import sys
inp=sys.stdin.buffer.readline
inar=lambda: list(map(int,inp().split()))
inin=lambda: int(inp())
inst=lambda: inp().decode().rstrip('\n\r')
# Am I debugging, check if I'm using same variable name in two places
# Start Pyrival Bootstrap (Pajenegod's Infinite Recursion trick)
from types import GeneratorType
def recursive(f, stack=[]):
  def wrappedfunc(*args, **kwargs):
    if stack: return f(*args, **kwargs)
    else: 
      to = f(*args, **kwargs)
      while True:
        if type(to) is GeneratorType:
          stack.append(to); to = next(to)
        else:
          stack.pop()
          if not stack: break
          to = stack[-1].send(to)
      return to
  return wrappedfunc
# End PyRival Bootstrap;


def centroid(g):
    n=len(g)
    centroid=[]
    size=[0 for i in range(n)]
    @recursive
    def dfs(node,par):
        size[node]=1
        iscent=True
        for nei in g[node]:
            if nei!=par:
                yield dfs(nei,node)
                size[node]+=size[nei]
                if size[nei]> n//2:
                    iscent=False
        if n-size[node]>n//2:
            iscent=False
        if iscent:
            centroid.append(node)
        yield
    dfs(0,-1)
    return centroid,size


_T_=inin()
for _t_ in range(_T_):
    n=inin()
    gr=[[] for i in range(n)]
    vis=[False for i in range(n)]
    for i in range(n-1):
        x,y=inar()
        x-=1
        y-=1
        gr[x].append(y)
        gr[y].append(x)
    cent,size=centroid(gr)
    if len(cent)==1:
        print(x+1,y+1)
        print(x+1,y+1)
    else:
        #print(size)
        opponent=-1
        maxsize=-12
        to_remove=-1
        for node in cent:
            for nei in gr[node]:
                if size[nei]>maxsize and nei not in cent:
                    maxsize=size[nei]
                    opponent=node 
                    to_remove=nei

        if opponent==cent[0]:
            print(cent[0]+1,to_remove+1)
            print(cent[1]+1,to_remove+1)
        else:
            print(cent[1]+1,to_remove+1)
            print(cent[0]+1,to_remove+1)
