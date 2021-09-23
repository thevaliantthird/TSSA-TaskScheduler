import pickle
import datetime
import annealing.getperm
class Manager:
    def __init__(self):
        self.ListTask = []
        with open('tasks.dum','rb') as f:
            self.ListTask = pickle.load(f)
        for i in range(0,len(self.ListTask)):
            self.ListTask[i].id = i
        self.UsersTimeSlots = []
        self.TaskToTime = {}
        
    def GetUsersTimeBracket(self):
        print('Enter all data in 24Hrs System!')
        n = int(input('How many slots do you have in your day?'))
        date = [0,0,0]
        date[0] = int(input('What day is it?'))
        date[0] = int(input('What month is it?'))
        date[0] = int(input('What year is it?'))
        for x in range(0,n):
            h = int(input('Your ',x+1,'th slot starts at? Hour : '))
            m = int(input('Your ',x+1,'th slot starts at? Minutes : '))
            he = int(input('Your ',x+1,'th slot ends at? Hour : '))
            me = int(input('Your ',x+1,'th slot ends at? Minutes : '))
            self.UsersTimeSlots.append((datetime.datetime(date[2],date[1],date[0],h,m,0,0),datetime.datetime(date[2],date[1],date[0],he,me,0,0),((he-h)*60 + (me-m))/30))
    def PrintTasks(self):
        i = 1
        for x in self.ListTask:
            print(i, x.course, c.topic, x.desc)
            i+=1

    def DeleteTasks(self):
        print('Which tasks would you like to delete?')
        PrintTasks()
        x = input('Please enter them as a string with commas, no whitespace! :')
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
            self.ListTask.append(ids+1,input('Which course?'),input('Which topic?'),(input('What is the Lecture Watching Component?'),input('What is the learning/memorizing Component?'),input('What is the Problem Solving Component?'),input('What is the Coding Component?'),input('What is the Writing as an assignment Component?')),int(input('Tentative Time Required?(In multiples of 30 minutes!)')),input('Rate the Difficulty?'),datetime.datetime(int(input('Deadline : Year?')),int(input('Deadline : Month?')),int(input('Deadline : Day?')),int(input('Deadline : Hour?')),int(input('Deadline : Minute?')),0,0),input('Briefly Describe the Project!'))
    
    def GenerateTimeSlot(self):
        L = []
        for x in self.UsersTimeSlots:
            L.append(x[2])
        return L
    
    def GenerateEnergyArgument(self, L):
        Z = []
        for l in L:
            Z.append(self.ListTask[l[0]].GetTaskBracket(l[1]))
        return Z


            