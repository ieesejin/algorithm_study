# https://www.acmicpc.net/problem/1620


import sys

N, M = map(int, sys.stdin.readline().split())
pokemons = {}
for i in range(N):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[pokemon] = i+1
    pokemons[str(i+1)] = pokemon

for j in range(M):
    problem = sys.stdin.readline().rstrip()
    print(pokemons[problem])


# import bisect
#
#
# N, M = map(int, input().split())
# pokemons = []
# answer = []
#
# for i in range(N):
#     pokemon = input()
#     pokemons.append((pokemon, i+1))
#
# sorted_pokemons = sorted(pokemons)
# keys = [x[0] for x in sorted_pokemons]
#
# for j in range(M):
#     problem = input()
#     if problem.isdigit():
#         print(pokemons[int(problem) - 1][0])
#     if problem.isalpha():
#         print(sorted_pokemons[bisect.bisect_left(keys, problem)][1])

