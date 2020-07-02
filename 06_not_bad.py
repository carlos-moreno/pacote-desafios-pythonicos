import re

"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""


def find_pattern(s):
    regex = r".?not.*.?bad?"
    matches = re.finditer(regex, s)
    pattern = [(match.start(), match.end()) for match in matches]
    return pattern


def not_bad(s):
    if find_pattern(s):
        start, end = find_pattern(s)[0]
        s = s.replace(s[start:end], " good")
    return s


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = "✅"
        info = ""
    else:
        sign = "❌"
        info = f"e o correto é {expected!r}"

    print(f"{sign} {f.__name__}({in_!r}) retornou {out!r} {info}")


if __name__ == "__main__":
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, "This movie is not so bad", "This movie is good")
    test(not_bad, "This dinner is not that bad!", "This dinner is good!")
    test(not_bad, "This tea is not hot", "This tea is not hot")
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, "This movie is not not not so bad", "This movie is good")
    test(not_bad, "The car is bad or not", "The car is bad or not")
