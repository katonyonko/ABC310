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
5
00110
30
101010000100101011010011000010
"""

def solve(test):
  N=int(input())
  S=input()
  ans=0
  now=-10**15
  tmp=[now]*N
  for i in range(N):
    if S[i]=='0':
      now=i
    else:
      tmp[i]=now
  for i in range(N):
    if S[i]=='0':
      ans+=i
    else:
      if tmp[i]==-10**15:
        ans+=(i+2)//2
      else:
        ans+=(i-tmp[i]+1)//2
        if (i-tmp[i])%2==0: ans+=tmp[i]
        else: ans+=1
    # print(i,ans)
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