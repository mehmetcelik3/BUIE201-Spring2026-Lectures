x = 30
class Telephone:
    x = 10

    print(x)

    def Respond():
        pass
    def Ring():
        pass

Telephone.Respond()
print(x)
print(Telephone.x)
z = Telephone.x
Telephone.x = 20
Telephone.y = 99

t1 = Telephone()
t1.ringtone = "ringtone1"

t2 = Telephone()
t2.ringtone = "ringtone2"

list = []
for t in range(500):
    tel = Telephone()
    list.append(tel)
    tel.ringtone = "ringtone" + str(t)

for tel in list:
    print(tel.ringtone)