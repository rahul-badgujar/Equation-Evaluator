from Utilities import SimpleMath, clearScreen

# Equation Class models a Equation and provide useful Functions


class Equation:
    # Class Variables
    standardEquations = ('{A}x + {B} = 0',
                         '{A}x^2 + {B}x + {C} = 0', '{A}x^3 + {B}x^2 + {C}x + {D} = 0')

    def __init__(self):
        self.degree = 0
        self.coefficients = ['A', 'B', 'C', 'D']
        self.solution = list()

    def readEquation(self):
        while True:
            clearScreen()
            try:
                self.degree = int(input('\tEnter the Degree of Equation [ 1/2/3 ] : '))
                if self.degree>3 or self.degree<1:
                    raise Exception('Invalid Degree !')
                else:
                    break
            except Exception as msg:
                print('Exception Caught : '+str(msg))
                continue            
        print('\tEnter the corresponding Coefficients for Standard Form ' +
              self.getEquation())
        while self.degree+1 < len(self.coefficients):
            self.coefficients.pop()
        for i in range(self.degree+1):
            self.coefficients[i] = int(input('\t'+self.coefficients[i]+' : '))
        print('T\n\the Equation entered is : '+self.getEquation())

    def getEquation(self):
        equation = Equation.standardEquations[self.degree-1]
        if self.degree == 1:
            equation = equation.format(
                A=self.coefficients[0], B=self.coefficients[1])
        elif self.degree == 2:
            equation = equation.format(
                A=self.coefficients[0], B=self.coefficients[1], C=self.coefficients[2])
        elif self.degree == 3:
            equation = equation.format(
                A=self.coefficients[0], B=self.coefficients[1], C=self.coefficients[2], D=self.coefficients[3])
        return equation

    def solveEquation(self):
        clearScreen()
        print('\n\tRoots of the Given Equation '+self.getEquation()+' are : ')
        if self.degree == 1:
            self.solveDegree1()
        elif self.degree == 2:
            self.solveDegree2()
        elif self.degree == 3:
            self.solveDegree3()

    def solveDegree1(self):
        a = self.coefficients[0]
        b = self.coefficients[1]
        root1 = (-1)*(b/a)
        self.solution.append(root1)
        self.showSolution()

    def solveDegree2(self):
        a = self.coefficients[0]
        b = self.coefficients[1]
        c = self.coefficients[2]
        discriminant = (b**2-4*a*c)
        if discriminant < 0:
            print('\tNo real roots exits for the Given Equation')
            return
        root1 = (-b+discriminant**0.5)/(2*a)
        root2 = (-b-discriminant**0.5)/(2*a)
        self.solution.append(root1)
        self.solution.append(root2)
        self.showSolution()

    def solveDegree3(self):
        a = self.coefficients[0]
        b = self.coefficients[1]
        c = self.coefficients[2]
        d = self.coefficients[3]
        if d == 0:
            self.solution.append(0)
            self.solveDegree2()
            return
        factorsA = SimpleMath.getFactors(abs(a))
        factorsD = SimpleMath.getFactors(abs(d))
        factorsList = list()
        for i in factorsD:
            for j in factorsA:
                factorsList.append(j/i)
                factorsList.append((-1)*(j/i))

        flag = False
        for i in factorsList:
            value = a*(i**3)+b*(i**2)+c*i+d
            if value == 0:
                synDivResult = SimpleMath.syntheticDivision([i, a, b, c, d])
                if synDivResult[len(synDivResult)-1] == 0:
                    self.solution.append(i)
                    for i in range(self.degree+1):
                        self.coefficients[i] = synDivResult[i+1]
                    self.solveDegree2()
                    flag = True
                    break
        if flag == False:
            print('\tNo real roots exits')

    def showSolution(self):
        for i in range(self.degree):
            print('\tRoot '+str(i+1)+' : '+str(self.solution[i]))


# For Module Testing, neglet
if __name__ == '__main__':
    e = Equation()
    e.readEquation()
    e.solveEquation()
