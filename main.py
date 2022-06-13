
import time
EXCERCISE_NUMBER=input("Which exercise 1-first, 2-secound,3- third")
tab=["first","secound","third"]
string="Wellcome in "
string2=" exercise"
string3="please input values"
if EXCERCISE_NUMBER== "1":

    print(string + tab[0] + string2)
    time.sleep(1)
    print(string3)


    import task_1


elif EXCERCISE_NUMBER=="2":

    print(string + tab[1] + string2)
    time.sleep(1)
    print(string3)



    import task_2


elif EXCERCISE_NUMBER=="3":
    print(string + tab[2] + string2)
    time.sleep(1)
    print(string3)



    import  task_3


else:
    print("Wrong input")






