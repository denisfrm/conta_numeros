# -*- coding: UTF-8 -*-
import unittest
from conta_numeros_extenso import ContaNumerosExtenso
conta = ContaNumerosExtenso()


class TestContaNumerosExtenso(unittest.TestCase):

    def test_numero_por_extenso_zero(self):
        assert conta.numero_por_extenso(0) == 'zero'

    def test_numero_por_extenso_converte_float(self):
        self.assertEquals(conta.numero_por_extenso(3.20), 'tres')

    def test_numero_por_extenso_converte_str(self):
        self.assertEquals(conta.numero_por_extenso('8.20'), 'oito')

    def test_numero_por_extenso_invalido(self):
        self.assertRaises(Exception, conta.numero_por_extenso, 'foo')

    def test_numero_por_extenso_negativo_invalido(self):
        self.assertRaises(Exception, conta.numero_por_extenso, -1)

    def test_numero_por_extenso_maior_ou_igual_um_milhao_invalido(self):
        self.assertRaises(Exception, conta.numero_por_extenso, 1000000)

    def test_1_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(1), 'um')

    def test_5_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(5), 'cinco')

    def test_20_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(20), 'vinte')

    def test_21_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(21), 'vinte e um')

    def test_100_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(100), 'cem')

    def test_102_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(102), 'cento e dois')

    def test_119_numero_por_extenso(self):
        self.assertEquals(conta.numero_por_extenso(119), 'cento e dezenove')

    def test_122_numero_por_extenso(self):
        self.assertEquals(
            conta.numero_por_extenso(122),
            'cento e vinte e dois'
        )

    def test_1131_numero_por_extenso(self):
        self.assertEquals(
            conta.numero_por_extenso(1131),
            'mil cento e trinta e um'
        )

    def test_2131_numero_por_extenso(self):
        self.assertEquals(
            conta.numero_por_extenso(2131),
            'dois mil cento e trinta e um'
        )

    def test_1221_numero_por_extenso(self):
        self.assertEquals(
            conta.numero_por_extenso(1221),
            'mil duzentos e vinte e um'
        )

    def test_19531_numero_por_extenso(self):
        self.assertEquals(
            conta.numero_por_extenso(19531),
            'dezenove mil quinhentos e trinta e um'
        )

    def test_1_antecessores_por_extenso(self):
        self.assertEquals(conta.antecessores_por_extenso(1), 'um')

    def test_3_antecessores_por_extenso(self):
        self.assertEquals(conta.antecessores_por_extenso(3), 'umdoistres')

    def test_5_antecessores_por_extenso(self):
        self.assertEquals(
            conta.antecessores_por_extenso(5),
            'umdoistresquadrocinco'
        )

    def test_26_antecessores_por_extenso(self):
        self.assertEquals(
            conta.antecessores_por_extenso(26),
            'umdoistresquadrocincoseisseteoitonovedezonzedozetrezequatorze'
            'quinzedezeseisdezesetedezoitodezenovevintevinte e umvinte e '
            'doisvinte e tresvinte e quadrovinte e cincovinte e seis'
        )

    def test_1_tamanho_antecessores_por_extenso(self):
        self.assertEquals(conta.tamanho_antecessores_por_extenso(1), len('um'))

    def test_3_tamanho_antecessores_por_extenso(self):
        self.assertEquals(
            conta.tamanho_antecessores_por_extenso(3),
            len('umdoistres')
        )

    def test_5_tamanho_antecessores_por_extenso(self):
        self.assertEquals(
            conta.tamanho_antecessores_por_extenso(5),
            len('umdoistresquadrocinco')
        )

    def test_26_tamanho_antecessores_por_extenso(self):
        self.assertEquals(
            conta.tamanho_antecessores_por_extenso(26),
            len(
                'umdoistresquadrocincoseisseteoitonovedezonzedozetrezequator'
                'zequinzedezeseisdezesetedezoitodezenovevintevinte e umvinte'
                ' e doisvinte e tresvinte e quadrovinte e cincovinte e seis'
            )
        )

    def test_19531_tamanho_antecessores_por_extenso(self):
        self.assertEquals(
            conta.tamanho_antecessores_por_extenso(19531),
            629574
        )

if __name__ == '__main__':
    unittest.main()
