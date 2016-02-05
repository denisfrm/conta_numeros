# -*- coding: UTF-8 -*-
import collections


class ContaNumerosExtenso:

    def __init__(self):
        self.mapeamento = collections.OrderedDict([
            [1000, 'mil'],
            [900, 'novecentos'],
            [800, 'oitocentos'],
            [700, 'setecentos'],
            [600, 'seiscentos'],
            [500, 'quinhentos'],
            [400, 'quatrocentos'],
            [300, 'trezentos'],
            [200, 'duzentos'],
            [100, 'cem'],
            [90, 'noventa'],
            [80, 'oitenta'],
            [70, 'setenta'],
            [60, 'sessenta'],
            [50, 'cinquenta'],
            [40, 'quarenta'],
            [30, 'trinta'],
            [20, 'vinte'],
            [19, 'dezenove'],
            [18, 'dezoito'],
            [17, 'dezesete'],
            [16, 'dezeseis'],
            [15, 'quinze'],
            [14, 'quatorze'],
            [13, 'treze'],
            [12, 'doze'],
            [11, 'onze'],
            [10, 'dez'],
            [9, 'nove'],
            [8, 'oito'],
            [7, 'sete'],
            [6, 'seis'],
            [5, 'cinco'],
            [4, 'quadro'],
            [3, 'tres'],
            [2, 'dois'],
            [1, 'um'],
            [0, 'zero'],
        ])

    def numero_por_extenso(self, numero):
        numero = int(float(numero))
        if numero > 999999:
            raise Exception(
                'Nao aceita numero maior que 999999 (%s).' %
                self.numero_por_extenso(999999)
            )
        if numero in self.mapeamento:
            return self.mapeamento[numero]
        for chave in self.mapeamento:
            if chave <= numero:
                total = []
                quantos_mil = 1
                if chave == 100:
                    total = ['cento']
                else:
                    if chave == 1000:
                        quantos_mil = numero / chave
                        if quantos_mil > 1:
                            total.append(
                                self.numero_por_extenso(quantos_mil) + ' '
                            )
                    total.append(self.numero_por_extenso(chave))
                resto = numero - (chave * quantos_mil)
                if resto:
                    if chave != 1000:
                        total.append(' e')
                    total.append(' ' + self.numero_por_extenso(resto))
                return ''.join(total)
        raise Exception('Erro ao tentar escrever o numero ' + str(numero))

    def antecessores_por_extenso(self, numero):
        return ''.join(
            [self.numero_por_extenso(num) for num in range(1, numero + 1)]
        )

    def tamanho_antecessores_por_extenso(self, numero):
        return len(self.antecessores_por_extenso(numero))
