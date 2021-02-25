def acima_5(quantidade_carne):
    if(quantidade_carne > 5):
        return 0.9
    return 0


def descontado(tipo_pagamento):
    if(tipo_pagamento == 1):
        return 0.95
    return 1


def valor_carnes(tipo_carne):
    if(tipo_carne == "0"):
        return 4.9
    if(tipo_carne == "1"):
        return 5.9
    if(tipo_carne == "2"):
        return 6.9
