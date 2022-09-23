


def get_sum(nums, target):
	myhashmap = {}

	for i, value in enumerate(nums): 
		#print(i, " ** ", value)
		diff = target - value
	
		if diff in myhashmap.keys():
			# will not print to console
			return [myhashmap[diff], i]
			#print([myhashmap[diff], i])
			#break

		myhashmap[value] = i

	return



mynums = [2,7,11,15]
thetarget = 9

myindex = get_sum(mynums,thetarget)

print(myindex)
