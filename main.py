from useri.interact import Manager


mymanage = Manager()


print(" \t Welcome to TSSA")
print("Following are the instructions : ")
print("Press 1 to update tasks")
print("Press 2 to add info about today's slots and generate time table!")

x = input('What do you want?')
if x=='1':

    mymanage.DeleteTasks()
    mymanage.AddTasks()
    mymanage.SaveTasks()
    
elif x=='2':
    mymanage.GetUsersTimeBracket()
    mymanage.swarm()
    mymanage.printresults()