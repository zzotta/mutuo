#!/usr/bin/env python3.2

import rata_modulo

numero_rate_anno = 12
numero_rate = 300
capitale_residuo = 135000.0

rate = []
interessi = []
quote_capitale = []

tassi = []
tassi = tassi + ([2.95] * 24) + ([4.00] * 276)

for rata_num in range(numero_rate):

    interesse = rata_modulo.calcola_interessi(tassi[rata_num], numero_rate_anno,
                                              capitale_residuo)

    rata = rata_modulo.calcola_rata(tassi[rata_num], numero_rate_anno,
                                    numero_rate, capitale_residuo)

    quota_capitale = rata - interesse

    capitale_residuo = capitale_residuo - quota_capitale

    numero_rate = numero_rate - 1

    rate.append(rata)
    interessi.append(interesse)
    quote_capitale.append(quota_capitale)


#print(rate)
print(sum(interessi))
#print(quote_capitale)

numero_rate_anno = 12
numero_rate = 300
capitale_residuo = 135000.0

rate = []
interessi = []
quote_capitale = []

tassi = []
tassi = tassi + ([2.95] * 24) + ([4.00] * 276)

for rata_num in range(numero_rate):

    interesse = rata_modulo.calcola_interessi(6.2, numero_rate_anno,
                                              capitale_residuo)

    rata = rata_modulo.calcola_rata(6.2, numero_rate_anno,
                                    numero_rate, capitale_residuo)

    quota_capitale = rata - interesse

    capitale_residuo = capitale_residuo - quota_capitale

    numero_rate = numero_rate - 1

    quote_capitale.append(quota_capitale)

numero_rate_anno = 12
numero_rate = 300
capitale_residuo = 135000.0

rate = []
interessi = []
#quote_capitale = []

tassi = []
tassi = tassi + ([2.95] * 24) + ([4.00] * 276)

for rata_num in range(numero_rate):

    interesse = rata_modulo.calcola_interessi(tassi[rata_num], numero_rate_anno,
                                              capitale_residuo)

    rata = rata_modulo.calcola_rata(tassi[rata_num], numero_rate_anno,
                                    numero_rate, capitale_residuo)

    capitale_residuo = capitale_residuo - quote_capitale[rata_num]

    numero_rate = numero_rate - 1

    rate.append(rata)
    interessi.append(interesse)

print(sum(interessi))

