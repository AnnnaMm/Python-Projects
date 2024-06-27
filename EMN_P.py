import numpy as np
import matplotlib.pyplot as plt

# Parametry siatki
Nx = 50  
Ny = 50  
Lx = 1.0  
Ly = 1.0 

# Tworzenie siatki
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
X, Y = np.meshgrid(x, y)

# Warunki brzegowe
u_top = np.sin(np.pi * x / Lx)  # Przykładowe warunki brzegowe
u_bottom = np.zeros(Nx)
u_left = np.zeros(Ny)
u_right = np.zeros(Ny)

# Inicjalizacja funkcji u
u = np.zeros((Ny, Nx))

# Implementacja metody różnic skończonych dla równania Poissona
def solve_poisson(u, f, dx, dy, maxiter=1000, tol=1e-4):
    for _ in range(maxiter):
        u_new = u.copy()
        for i in range(1, Ny - 1):
            for j in range(1, Nx - 1):
                u_new[i, j] = 0.25 * (u[i - 1, j] + u[i + 1, j] + u[i, j - 1] + u[i, j + 1] - dx ** 2 * dy ** 2 * f[i, j])
        diff = np.linalg.norm(u_new - u)
        if diff < tol:
            break
        u = u_new
    return u

# Zdefiniowanie funkcji  f(x, y)
def source_function(x, y):
    return np.sin(x) + np.cos(y)  # Przykładowa funkcja 

# Rozwiązanie równania Poissona
f = source_function(X, Y)
u = solve_poisson(u, f, dx, dy)

# Wizualizacja rozwiązania
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x, y)')
ax.set_title('Rozwiązanie równania Poissona: ∇^2 u = sin(x) + cos(y)')
plt.show()


