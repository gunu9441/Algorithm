input_str = 'leebros'
sorted_str_as_list = sorted(input_str)
input_str = "".join(sorted_str_as_list)

print(sorted_str_as_list)
print(input_str)

num, k = map(int, input().split())
num_array = list(map(int, input().split()))

num_array.sort(reverse=True)
print(num_array)
print(num_array[k-1])
