# hot potaote game also known as passing the parcel is a group activity.
# In this the participants form a circle and start passing a parcel or a hot potato to the person sitting next.
# In this particular game the person who comes at the position fixed at the start of the game is eliminated.
# queue library used in this program is included in the same folder.
from queue import Queue

players = Queue()

num = int(input("Enter number of players"))
for i in range(num):
	player =input("enter the name of player, %s ".format(i))
	players.enqueue(player)

# Eliminator is the position the player at this position is eliminated first
eliminator = input("Enter position of the player to be eliminated")

count = 0
while players.size() > 1:
	if (count % num) == 0:
		players.dequeue()

	else:
		tempout = players.dequeue()
		players.enqueue(tempout)

	count += 1

print(players.dequeue())





