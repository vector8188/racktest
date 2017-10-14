class Customer:
    def __init__(self, customerType, arrivalTime, items, customerNumber):
        self.items = items
        self.customerType = customerType
        self.arrivalTime = arrivalTime
        self.customerNumber = customerNumber

class CustomerA(Customer):
    def enqueCustomer(self, registers):
        currentRegister = registers[0]
        for register in registers:
            if currentRegister.queue.size() == register.queue.size():
                if currentRegister.registerNumber > register.registerNumber:
                    currentRegister = register
            else:
                if currentRegister.queue.size() > register.queue.size():
                    currentRegister = register
        currentRegister.queue.enqueue(self)
        print  "Customer #({customerNumber}) (type A) arrives with ({items}) items and goes to register #{registerNumber}.".format(
            customerNumber = self.customerNumber, items = self.items, registerNumber =currentRegister.registerNumber
        )
        return

class CustomerB(Customer):
    def enqueCustomer(self, registers):
        currentRegister = registers[0]
        for register in registers:
            if register.queue.isEmpty():
                currentRegister = register
                currentRegister.queue.enqueue(self)
                print  "Customer #({customerNumber}) (type B) arrives with ({items}) items and goes to register #{registerNumber}.".format(
                    customerNumber = self.customerNumber, items = self.items, registerNumber =currentRegister.registerNumber
                    )
                return
        for register in registers:
            if register.queue.lastItem():
                if currentRegister.queue.lastItem().items > register.queue.lastItem().items:
                    currentRegister = register
        currentRegister.queue.enqueue(self)
        print  "Customer #({customerNumber}) (type B) arrives with ({items}) items and goes to register #{registerNumber}.".format(
            customerNumber = self.customerNumber, items = self.items, registerNumber =currentRegister.registerNumber
        )
        return

    