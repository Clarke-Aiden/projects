#Aiden Clarke
#5/30/23
#midterm q1

tg = 0
cg = 1
for i in range (64):
    print(i  , tg)
    tg += cg
    cg *= 2

print("total grains on the chessboard is:",tg)
input("press enter to exit")