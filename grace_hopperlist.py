grace_hopper = [] 
grace_hopper.extend(["Holia", "Francisca"])
grace_hopper.extend (["Talya", "Ann", "Gloria"])       
grace_hopper.pop(3)
grace_hopper.insert(2, "Dewan")
grace_hopper.pop(4)

for name in grace_hopper:
	print(grace_hopper)
print (len(grace_hopper))
grace_hopper[4] = "Abigal"
print (grace_hopper)
