import pprint
import normalisation
import re


def curr_symbols(file):
  my_list = []

  with open(file, 'r') as f1:
    for line in f1:
      words = line.split(',')
      my_list.append((words[0],words[1:]))
    x = [my_list[i][1][0] for i in range(len(my_list))]
    return x


def read_and_norm(file1,file2):

  pattern = r"[0-9]"
  my_list = curr_symbols(file2)

  with open(file1, 'r') as f1:
    tokens = []
    for line in f1:
      line = line.strip()

      i=0
      for j in range(len(line)):
        if line[j] == " ":
          tokens.append(line[i:j])
          i=j
      tokens.append(line[i:])

  k=[]
  for i in tokens:
    l = i.strip()
    k.append(l)

  for i in range(len(k)):
    if len(k[i]) > 0:
      if k[i][0] in my_list and re.match(pattern, k[i][1]):
        x = normalisation.Money(k[i])
        j = x.currency()
        k[i] = j

      else:
        pass
  k = ' '.join(k)
  pprint.pprint(k)





read_and_norm('input.txt','currency_table.txt')


#x = Money("$90000.10")

#print(x.currency())

