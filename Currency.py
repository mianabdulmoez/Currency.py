china_c = input("What do you have left in yuan ? ")
china = int(china_c)
print(china)
japan_c = input("What do you have left in yen ? ")
japan = int(japan_c)
print(japan)
korea_c = input("What do you have left in won ? ")
korea = int(korea_c)
print(korea)
usd_china = int(china / 6.93)
print("Now you have",usd_china,"dollars left from china.")
usd_japan = int(japan / 142.76)
print("Now you have",usd_japan,"dollars left from japan.")
usd_korea = int(korea/ 1376.15)
print("Now you have",usd_korea,"dollars left from korea.")
usd_sum = usd_china + usd_japan + usd_korea
print("Now you have total",usd_sum,"dollars.")