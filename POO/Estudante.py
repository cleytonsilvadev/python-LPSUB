class Estudante:
 def __init__(self, nome_completo, nome, origem, tipo, nivel_dificuldade):
   self.nome_completo = nome_completo
   self.nome = nome
   self.origem = origem
   self.tipo = tipo
   self.nivel_dificuldade = nivel_dificuldade

maria = Estudante('Maria dos Santos', 'Mari', 'Trabalha', 'Maga', 2)
print( maria.nome_completo + "\n" + maria.origem + "\n" + maria.tipo)
