import numpy as np
import matplotlib.pyplot as plt

# Funkcja reprezentująca równanie różniczkowe cząstkowe: u_xx = f(x)
def funkcja_pochodna_przestrzenna(x):
    return x**2

# Metoda różnic skończonych dla równania różniczkowego cząstkowego
def metoda_roznic_skonczonych(f, a, b, n):
    h = (b - a) / (n + 1)
    x = np.linspace(a, b, n + 2)
    
    # Macierz układu równań
    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(1, n + 1):
        A[i - 1, i - 1] = -2
        if i > 1:
            A[i - 1, i - 2] = 1
        if i < n:
            A[i - 1, i] = 1
        b[i - 1] = h**2 * f(x[i])
    
    # Rozwiązanie układu równań
    u = np.linalg.solve(A, b)
    
    # Dodanie warunków brzegowych
    u = np.concatenate(([0], u, [0]))
    
    return x, u

# Parametry
a, b = 0, 1  # Przedział [a, b]
n = 100  # Liczba podziałów przestrzeni

# Wywołanie metody różnic skończonych
x, wyniki = metoda_roznic_skonczonych(funkcja_pochodna_przestrzenna, a, b, n)
print(x)
print(wyniki)

# Wykres wyników
plt.plot(x, wyniki, label='Rozwiązanie')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Rozwiązanie równania różniczkowego cząstkowego u_xx = x^2')
plt.legend()
plt.show()
