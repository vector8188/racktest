class Cashier(object):
    def __init__(self, cashierNumber):
        self.cashierNumber = cashierNumber
        self.serviceTime = 1



class Trainee(Cashier):
    def __init__(self, cashierNumber):
        super(Trainee, self).__init__(cashierNumber)
        self.serviceTime = 2