import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
5 2 2
1 3
3 4
5 1 2
1 3
3 4
6 4 0
10 6 8
5 9
1 4
3 8
1 6
4 10
5 7
5 6
3 7
"""

def solve(test):
  N,T,M=map(int, input().split())
  G=[[] for _ in range(N)]
  for _ in range(M):
    a,b=map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
  ans=0
  
  def EulerTour(G):
      Q = [(~0,0), (0,0)] # 根をスタックに追加
      now=[]
      while Q:
          i,p = Q.pop()
          if i >= 0: # 行きがけの処理
              if p==len(now): now.append([i])
              else: now[p].append(i)
              if sum([len(now[j]) for j in range(len(now))])==N:
                if len(now)==T:
                  nonlocal ans
                  ans+=1
              else:
                for j in range(len(now)):
                  flg=0
                  for k in G[i+1]:
                    if k in now[j]: flg=1
                  if flg==0:
                    Q.append((~(i+1),j))
                    Q.append((i+1,j))
                Q.append((~(i+1),len(now)))
                Q.append((i+1,len(now)))
          else: # 帰りがけの処理
            for j in range(len(now)):
              if now[j][-1]==~i:
                if len(now[j])>1: now[j].pop()
                else: now.pop()

  EulerTour(G)
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)