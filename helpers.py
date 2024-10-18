import sys
import getopt
from messages import getErrorMessage


def isConsoleApplication():
    __IS_CONSOLE_APPLICATION = False

    opts, args = getopt.getopt(sys.argv[1:], "c", ['console'])

    for opt, arg in opts:
        if opt in ('-c', '--console'):
            __IS_CONSOLE_APPLICATION = True
            
    return __IS_CONSOLE_APPLICATION


def validateIpAddress(ipAddress):
    octs = ipAddress.split(".")
    if len(octs) != 4:
        return getErrorMessage('INVALID_IP_ADDRESS')
        
    for singleOct in octs:
        try:
            intSingleOct = int(singleOct)
            if intSingleOct < 0 or intSingleOct > 255:
                return getErrorMessage('INVALID_IP_ADDRESS')
        except ValueError:
            return getErrorMessage('INVALID_IP_ADDRESS')
        except Exception:
            return getErrorMessage('IP_VALIDATION_ERROR')   


# Takes IP as a binary number and converts it to decimal
# Example: 11000000101010000000000100001010 -> 192.168.1.10
def binIpToDec(ipAddress):
	decimalOctetsArr = []

	octs = [
		ipAddress[0:8],
		ipAddress[8:16],
		ipAddress[16:24],
		ipAddress[24:32]
	]
 
	for octet in octs:
		decimalOctetsArr.append(str(int(octet, 2)))
	
	return '.'.join(decimalOctetsArr)


# Takes ip address as a string and converts it to binary number
# Example 192.168.1.10 -> 11000000101010000000000100001010
def decIpToBin(ipAddress):
    octs = ipAddress.split('.')
    binaryIp = ''
    
    for octet in octs:
        binaryIp += f'{int(octet):08b}'
        
    return binaryIp