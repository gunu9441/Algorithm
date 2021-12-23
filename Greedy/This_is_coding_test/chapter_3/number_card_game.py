given_matrix = []
prev_value = 0
row, column = map(int, input().split())
for idx in range(row):
    given_matrix.append(list(map(int, input().split())))

for element in (given_matrix):
    value = min(element)
    prev_value = max(prev_value, value)

result = prev_value
print(result)

'''
for element in (given_matrix):
    value = min(element)
    if prev_value < value:
        prev_value = value
    else:
        continue
        
'''
'''
## Summary

* Implementation
1. Have to initialize the list when we want to use list. If not, we have to use
append method to add the element in the list because the python list is dynamically
intialized array.
ex) given_matrix.append(list(map(int, input().split())))

2. min(iterable) or min(first_component, second, third...)
* Idea
Select the lowest number in each of the rows and compare them, And then pick the
lowest number again.

* reference
1. internal structure of python list: 
https://seoyeonhwng.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%82%B4%EB%B6%80-%EA%B5%AC%EC%A1%B0-f04847b58286
2. solution of list usage: https://power-of-optimism.tistory.com/123
'''
