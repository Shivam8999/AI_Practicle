#Python program to solve Tower of Hanoi
def TowerofHanoi(n,source,dest,middle):
    if(n<1):
        print("NOT Possible")
    if(n==1):
        print("MOVE DISK {} FROM {} TO {}".format(n,source,dest))
        return
    TowerofHanoi(n-1,source,middle,dest)
    print("MOVE DISK {} FROM {} TO {}".format(n,source,dest))
    TowerofHanoi(n-1,middle,dest,source)
n=int(input("Enter the number of disk"))
TowerofHanoi(n,"A","C","B")