# -*- coding: utf-8 -*-



# function to read in given amount, extract currency symbol, look it up in the currency lexicon
# and return the currency name
class Currency:
    def __init__(self, amount):
      self.amount = amount

      if self.amount[-3] != '.':
        self.amount = self.amount + '.00'

      if ',' in self.amount:
        self.amount = str(self.amount).replace(',', '')



    def read_curr(self):
        file = 'currency_table.txt'
        currency_dict = {}

        with open(file, 'r') as f:
            for line in f:
                line = line.split(',')
                index = line[0]
                symbol = line[1]
                currency = line[2],line[4]
                fraction = line[3],line[5]
                currency_dict[index] = symbol, currency, fraction



        return currency_dict


    def get_currency(self):
        currency_dict = self.read_curr()

        for key in currency_dict:
           if currency_dict[key][0] != str(self.amount[0]):
               pass
           else:
               x =str(self.amount).split('.')
               k = int(x[0][1:])   # currency amount as int
               q = int(x[1])       # fraction amount as int

               if k > 1 and q > 1:
                 curr = currency_dict[key][1][1]
                 fract = currency_dict[key][2][1]
                 return curr, fract
               elif k == 1 and q == 1:
                 curr = currency_dict[key][1][0]
                 fract = currency_dict[key][2][0]
                 return curr, fract
               elif k >1 and q == 1:
                 curr = currency_dict[key][1][1]
                 fract = currency_dict[key][2][0]
                 return curr, fract
               elif k == 1 and q > 1:
                 curr = currency_dict[key][1][0]
                 fract = currency_dict[key][2][1]
                 return curr, fract
               elif k > 1 and q == 0:
                   curr = currency_dict[key][1][1]
                   return curr








#curr = Currency('£200.00')
#curr = Currency('50p') #TODO: read in fractional units only

#print(curr.get_currency())
#print(curr.read_curr())
