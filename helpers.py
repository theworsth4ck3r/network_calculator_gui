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
    

# Crates given amount of bits
# Example: 8 -> 1, 2, 4, 8, 16, 32, 64, 128
def getBits(amountBitsToCreate):
	arr = []

	for x in range(0, amountBitsToCreate):
		arr.append(pow(2, x))

	return arr[::-1]


# Takes IP as a binary number and converts it to decimal
# Example: 11000000101010000000000100001010 -> 192.168.1.10
def binIpToDec(ipAddress):
	ipBinArr = []
	bits = getBits(8)

	octs = [
		ipAddress[0:8],
		ipAddress[8:16],
		ipAddress[16:24],
		ipAddress[24:32]
	]

	for octsIndex in range(0, len(octs)):
		octBin = 0
		for singleBinIndex in range(0, len(octs[octsIndex])):
			if int(octs[octsIndex][singleBinIndex]) == 1:
				octBin += int(bits[singleBinIndex])

		ipBinArr.append(octBin)
		octBin = 0

	return '.'.join(str(x) for x in ipBinArr)


# Takes ip address as a string and converts it to binary number
# Example 192.168.1.10 -> 11000000101010000000000100001010
def decIpToBin(ipAddress):
	octs = ipAddress.split('.')

	bits = getBits(8)
	binIpArr = []

	for index in range(0, len(octs)):
		octBin = ""
		total = 0

		for bitIndex in range(0, len(bits)):
			if int(octs[index]) >= (bits[bitIndex] + total):
				total += int(bits[bitIndex])
				octBin += str(1)
			else:
				octBin += str(0)

		binIpArr.append(octBin)

	return ''.join(str(x) for x in binIpArr)

