class taskBracket:
    def __init__(self, _type, _time, _proportion, parentid):
        self.type = _type
        self.time = _time
        self.proportion = _proportion
        self.id = parentid
    def GetVector(self):
        return (self.type[0],self.type[1],self.type[2],self.type[3],self.type[4],self.proportion)
class task:
    def __init__(self,_id,_course, _topic, _type , _time, _diff,_deadline, _desc):
        self.id = _id
        self.course = _course
        self.topic = _topic
        self.type = _type
        self.time = _time
        self.diff = _diff
        self.deadline = _deadline
        self.desc = _desc
    
    def __init__(self,string):
        x = string.split(',')
        self.course = int(x[0])
        self.topic = int(x[1])
        self.type = int(x[2])
        self.time = int(x[3])
        self.diff = int(x[4])
        self.deadline = float(x[5])
        self.desc = x[6]

    def WriteTask(self,file):
        stra = ''
        stra += str(self.course)
        stra+=','
        stra += str(self.topic)
        stra+=','
        stra += str(self.type)
        stra+=','
        stra += str(self.time)
        stra+=','
        stra += str(self.deadline)
        stra+='\n'
        f = fopen(file)
        f.write(stra)
        f.close()
    
    def GetTaskBracket(self, time)
        if time/self.time < 0.1 :
            return 0
        else:
            return taskBracket(self.type, time, time/self.time, self.id)
    
    def UpdateDes

        