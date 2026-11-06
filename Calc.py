def calcular(a: float, b: float, operacao: str) -> float:
    match operacao:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            return a / b
        case _:
            raise ValueError(f"Operador inválido: '{operacao}'. Escolha entre +, -, * ou /.")


def main() -> None:
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Operação (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))

        resultado = calcular(num1, num2, operacao)
        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except ZeroDivisionError as e:
        print(f"Erro matemático: {e}")


if __name__ == "__main__":
    main()