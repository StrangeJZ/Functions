def area_of_a_circle(value1):
    answer = value1**2 * 3.14
    return answer

area = area_of_a_circle(10)
print(area)
area2 = area_of_a_circle(6)
print(area2)
area3 = area_of_a_circle(24)
print(area3)
area4 = area_of_a_circle(2)
print(area4)
area5 = area_of_a_circle(1)
print(area5)

def totalMoney(value2, value3):
    amountDue = value2 + (value2 * value3)
    return amountDue

amountDue1 = totalMoney(20, 0.06)
print("$ ",amountDue1)
amountDue2 = totalMoney(54, 0.04)
print("$ ",amountDue2)
amountDue3 = totalMoney(68, 0.08)
print("$ ",amountDue3)

def temperature(value4):
    celsius = (value4 - 32) * (5/9)
    return celsius

temperature1 = temperature(32)
print(temperature1, "degrees celsius")
temperature2 = temperature(80)
print(temperature2, "degrees celsius")
temperature3 = temperature(73)
print(temperature3, "degrees celsius")
temperature4 = temperature(42)
print(temperature4, "degrees celsius")
