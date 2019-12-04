from Equation import Equation
from Utilities import clearScreen

# System Class handles all System Functionalities


class System:
    def __init__(self):
        pass

    # Class Methods
    def showMenu():
        clearScreen()
        print('''
        MAIN MENU

        1. Find Roots of Equation
        2. About
        3. Quit

        ''')
        choice = input('\tEnter Your Choice : ')
        return choice

    def runEvaluator():
        e = Equation()
        e.readEquation()
        e.solveEquation()

    def aboutInfo():
        clearScreen()
        print('''
        EQUATION EVALUATOR : PPS Mini Project
            ( Made with Python 3 )

        Project Members : 
            Rahul Badgujar      FE1002
            Ganesh Bhise        FE1004
            Prathamesh Inde     FE1013
            Prathamesh Jadhav   FE1015
            Yash Jagtap         FE1016
            Omkar Raskar        FE1035
            Rahul Salunkhe      FE1036
            Mahesh Yewale       FE1057
        ''')

    def exitProgram():
        quit()

    # This runs the whole program
    def mainloop():
        # The Application Loop
        while True:
            choice = System.showMenu()
            try:
                if choice == '1':
                    System.runEvaluator()
                elif choice == '2':
                    System.aboutInfo()
                elif choice == '3':
                    break
                if choice not in ['1','2','3']:
                    raise Exception('Not a Valid Choice !')
            except Exception as msg:
                print('Exception Caught : '+str(msg))
                continue

            input('\n\tEnter any key to Continue ...')
