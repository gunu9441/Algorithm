n, m, k = map(int, input().split())
given_list = list(map(int, input().split()))
given_list.sort(reverse=True)
sum = 0
iteration = m // (k+1)
extra = m % (k+1)

max_iteration = k*iteration + extra
min_iteration = iteration
sum = max_iteration*given_list[0] + min_iteration*given_list[1]

print("sum: {}\n".format(sum))

'''
1. list.sort: default ascending
2. idea: add the biggest number as much as possible
'''
