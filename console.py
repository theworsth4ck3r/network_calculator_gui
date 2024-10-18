from calc_functions import *
from helpers import validateIpAddress
from messages import getMessage

class ConsoleApplication:

    def __init__(self):
        self.ipAddress, self.subnetMask = self.getAndValidateIpAddressAndSubnetMask()        
        self.calculateAndPrintResult()


    def getAndValidateIpAddressAndSubnetMask(self):
        __IP_ADDRESS = (input(getMessage('PASS_IP_ADDRESS'))).strip()
        self.handleValidationError(validateIpAddress(__IP_ADDRESS))

        __SUBNET_MASK_ADDRESS = (input(getMessage('PASS_SUBNET_MASK_IP_ADDRESS'))).strip()
        self.handleValidationError(validateIpAddress(__SUBNET_MASK_ADDRESS))
        
        return __IP_ADDRESS, __SUBNET_MASK_ADDRESS
    

    def calculateAndPrintResult(self):

        print('''
------------------------------------------------------
Adres sieci                            %s
Adres rozgłoszeniowy                   %s
Maksymalna liczba urządzeń             %d
Adres IP pierwszego urządzenia         %s
Adres IP ostatniego urządzenia         %s
------------------------------------------------------
        ''' % (calculateAll(self.ipAddress, self.subnetMask)))
        
    
    def handleValidationError(self, errorMessage):
        if errorMessage:
            print(errorMessage)
            sys.exit(1)