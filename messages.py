__MESSAGES = {
    'APP_TITLE': 'Kalkulator sieciowy',
    'CALCULATE': 'Oblicz',
    'PASS_IP_ADDRESS': 'Podaj adres IP: ',
    'PASS_SUBNET_MASK_IP_ADDRESS': 'Podaj adres maski podsieci: ',
    
    'NETWORK_ADDRESS': 'Adres sieci',
    'BROADCAST_ADDRESS': 'Adres rozgłoszeniowy',
    'MAXIMUM_HOSTS': 'Maksymalna liczba urządzeń',
    'FIRST_HOST_IP': 'Adres IP pierwszego urządzenia',
    'LAST_HOST_IP': 'Adres IP ostatniego urządzenia'
}


__ERROR_MESSAGES = {
    'INVALID_IP_ADDRESS': 'Nieprawidłowy adres IP',
    'IP_VALIDATION_ERROR': 'Błąd podczas walidacji adresu IP'
}

def getMessage(key):
    return __MESSAGES[key]

def getErrorMessage(key):
    return __ERROR_MESSAGES[key]