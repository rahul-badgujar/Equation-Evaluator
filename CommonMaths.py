class SimpleMath:
    def __init__(self):
        pass

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


if __name__ == '__main__':
    SimpleMath.syntheticDivision([-1, 2, 9, 13, 6])
