x = 10
def f():
    x = 15

    def g(x):
        w = x + 12
        print(w)

    g(x)
    f()

f()
print