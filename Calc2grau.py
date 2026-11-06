import matplotlib.pyplot as plt
import numpy as np


def calcular_raizes(
    a: float, b: float, c: float
) -> tuple[float, tuple[float | complex, ...]]:
    if a == 0:
        raise ValueError(
            "O coeficiente 'a' deve ser diferente de zero para uma equação de segundo grau."
        )

    delta = (b**2) - (4 * a * c)

    if delta > 0:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        raizes = (x1, x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        raizes = (x1,)
    else:
        parte_real = -b / (2 * a)
        parte_imag = ((-delta) ** 0.5) / (2 * a)
        raizes = (
            complex(parte_real, parte_imag),
            complex(parte_real, -parte_imag),
        )

    return delta, raizes


def plotar_grafico(
    a: float,
    b: float,
    c: float,
    delta: float,
    raizes: tuple[float | complex, ...],
) -> None:
    xv = -b / (2 * a)
    yv = (a * xv**2) + (b * xv) + c

    # Ajusta o domínio do gráfico dinamicamente com base nas raízes ou no vértice
    if delta >= 0:
        valores_x = [float(r) for r in raizes] + [xv]
        margem = max(abs(max(valores_x) - min(valores_x)) * 0.4, 2.0)
        x_min, x_max = min(valores_x) - margem, max(valores_x) + margem
    else:
        x_min, x_max = xv - 5.0, xv + 5.0

    x = np.linspace(x_min, x_max, 400)
    y = (a * x**2) + (b * x) + c

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, label=f"f(x) = {a}x² + {b}x + {c}", color="#1f77b4", lw=2)

    # Eixos cartesianos de referência
    ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)

    # Destaque do vértice
    ax.scatter(
        [xv], [yv], color="#d62728", zorder=5, label=f"Vértice: ({xv:.2f}, {yv:.2f})"
    )

    # Destaque das raízes reais no plano cartesiano
    if delta >= 0:
        for idx, r in enumerate(raizes, start=1):
            ax.scatter(
                [r],
                [0],
                color="#2ca02c",
                zorder=5,
                label=f"Raiz x{idx}: {r:.2f}",
            )

    ax.set_title("Equação de 2º Grau - Análise Gráfica")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    try:
        a = float(input("Coeficiente a: "))
        b = float(input("Coeficiente b: "))
        c = float(input("Coeficiente c: "))

        delta, raizes = calcular_raizes(a, b, c)

        print(f"\nΔ (Delta): {delta:.2f}")
        if delta > 0:
            print(f"Duas raízes reais distintas: x1 = {raizes[0]:.2f}, x2 = {raizes[1]:.2f}")
        elif delta == 0:
            print(f"Raiz real única (dupla): x = {raizes[0]:.2f}")
        else:
            print(f"Raízes complexas: {raizes[0]:.2f} e {raizes[1]:.2f}")

        plotar_grafico(a, b, c, delta, raizes)

    except ValueError as e:
        print(f"Erro de entrada: {e}")


if __name__ == "__main__":
    main()