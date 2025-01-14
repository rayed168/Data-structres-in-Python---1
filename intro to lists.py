name = ["Rayed", "Mimo", "Max"]
#positive indexing left to right while 0 ... n-1
#negative indexing right to left -n .... -1
print(name[0])
print(name[2])
print(name[-1])
print(name[-2])

different_list = [1, True, "Mimo", 1.0002, [1, 2, (1, 2, 3)]]

#Lists are hetrogenous

print(different_list[4][2][2])

numbers = [10, -1, 4, 5, 1, 1, 1]
numbers.sort(reverse=False)
print(numbers)

numbers.reverse()
print(numbers)

l = [1, 2, 3] * 3
print(l)

print(l[0 : 2])

l.clear()
print(l)