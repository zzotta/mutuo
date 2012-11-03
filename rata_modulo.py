#!/usr/bin/env python3.2

def calcola_rata(tasso_annuo, numero_rate_anno, numero_rate, capitale_residuo):

    tasso_periodo = (tasso_annuo / numero_rate_anno) / 100
    ani = (1 - pow((1 + tasso_periodo), -numero_rate)) / tasso_periodo
    rata = capitale_residuo / ani

    return rata


def calcola_interessi(tasso_annuo, numero_rate_anno, capitale_residuo):

    tasso_periodo = (tasso_annuo / numero_rate_anno) / 100
    interessi = capitale_residuo * tasso_periodo

    return interessi

if __name__ == "__main__":

    tasso_annuo = 2.95
    numero_rate_anno = 12
    numero_rate = 300
    capitale_residuo = 135000.0

    print(calcola_rata(tasso_annuo, numero_rate_anno,
                       numero_rate, capitale_residuo))

    print(calcola_interessi(tasso_annuo, numero_rate_anno, capitale_residuo))


