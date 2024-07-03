'''
Faça um programa para calcular o preço de venda fnal de um produto. Para tal solicita, através da linha de
comandos (shell), o preço do produto, o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um
desconto a aplicar ao valor fnal do produto. O programa deverá dar instruções ao utilizador de como deve
ser invocado. O valor do IVA e do desconto deve ser dado em percentagem.
_______________________________

Nesta versão:
    - preço e restantes parametros são obtidos a partir da entrada padrão /
        standard input (ie, por via do input)
    - desconto não é opcional
    - tambem vamos ignorar "o programa deverá dar instruções ao utilizador
        de como deve ser invocado."
'''

from decimal import Decimal as dec

preco = dec(input("Preço : "))
taxa_iva = dec(input("Taxa de IVA (%) : "))
desconto = dec(input("Desconto (%) : "))

preco_final = preco * (1 + taxa_iva / 100) * (1 - desconto / 100)

print(f"Preço final : {preco_final:.2f}")

