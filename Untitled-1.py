class sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def sum1(self):
        self.value1 = self.a + self.b
        return self.value1
    
    
    def sum2(self):
        self.sum1()
        self.value2 = self.value1 + 2
        #return self.value2
        print("THe value",self.value2)

v1=sum(5,6)
# print(v1.sum1())
#print("The sum is: ", v1.sum2())
v1.sum2()
sum(1,2).sum2()