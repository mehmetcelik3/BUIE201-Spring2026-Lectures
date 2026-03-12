y = 30
class Telephone:
    x = 10

    print(x)

    def Respond():
        pass
    def Ring():
        pass

Telephone.Respond()
print(Telephone.x)
z = Telephone.x
Telephone.x = 20

t1 = Telephone()
t1.ringtone = "ringtone1"

t2 = Telephone()

for t in range(500):
    t = Telephone()
    t.ringtone = "ringtone" + str(t)