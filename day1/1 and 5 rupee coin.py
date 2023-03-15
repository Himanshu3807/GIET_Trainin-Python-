x=int(input("no. of 5 rupee coins"))
y=int(input("no. of 1 rupee coins"))
z=int(input("Amount"))
if(x * 5 + y < z):
    print(-1)
fives = min(x, z // 5)
ones = z - fives * 5
if(ones > y):
    print(-1)
else:
    print("Total 5rs coin:",fives, "\nTotal 1rs coin:",ones)
