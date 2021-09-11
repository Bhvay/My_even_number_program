tamil_dishes=["idly","sambar","idiappam"]

Andhra_dishes=["gongoor pickle","dosa","natu kodi chicken"]

karnataka_dishes=["ragimuddha","ragragiidosa"]

kerala_dishes=["putt","avial","aaapam"]

bengali_dishes=["bengali sweets","rasagulla"]

north_indian_dishes=["paratha","naan","roti","chapathi"]
dish=input("enter any dish")
if dish in tamil_dishes:

      print(" It is a tamil dish")
elif dish in Andhra_dishes:
    print("it is a andhra dish")

elif dish in karnataka_dishes:
    print(" it is karnataka dish")
elif dish in kerala_dishes:
    print("it is a kerala dish")
elif dish in north_indian_dishes:
    print("it is a north indian dish")
elif dish in bengali_dishes:
    print("it is a bengali dish")
else:
    print("no dish in any culture")