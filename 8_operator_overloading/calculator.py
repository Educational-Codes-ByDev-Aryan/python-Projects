
# calculator concept using operator overloading


class point:

    def __init__(self, num1):
        self.num1 = num1

    def sum(self, num2):
        return self.num1 + num2.num1

    def print_result(self, results):
        print(f"The result is {results}")

    def __add__(self, num2):
          return "for addition",self.num1 + num2.num1
    
    def __sub__(self, num2):
         return "for substraction",self.num1 - num2.num1
    
    def __mul__(self, num2):
         return "for multiplication",self.num1 * num2.num1
    
    def __truediv__(self, num2):
         return "for division",self.num1 / num2.num1

p1 = point(52)
p2 = point(5)

# the total resutlts is shown throug this object
result = point(0)

results = p1.sum(p2)
result.print_result(results)

results = p1 + p2
result.print_result(results)

results = p1 - p2
result.print_result(results)

results = p1 * p2
result.print_result(results)

results = p1 / p2
result.print_result(results)