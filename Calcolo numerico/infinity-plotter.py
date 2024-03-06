import matplotlib.pyplot as plt

function = str(input("Inserisci la funzione: "))


def f(x, function):
    return eval(function)


x = list(range(-100, 101))
y = []
count = 0
nondomain = []
while count < len(x):
    try:
        for i in x:
            if i not in nondomain:
                y.append(f(i, function))
            else:
                y.append(None)
        count = len(y + nondomain)
    except ZeroDivisionError:
        print(f"Punto di discontinuità all\'ascissa x = {i}")
        nondomain.append(i)
        y = []
plt.grid(True)
plt.plot(x, y)
plt.show()
