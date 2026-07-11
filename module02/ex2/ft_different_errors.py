#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    """Função simuladora de falhas comuns em pipelines de dados agrícolas."""
    if operation_number == 0:
        int("abc")  # Erro de conversão de dados
    elif operation_number == 1:
        10 / 0  # Erro de divisão (ex: cálculo de médias sem dados)
    elif operation_number == 2:
        open("non/existent/file")  # Erro de leitura de configuração/logs
    elif operation_number == 3:
        "text" + 5  # Erro de tipagem dinâmica em tempo de execução
    else:
        return


def test_error_types() -> None:
    # Testando cada operação individualmente dentro de blocos try-except
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
            if op == 4:
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
