# a lesson on functions
l1 = [1,2,3,4,5,6]
l2 = [7,8]
l3 = [234, 567, 8910, 123, 11, 17, 29, 33, 0]

# for x in l1:
# 	if x > 4:
# 		print(x)

# for x in l2:
# 	if x > 4:
# 		print(x)

# You can save yourself some time and effort by putting the above code into a function.

# def greater_than_4(num_list):
# 	for x in num_list:
# 		if x > 5:
# 			print(x)

# greater_than_4(l1)
# greater_than_4(l2)
# greater_than_4(l3)

def add_list(num_list):
	y = 0
	for x in num_list:
		y = x + y
	return y

new_num = add_list(l1)
print(new_num)