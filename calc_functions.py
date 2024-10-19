from helpers import *

def calcNetworkAddress(ipAddress, subnetMask):
	ipAddressBin = decIpToBin(ipAddress)
	subnetMaskBin = decIpToBin(subnetMask)
	networkAddressBin = ''

	for x in range(0, 32):
		networkAddressBin += str(int(ipAddressBin[x]) * int(subnetMaskBin[x]))

	return binIpToDec(networkAddressBin)


def calcBroadcastAddress(networkAddress, subnetMask):
	subnetmaskBin = decIpToBin(subnetMask)
	reversedSubnetMaskBin = ''

	for x in range(0, len(subnetmaskBin)):
		if int(subnetmaskBin[x]) == 1:
			reversedSubnetMaskBin += '0'
		else:
			reversedSubnetMaskBin += '1'
	

	reversedSubnetMaskDec = binIpToDec(reversedSubnetMaskBin)

	reversedSubnetMaskDec_arr = reversedSubnetMaskDec.split('.')
	networkAddressArr = networkAddress.split('.')

	broadcastAddressArr = []
	for index in range(0, 4):
		broadcastAddressArr.append(
			str(int(reversedSubnetMaskDec_arr[index]) + int(networkAddressArr[index]))
			)

	return '.'.join(str(x) for x in broadcastAddressArr)
		

def getMaximumHostsAmount(subnetMask):    
	subnetMaskShort = 0
	subnetMaskBin = decIpToBin(subnetMask)

	for x in range(0, len(subnetMaskBin)):
		if int(subnetMaskBin[x]) == 1:
			subnetMaskShort += 1

	return pow(2, 32 - subnetMaskShort) - 2


def getFirstHostIP(networkAddress):
	networkAddressArr = networkAddress.split('.')
	networkAddressArr[3] = str(int(networkAddressArr[3]) + 1)

	return '.'.join(str(x) for x in networkAddressArr)


def getLastHostIP(broadcastAddress):
	broadcastAddressArr = broadcastAddress.split('.')
	broadcastAddressArr[3] = str(int(broadcastAddressArr[3]) - 1)

	return '.'.join(str(x) for x in broadcastAddressArr)


def calculateAll(ipAddress, subnetMask):
    __NETWORK_ADDRESS = calcNetworkAddress(ipAddress, subnetMask)
    __BROADCAST_ADDRESS = calcBroadcastAddress(__NETWORK_ADDRESS, subnetMask)
    __MAXIMUM_HOSTS_AMOUNT = getMaximumHostsAmount(subnetMask)
    __FIRST_HOST_IP = getFirstHostIP(__NETWORK_ADDRESS)
    __LAST_HOST_IP = getLastHostIP(__BROADCAST_ADDRESS)
    
    return __NETWORK_ADDRESS, __BROADCAST_ADDRESS, __MAXIMUM_HOSTS_AMOUNT, __FIRST_HOST_IP, __LAST_HOST_IP