# http://strftime.org/ for more information
from datetime import datetime

delta = datetime.now() - datetime(1900,12,31)
print("Delta days:", delta.days)

then = datetime(1900, 12, 31, 20, 12, 59, 83845)
now = datetime.now()
dif = then-now
print("Difference between then and now:", dif)

whenever = datetime.strptime("2017-12-31" , "%Y-%m-%d")

print("Whenever:", whenever)
print("Whenever:", whenever.strftime("%m:%d:%Y"))
