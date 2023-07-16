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
4
1 7 2 9
7
1 10 100 1000 10000 100000 1000000
"""

def solve(test):
  mod=998244353
  N=int(input())
  A=list(map(int, input().split()))
  dp=[0]*(N+1)*(1<<11)
  def idx(i,j):
    return i*(1<<11)+j
  dp[idx(0,1)]=1
  for i in range(N):
    x=pow(A[i],mod-2,mod)
    for j in range(1<<11):
      p=dp[idx(i,j)]
      for k in range(1,min(11,A[i])+1):
        dp[idx(i+1,(j|(j<<k))&((1<<11)-1))]+=p*x
        dp[idx(i+1,(j|(j<<k))&((1<<11)-1))]%=mod
      if A[i]>11:
        dp[idx(i+1,j)]+=p*(A[i]-11)*x
        dp[idx(i+1,j)]%=mod
  ans=sum([dp[idx(N,(1<<10)+i)] for i in range(1<<10)])%mod
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