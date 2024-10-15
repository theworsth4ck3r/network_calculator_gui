from helpers import *

def calcNetworkAddress(ipAddress, subnetMask):
	ip_address_bin = decIpToBin(ipAddress)
	subnet_mask_bin = decIpToBin(subnetMask)
	network_address_bin = ''

	for x in range(0, 32):
		network_address_bin += str(int(ip_address_bin[x]) * int(subnet_mask_bin[x]))

	return binIpToDec(network_address_bin)


def calcBroadcastAddress(networkAddress, subnetMask):
	subnetmask_bin = decIpToBin(subnetMask)
	subnetmask_reversed_bin = ''

	for x in range(0, len(subnetmask_bin)):
		if int(subnetmask_bin[x]) == 1:
			subnetmask_reversed_bin += '0'
		else:
			subnetmask_reversed_bin += '1'
	

	subnetmask_reversed_dec = binIpToDec(subnetmask_reversed_bin)

	subnetmask_reversed_dec_arr = subnetmask_reversed_dec.split('.')
	network_address_arr = networkAddress.split('.')

	broadcast_address_arr = []
	for index in range(0, 4):
		broadcast_address_arr.append(
			str(int(subnetmask_reversed_dec_arr[index]) + int(network_address_arr[index]))
			)

	return '.'.join(str(x) for x in broadcast_address_arr)
		

def getMaximumHostsAmount(subnetMask):    
	subnetmask_short = 0
	subnetmask_bin = decIpToBin(subnetMask)

	for x in range(0, len(subnetmask_bin)):
		if int(subnetmask_bin[x]) == 1:
			subnetmask_short += 1

	return pow(2, 32 - subnetmask_short) - 2


def getFirstHostIP(networkAddress):
	network_address_arr = networkAddress.split('.')
	network_address_arr[3] = str(int(network_address_arr[3]) + 1)

	return '.'.join(str(x) for x in network_address_arr)


def getLastHostIP(broadcastAddress):
	broadcast_address_arr = broadcastAddress.split('.')
	broadcast_address_arr[3] = str(int(broadcast_address_arr[3]) - 1)

	return '.'.join(str(x) for x in broadcast_address_arr)


def calculateAll(ipAddress, subnetMask):
    __NETWORK_ADDRESS = calcNetworkAddress(ipAddress, subnetMask)
    __BROADCAST_ADDRESS = calcBroadcastAddress(__NETWORK_ADDRESS, subnetMask)
    __MAXIMUM_HOSTS_AMOUNT = getMaximumHostsAmount(subnetMask)
    __FIRST_HOST_IP = getFirstHostIP(__NETWORK_ADDRESS)
    __LAST_HOST_IP = getLastHostIP(__BROADCAST_ADDRESS)
    
    return __NETWORK_ADDRESS, __BROADCAST_ADDRESS, __MAXIMUM_HOSTS_AMOUNT, __FIRST_HOST_IP, __LAST_HOST_IP