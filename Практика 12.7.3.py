money = int(input ("Сумма инвестиций:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())
TKB = round(procent[0]/100*money)
CKB = round(procent[1]/100*money)
VTB = round(procent[2]/100*money)
SBER = round(procent[3]/100*money)
deposit = [TKB, CKB, VTB, SBER]
print("Накопленные средства за год:", deposit)
max_deposit = max(deposit)
print("Максимальная сумма дохода: ", max_deposit)