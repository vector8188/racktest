from register import Register
from customer import CustomerA, CustomerB
from cashier import  Cashier, Trainee


def run():
    with open('input.txt', 'r') as f:
        simulationData = f.readlines()

    numberOfRegisters = int(simulationData[0].strip('\n'))
    del(simulationData[0])
    registers = []
    for i in range(numberOfRegisters):
        if i == numberOfRegisters - 1:
            trainee = Trainee(i)
            registers.append(Register(i, trainee))
        else:
            cashier = Cashier(i)
            registers.append(Register(i, cashier))
    print "Simulation starts with {register} registers; #{register} is a training register.".format(register=numberOfRegisters) 

    CustomerNumber = 1
    for customerData in simulationData:
        customerEntry = customerData.strip('\n').split(' ')
        customerType = customerEntry[0]
        customerArrival = int(customerEntry[1])
        customerItems = int(customerEntry[2])
        if customerType == 'A':
            customer = CustomerA(customerType, customerArrival, customerItems, CustomerNumber)
        else:
            customer = CustomerB(customerType, customerArrival, customerItems, CustomerNumber)
        customer.enqueCustomer(registers)
        CustomerNumber = CustomerNumber + 1
    
    
    for register in registers:
        for item in range(register.queue.size()):
            if not register.queue.isEmpty():
                customer = register.queue.dequeue()
                ProcessingTime = register.customerProcessingTime(register.cashier, customer)
        


if __name__ == "__main__":
    run()