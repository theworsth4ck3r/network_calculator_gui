__MESSAGES = {
    'PASS_IP_ADDRESS': 'Podaj adres IP: ',
    'PASS_SUBNET_MASK_IP_ADDRESS': 'Podaj adres maski podsieci: '
}


__ERROR_MESSAGES = {
    'INVALID_IP_ADDRESS': 'Nieprawidłowy adres IP',
    'IP_VALIDATION_ERROR': 'Błąd podczas walidacji adresu IP'
}

def getMessage(key):
    return __MESSAGES[key]

def getErrorMessage(key):
    return __ERROR_MESSAGES[key]