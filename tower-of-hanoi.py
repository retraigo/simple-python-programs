# I remember when my curiosity made me try it with 69 disks. 

n = 3 # Number of disks
steps = 0
# x = disc
# initial = initial position
# final = final position
# spare = spare position
def move(x, initial, final, spare):
    global steps
    if x == 1: 
        print("Move disc from ", initial, " to ", final)
        steps += 1
    else:
        move(x - 1, initial, spare, final)
        move(1, initial, final, spare)
        move(x - 1, spare, final, initial)
move(n, "a", "c", "b")
print(steps, "steps")
