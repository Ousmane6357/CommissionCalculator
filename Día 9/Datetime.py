from datetime import datetime


despierta = datetime(2022, 12, 23, 7, 50)
duerme = datetime(2022, 6, 10, 12, 34)

vigila = duerme - despierta

print(vigila)
