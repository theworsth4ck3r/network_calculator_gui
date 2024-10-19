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

        print(f'''
------------------------------------------------------
{str(getMessage('NETWORK_ADDRESS'))}                            %s
{str(getMessage('BROADCAST_ADDRESS'))}                   %s
{str(getMessage('MAXIMUM_HOSTS'))}             %d
{str(getMessage('FIRST_HOST_IP'))}         %s
{str(getMessage('LAST_HOST_IP'))}         %s
------------------------------------------------------
        ''' % (calculateAll(self.ipAddress, self.subnetMask)))
        
    
    def handleValidationError(self, errorMessage):
        if errorMessage:
            print(errorMessage)
            sys.exit(1)