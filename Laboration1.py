#  k = P + (a+1)Pr/2 formel som skall användas.
# P = lånade beloppet, r = årliga räntesatsen, a = antal år för återbetalning. 


P, r, a = int(input('skriv in lånade beloppet ')), float(input("Skriv in den årliga räntesatsen ")), int(input("skriv in antal år för återbetalning "))

k = P + (a + 1)*(P*r)/2


myåterbetalning = "Efter {} år med en {} årlig räntesats och ett start lånebelopp på {} så blir den totala kostnaden {}"

print(myåterbetalning.format(a, r, P, k))
