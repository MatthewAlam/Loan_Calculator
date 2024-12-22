num_one = int(input())
num_two = int(input())

def greater(a, b):
    greater_num = [a, b]
    print(f"{max(greater_num)}\n{min(greater_num)}")


if num_one > num_two:
    greater(num_one, num_two)
else:
    greater(num_two, num_one)