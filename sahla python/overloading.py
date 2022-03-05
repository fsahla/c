class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hour,self.minute,self.second)

    def __add__(self,other):
        hour=self.hour+other.hour
        minute=self.minute+other.minute
        second=self.second+other.second
        return time(hour,minute,second)

t1=time(6,34,25)
print("first time=",t1)
t2=time(5,25,34)
print("second time=",t2)
print("sum of 2 times=",t1+t2)
