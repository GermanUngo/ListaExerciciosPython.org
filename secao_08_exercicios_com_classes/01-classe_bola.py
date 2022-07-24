#EXERCICIO 1...

#Classe Bola: Crie uma classe que modele uma bola:

#Atributos: Cor, circunferência, material Métodos: trocaCor e mostraCor

class CirculoPerfeito:
  def __init__(self):
    self.cor = 'Azul'
    self.circunferencia = 4
    self.material = 'Papel'

  def mostra_cor(self):
    return id(self)
  
  def trocar_cor(self, cor):
    self.cor = cor



circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

print(type(circulo_primeiro))
print( circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())
circulo_segundo.cor = 'Amarelo'
print(circulo_primeiro.cor, circulo_segundo.cor)

