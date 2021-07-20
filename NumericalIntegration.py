#NumericalIntegration.py - Examples of two Python classes that can be further developed to perform numerical integrations found in elementary calculus texts.
####The goal of these two classes was to experiment with the OOP features Python offers. Future work will include an update too follow PEP 8. Also, the class
####Function will be rewritten to implement two special attributes in its initializer: a 'domain' attribute and a'range' attribute, such that the terminology
####is mathematically consistent with the standard definition of a function.

#class Function
class Function:
    
    functions = {0: math.sin, 1: math.cos, 2: math.tan, 3: math.exp}
    
    def __init__(self,option_code=0,x=0):
        self._option_code = option_code
        self._x = x
    
    @property
    def code(self):
        return self._option_code
    
    @code.setter
    def code(self,new_code):
        self._option_code = new_code
        
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,new_x):
        self._x = new_x
        
    def f_x(self):
        if self.code in self.functions:
            return self.functions[self.code](self.x)

    def __add__(self,other):
        sum = self.f_x() + other.f_x()
        return sum
    
    def __mul__(self,other): 
        product = self.f_x() * other.f_x()
        return product
    
    def __truediv__(self,other):
        quotient = self.f_x() / other.f_x()
        return quotient
    
    
#class NumericalIntegration
class NumericalIntegration:
    
    #defaults to math.sin
    def __init__(self,func=0):
        self.function = Function(func)
##(source: https://en.wikipedia.org/wiki/Numerical_integration
#
#rectangle rule of numerical integration------------------------------------------------------------
    def rectangle_rule(self, limit_a,limit_b):
        self.function.x = limit_a
        return (limit_b - limit_a)*self.function.f_x() 
    
##midpoint rule of numerical integration----------------------------------------------------------------
    def midpoint_rule(self,limit_a,limit_b):
        self.function.x = (limit_a + limit_b) / 2
        return (limit_b - limit_a) * self.function.f_x()
        
##trapezoidal rule of numerical integration-----------------------------------------------------------------
    def trapezoidal_rule(self, limit_a, limit_b):
        self.function.x, x_a, f_a = limit_a, self.function.x, self.function.f_x()
        self.function.x, x_b, f_b = limit_b, self.function.x, self.function.f_x()
        return (limit_b - limit_a)*(f_a + f_b)/2
