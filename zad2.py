import matplotlib.pyplot as plt


def f(x):
    return 3 * (x ** 2) - 2 * x + 5


def gradient(x):
    return 6 * x - 2


liczba_iteracji = 6
x = 10
x_do_wykresu = [x]
y_do_wykresu = [f(x)]
podpisy = range(0, liczba_iteracji + 1)
print(f"Iteracja 0: x = {x}, y = {f(x)}")

for i in range(1, liczba_iteracji + 1):
    eta = 1 / (2 ** i)
    x -= eta * gradient(x)
    x_do_wykresu.append(x)
    y_do_wykresu.append(f(x))
    print(f"Iteracja {i}: x = {round(x, 3)}, y = {round(f(x), 3)}")

dziedzina = range(-100, 101)
przeciwdziedzina = []
for element in dziedzina:
    przeciwdziedzina.append(f(element))

plt.plot(dziedzina, przeciwdziedzina)
for indeks, tekst in enumerate(podpisy):
    plt.annotate(tekst, (x_do_wykresu[indeks], y_do_wykresu[indeks]))

plt.scatter(x_do_wykresu, y_do_wykresu, edgecolors=(0, 0, 0))
plt.show()
