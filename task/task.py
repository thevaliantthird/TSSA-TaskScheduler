class taskBracket:
    def __init__(self, _type, _time, _proportion, _timere ,parentid):
        self.type = _type
        self.time = _time
        self.proportion = _proportion
        self.id = parentid
        self.timere = _timere

    def GetVector(self):
        return (self.type[0],self.type[1],self.type[2],self.type[3],self.type[4],self.proportion,self.timere)
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
        
    
    
    def GetTaskBracket(self, time)
        if time/self.time < 0.1 :
            return 0
        else:
            return taskBracket(self.type, time, time/self.time, self.id)
    
   

        