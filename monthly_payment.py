# FORMELN
# Formeln för månatlig avbetalning lyder: A = (P * r(1+r)^n) / ((1 + r)^n - 1). 
# A = avbetalning per månad i kronor
# P = totala lånebeloppet
# r = räntan per period (t.ex. om räntan är 9% blir det r = 0.09 / 12)
# n = totalt antal betalningsperioder

def calculate_monthly_payment(principal, annual_rate, years): 
    # räntan per period (t.ex. om räntan är 9% blir det r = 0.09 / 12)
    mounthly_rate = (annual_rate / 100) / 12
    month = years * 12
    # monthly payment
    return (principal * mounthly_rate * (1 + mounthly_rate) ** month) / ((1 + mounthly_rate) ** month - 1)


principal = float(input("Lånebelopp: ")) 
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))

payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")

# 100000, 0.05, 30
# return (principal * (mounthly_rate * (1 + mounthly_rate)**month)) / ((1 + mounthly_rate)**month - 1)