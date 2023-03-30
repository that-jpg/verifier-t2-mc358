#!/usr/bin/env python3

def read_file_and_build_hashmap(file_name):
  # create an empty hashmap
  hashmap = {}

  # open the file for reading
  with open(file_name, 'r') as f:
    # iterate over each line in the file
    for line in f:
      # split the line into a tuple of values
      values = line.strip().split(' ')
      if len(values) != 3:
          continue

      hashmap[values[0]+"-"+values[1]] = values[2]
      hashmap[values[1]+"-"+values[0]] = values[2]


  return hashmap

def read_file_and_return_pairs(file_name):
    with open(file_name, 'r') as f:
        numbers = f.readline().strip().split(' ')

    pairs = []
    for i in range(len(numbers) - 1):
        pairs.append((numbers[i], numbers[i+1]))
    return pairs


values = read_file_and_build_hashmap("in")
results = read_file_and_return_pairs("res")

wrong = False;
past_color = None
for edge in results[:-1]:
    if (past_color == None):
        past_color = values[edge[0]+"-"+edge[1]]
    else:
        current_color = values[edge[0]+"-"+edge[1]]
        if current_color == past_color:
            print("caraca muleque; esse pair aqui ta errado", edge)
            wrong = True;
        else:
            past_color = current_color


if not wrong:
    print("""
Melhor assim
Pra que fingir se você já não tem amor
Se os teus desejos já não me procuram mais
Se na verdade, pra você, eu já não sou ninguém

De coração eu só queria que você fosse feliz
Que outro consiga te fazer o que eu não fiz
Que você tenha tudo aquilo que sonhou (que sonhou)

Mas vá embora
Antes que a dor machuque mais meu coração
Antes que eu morra me humilhando de paixão
E me ajoelhe te implorando pra ficar comigo

Não diz mais nada
A dor é minha, eu me aguento, pode crer
Mesmo que eu tenha que chorar pra aprender
Como esquecer você

De coração eu só queria que você fosse feliz
Que outro consiga te fazer o que eu não fiz
Que você tenha tudo aquilo que sonhou (que sonhou)

Mas vá embora
Antes que a dor machuque mais meu coração
Antes que eu morra me humilhando de paixão
E me ajoelhe te implorando pra ficar comigo

Não diz mais nada
A dor é minha, eu me aguento, pode crer
Mesmo que eu tenha que chorar pra aprender
Como esquecer você

Mas vá embora (vá embora)
Antes que a dor machuque mais meu coração (meu coração)
Antes que eu morra me humilhando de paixão (de paixão)
E me ajoelhe te implorando pra ficar comigo

Não diz mais nada
A dor é minha, eu me aguento, pode crer
Mesmo que eu tenha que chorar pra aprender
Como esquecer você
    """)
