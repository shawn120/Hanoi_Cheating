'''
A cheating tool for the game of Tower of Hanoi.
Author: Shawn
Github: shawn120
Link: https://github.com/shawn120/hanoi_cheating

Go to the website below to try Tower of Hanoi Game!
https://www.mathsisfun.com/games/towerofhanoi.html
'''
print ("How many disks you want to play with?")
m = int(input ())

def hanoi (n):
    
    piles = []
    for i in range(n, 0, -1):
        piles.append(i)
    disk = {'1': piles, '2':[], '3':[]}

    def start (n, disk, source, temp, target):
        if n > 0:
            start (n-1, disk, source, target, temp)
            if disk[source]:
                disk[target].append(disk[source].pop())
                print("move from "+source+" to "+target)
                start (n-1, disk, temp, source, target)
                
    start(n, disk, "1", "2", "3")
    print("Congraduation! You made it!")
    # print(disk)

hanoi(m)