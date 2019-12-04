from os import system, name

# SimpleMath Class has basic Maths Funcions


class SimpleMath:
    def __init__(self):
        pass

    # Class Methods
    def getFactors(n):
        factors = list()
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        return factors

    def syntheticDivision(values):
        t = values[0]
        for i in range(2, len(values)):
            values[i] = values[i]+(t*values[i-1])
        return values

# Function defined to Clear Console Screen


def clearScreen():
    if name == 'nt':
        system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


# For Module Testing, neglet
if __name__ == '__main__':
    SimpleMath.syntheticDivision([-1, 2, 9, 13, 6])
