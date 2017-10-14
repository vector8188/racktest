from queue import  Queue

class Register:

    def __init__ (self, registerNumber, cashier):
        self.registerNumber = registerNumber
        self.queue = Queue()
        self.cashier = cashier
    
    def customerProcessingTime(self, cashier, customer):
        totaltime = cashier.serviceTime * customer.items
        return totaltime

