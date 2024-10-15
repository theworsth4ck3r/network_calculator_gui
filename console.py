from calc_functions import *
from helpers import validateIpAddress
from messages import __MESSAGES

class ConsoleApplication:

    def __init__(self):
        self.ipAddress, self.subnetMask = self.getAndValidateIpAddressAndSubnetMask()        
        self.calculateAndPrintResult()


    def getAndValidateIpAddressAndSubnetMask(self):
        __IP_ADDRESS = (input(__MESSAGES['PASS_IP_ADDRESS'])).strip()
        self.handleValidationError(validateIpAddress(__IP_ADDRESS))

        __SUBNET_MASK_ADDRESS = (input(__MESSAGES['PASS_SUBNET_MASK_IP_ADDRESS'])).strip()
        self.handleValidationError(validateIpAddress(__SUBNET_MASK_ADDRESS))
        
        return __IP_ADDRESS, __SUBNET_MASK_ADDRESS
    

    def calculateAndPrintResult(self):

        print('''
------------------------------------
Network address      %s
Broadcast address    %s
Maximum hosts        %d
First host IP        %s
Last host IP         %s
------------------------------------
        ''' % (calculateAll(self.ipAddress, self.subnetMask)))
        
    
    def handleValidationError(self, errorMessage):
        if errorMessage:
            print(errorMessage)
            sys.exit(1)