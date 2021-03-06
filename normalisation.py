# -*- coding: utf-8 -*-
import re
import number_norm
import currency_norm


class Money:
  def __init__(self, amount):
    self.amount = amount #I think this can be deleted
    self.full_amount = amount  #amount with currency symbol



  def dollars(self,amount): # l.h.s of amount, so '10.10' becomes '10.00'
    pattern = r"[0-9]{1,6}\.00"  # up to six figures

    curr = currency_norm.Currency(self.full_amount)

    currency = curr.get_currency()
    if type(currency) is tuple:
      currency = currency[0]


    if re.match(pattern, amount)  and float(amount) > 0:
      amount = amount.split(".") #amount becomes a list like ['10','00']


      x = amount[0]
      q = number_norm.Number(int(x))
      y = q.number()
      return y + " " + currency
    else:
      print("Error: invalid amount.")


  def cents(self, amount):
    pattern0 = r"[0-9]"

    if not re.match(pattern0,self.full_amount[0]): # checking that full amount starts with symbol
      curr = currency_norm.Currency(self.full_amount)
      currency = curr.get_currency()[0]  #<--unclear why this index is needed  #get main currency name
      fraction = curr.get_currency()[1]  #<--unclear why this index is needed #get fractional currency amount
    elif re.match(pattern0, self.full_amount[0]):
      print("Can't read in only fractional units yet")
      #TODO: read return values for amounts given in fractional units only.



    pattern = r"\.[0-9][0-9]"

    if re.match(pattern, amount) and int(amount[1:]) > 0:
      amount = int(amount[1:])
      q = number_norm.Number(amount)
      y = q.number()

      if amount > 0:
        return y +" " + fraction
      else:
        return "no value found"



  def currency(self):
    pattern = r"[0-9]"

    if self.full_amount[-3] != '.' and not re.match(pattern, self.full_amount[0]):
      self.full_amount = self.full_amount + '.00'
      if ',' in self.full_amount:
        self.full_amount = self.full_amount.replace(',', '')

      self.amount = self.full_amount[1:]   # amount where currency symbol is stripped away
      self.amount = self.amount.split(".")
      self.amount[0] = self.amount[0] + ".00"
      self.amount[1] = "." + self.amount[1]


    cent = str(self.cents(self.amount[1]))
    dollar = str(self.dollars(self.amount[0]))

    if float(self.amount[0]) > 0 and float(self.amount[1]) > 0:  # dollar and cent are plural
      cent = str(self.cents(self.amount[1]))
      return dollar + " and " + cent
    elif float(self.amount[0]) > 0 and float(self.amount[1]) == 0: # no cent value to return
      return dollar
    elif float(self.amount[0]) > 0 and float(self.amount[1]) == 1: # one cent value to return
      return dollar + " and " + cent

    elif float(self.amount[0]) == 0 and float(self.amount[1]) > 0: #no dollar value to return
      return cent

#x = Money("£9,000") #€

#print(x.currency())


