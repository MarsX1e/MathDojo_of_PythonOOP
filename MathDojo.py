# Part 1
class MathDojo(object):
    def __init__(self):
        self.value=0
    def add(self,*numbers):
        self.value+=sum(numbers)
        return self
    def subtract(self,*numbers):
        self.value-=sum(numbers)
        return self
math=MathDojo()
print math.add(2).add(2,5).subtract(3,2).value

# Part 2

class MathDojo1(object):
    def __init__(self):
        self.value=0
    def add(self,*numbers):
        sum1=0
        for number in numbers:
            if isinstance(number,int):
                sum1+=number
            else:
                sum1+=sum(number)
        self.value+=sum1
        return self
    def subtract(self,*numbers):
        sum1=0
        for number in numbers:
            if type(number)==int:
                sum1+=number
            else:
                sum1+=sum(number)
        self.value-=sum1
        return self
math1=MathDojo1()
print math1.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).value