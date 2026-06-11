from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Agua de coco', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 2.0, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)


def main():
    restaurante_praca.exibir_Cardapio

if __name__ == '__main__':
    main()