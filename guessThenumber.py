import random
x = random.randint(0,10)

print("You have to guess a number in the range 0 to 10. You will be given 2 hints and 2 chances.")
if x%2==0:
	print("The number is even.")
else:
	print("The number is odd.")


y = int(input())
if y == x:
	print("You won.")
	exit()

else:
	print("Wrong. Next hint is:")


if x in range(0,5):
	print("The number lies in the first half of the range.")
if x in range(5,11):
	print("The number lies in the second half of the range.")

l = int(input())
if l==x:
	print("YOU WON!")

else:
	print("The number was:",x)
	print("YOU LOSER!")
	exit()


	
