def calcular_custo_estufa(potencia_w, horas_dia, preco_kwh):
    consumo_mensal_kwh = (potencia_w * horas_dia * 30) / 1000
    custo_bruto = consumo_mensal_kwh * preco_kwh
    custo_final = custo_bruto * 1.1
    return round(custo_final, 2)

if __name__ == "__main__":
    pot = int(input("Potência (W): "))
    hor = int(input("Horas por dia: "))
    prec = float(input("Preço (R$/kWh): "))
    total = calcular_custo_estufa(pot, hor, prec)
    print(f"R$ {total}")