import pickle
import datetime
from annealing.getperm import GetCombination, GetDifferentCombination, BoltzmannFunction ,GetPermutation, GetDifferentPermutation
from task.task import task
from calculation.calc import GetEnergy


    


class Manager:
    def __init__(self):
        self.ListTask = []
        try:
            with open('tasks.dum','rb') as f:
                self.ListTask = pickle.load(f)
        except : 
            print('File tasks.dm not found!')
        for i in range(0,len(self.ListTask)):
            self.ListTask[i].id = i
        self.UsersTimeSlots = []
        self.TaskToTime = {}
        self.mincon = []
        
    def GetUsersTimeBracket(self):
        print('Enter all data in 24Hrs System!')
        n = int(input('How many slots do you have in your day?'))
        date = [0,0,0]
        date[0] = int(input('What day is it?'))
        date[1] = int(input('What month is it?'))
        date[2] = int(input('What year is it?'))
        for x in range(0,n):
            h = int(input('Your '+str(x+1)+'th slot starts at? Hour : '))
            m = int(input('Your '+str(x+1)+'th slot starts at? Minutes : '))
            he = int(input('Your '+str(x+1)+'th slot ends at? Hour : '))
            me = int(input('Your '+str(x+1)+'th slot ends at? Minutes : '))
            self.UsersTimeSlots.append((datetime.datetime(date[2],date[1],date[0],h,m,0,0),datetime.datetime(date[2],date[1],date[0],he,me,0,0),((he-h)*60 + (me-m))/30))
    def PrintTasks(self):
        i = 1
        for x in self.ListTask:
            print(i, x.course, x.topic, x.desc)
            i+=1

    def DeleteTasks(self):
        print('Which tasks would you like to delete?')
        self.PrintTasks()
        x = input('Please enter them as a string with commas, no whitespace! :')
        if x=='':
            return
        for y in x.split(','):
            del self.ListTask[int(y)-1]
    def SaveTasks(self):
        with open('tasks.dum','wb') as f:
            pickle.dump(self.ListTask,f)
    def AddTasks(self):
        num = int(input('How many tasks would you like to add?'))
        ids = len(self.ListTask)
        for i in range(0,num):
            print('For the ',i,'th task!')  
            self.ListTask.append(task(ids+1,input('Which course?'),input('Which topic?'),(float(input('What is the Lecture Watching Component?')),float(input('What is the learning/memorizing Component?')),float(input('What is the Problem Solving Component?')),float(input('What is the Coding Component?')),float(input('What is the Writing as an assignment Component?'))),int(input('Tentative Time Required?(In multiples of 30 minutes!)')),input('Rate the Difficulty?'),datetime.datetime(int(input('Deadline : Year?')),int(input('Deadline : Month?')),int(input('Deadline : Day?')),int(input('Deadline : Hour?')),int(input('Deadline : Minute?')),0,0),input('Briefly Describe the Project!')))
    
    def GenerateTimeSlot(self):
        L = []
        for x in self.UsersTimeSlots:
            L.append(x[2])
        return L
    
    def GenerateEnergyValue(self, L):
        Z = []
        dict = {}
        for l in L:
            Z.append(l[0])
            dict[l[0]] = self.ListTask[l[0]].GetTaskBracket(l[1])
        return GetEnergy(dict,Z)
    
    def metropolis(self, t2t,taken,iter = 100):
        curr = GetPermutation(taken)
        minenergy = self.GenerateEnergyValue(curr)
        minconf = curr
        mintaken = taken
        for k in range(0,iter):
            neighbours = []
            for i in range(0,10):
                z = GetDifferentCombination(t2t,mintaken)
                for j in range(0,10):
                    neighbours.append((GetPermutation(z),z))
            for j in range(0,100):
                neighbours.append((GetDifferentPermutation(curr),mintaken))
            for n in neighbours:
                enc = self.GenerateEnergyValue(n[0])
                if enc < minenergy:
                    minenergy = enc
                    minconf = n[0]
                    mintaken = n[1]
            ei = self.GenerateEnergyValue(curr)
            if BoltzmannFunction(minenergy-ei) > 1.5:
                curr = minconf
            else:
                break
        return minconf,minenergy

    def swarm(self):
        minconf = []
        minenergy = 100000000000
        b = [((x[1]-x[0]).total_seconds())//1800 for x in self.UsersTimeSlots]
        t2 = {}
        i = 0
        
        for x in self.ListTask:
            t2[i] = x.time
            i+=1
        for k in range(0,10):
            print('done')
            z = GetCombination(t2,b)
            x,y = self.metropolis(t2,z)
            if y < minenergy:
                minenergy = y
                minconf = x
        self.mincon = minconf

    def printresults(self):
        i = 1
        for l in self.mincon:
            print(i,'.',self.ListTask[l[0]].desc,' : Do this for ',l[1]*30,' minutes.')
        


            