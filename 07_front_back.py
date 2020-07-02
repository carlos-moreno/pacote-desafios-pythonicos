"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def divide_string(string):
    if len(string) % 2 == 0:
        a, b = string[:len(string) // 2], string[len(string) // 2:]
    else:
        a, b = string[:(len(string) // 2) + 1], string[(len(string) // 2) + 1:]
    return a, b


def front_back(a, b):
    first = divide_string(a)
    second = divide_string(b)
    return f"{first[0]}{second[0]}{first[1]}{second[1]}"


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = "✅"
        info = ""
    else:
        sign = "❌"
        info = f"e o correto é {expected!r}"

    print(f"{sign} {f.__name__}{in_!r} retornou {out!r} {info}")


if __name__ == "__main__":
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ("abcd", "xy"), "abxcdy")
    test(front_back, ("abcde", "xyz"), "abcxydez")
    test(front_back, ("Kitten", "Donut"), "KitDontenut")
