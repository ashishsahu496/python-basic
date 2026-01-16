class InstanceCount:

    __Counter=0

    def __init__(self):
        InstanceCount.__Counter+=1

    def getInstanceCount():
        return InstanceCount.__Counter


obj1=InstanceCount()
obj2=InstanceCount()
obj3=InstanceCount()
obj4=InstanceCount()

print("number of object in class are :",InstanceCount.getInstanceCount())