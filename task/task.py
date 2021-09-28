import datetime

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
        
    
    
    def GetTaskBracket(self, time):
        dict = {}
        dict["xc"] = self.type[3]
        dict["xwt"] = self.type[0] 
        dict["xr"] = self.type[1]
        dict["xp"] = self.type[2]
        dict["xt"] = self.type[4]
        dict["diff"] = self.diff
        dict["d"] = ((self.deadline-datetime.datetime.now()).total_seconds()//3600) * (time/self.time)
        return dict
    
   

        