class Number:
    def __init__(self, digit):
        self.digit = digit




    def get_basic_num(self, digit):
      units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ]
      teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
              "nineteen", ]
      tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ]

      if digit < 10:
          return units[digit]
      elif 9 < digit < 20:
          digit = digit - 10
          return teens[digit]
      elif 19 < digit < 100:
          if digit % 10 == 0:
            digit = (digit//10) - 2
            return tens[digit]
          elif digit % 10 != 0:
            temp = digit % 10  # extract unit of the two digit value
            digit = (digit // 10) - 2
            return tens[digit] + "-" + units[temp]

    def get_hun(self, digit):
      suffix = ["hundred", "thousand", "million"]
      if 99 < digit < 1000:
          if digit % 100 == 0:
              return self.get_basic_num(digit // 100) + " " + suffix[0]
          elif 0 < digit % 100:
              return self.get_basic_num(digit // 100) + " " + suffix[0] + " and " + self.get_basic_num(digit % 100)


    def get_thou(self, digit):
      suffix = ["hundred", "thousand", "million"]

      if 999 < digit < 100000: #1000 to 100,000
          if digit % 1000 == 0:
              return self.get_basic_num(digit // 1000) + " " + suffix[1]
          elif 0 < digit % 1000 < 100: #1001-1099 to 99,099
              return self.get_basic_num(digit // 1000) + " " + suffix[1] + " and " + self.get_basic_num(digit % 1000)
          elif 99 < digit % 1000 < 1000: #1100 to 99,999
              return self.get_basic_num(digit // 1000) + " " + suffix[1] + " " + self.get_hun(digit % 1000)
      if 99999 < digit < 1000000: # Handles hundreds of thousands
         if digit % 1000 == 0:
             return self.get_hun(digit // 1000) + " " + suffix[1]
         elif 0 < digit % 1000 < 100: # last two digits up to 99
             return self.get_hun(digit // 1000) + " " + suffix[1] + " and " + self.get_basic_num(digit % 1000)
         elif 99 < digit % 1000 < 1000:  # last three digits up to 999
             return self.get_hun(digit // 1000) + " " + suffix[1] + " " + self.get_hun(digit % 1000)

    def get_mill(self, digit):
        suffix = ["hundred", "thousand", "million"]

        if 999999 < digit < 1000000000: # a million to a billion
          #if int(str(digit)[-6:-3])== 0:  #Assuming middle three digits are 0
            if digit % 1000000 == 0:
                return self.get_basic_num(digit // 1000000) + " " + suffix[2]
            elif 0 < digit % 1000000 < 100:  # 1000001-1000099 to 99,099
                return self.get_basic_num(digit // 1000000) + " " + suffix[2] + " and " + self.get_basic_num(digit % 1000000)
            elif 99 < digit % 1000000 < 1000:  #
                return self.get_basic_num(digit // 1000000) + " " + suffix[2] + " " + self.get_hun(digit % 1000000)
            elif 999 < digit % 1000000 < 1000000:
                return self.get_basic_num(digit // 1000000) + " " + suffix[2] + " " +self.get_thou(digit % 1000000)




    def number(self):
        if 0 <= self.digit < 100:
            return self.get_basic_num(self.digit)
        if 99 < self.digit < 1000:
            return self.get_hun(self.digit)
        if 999 < self.digit < 1000000:
            return self.get_thou(self.digit)
        if 999999 < self.digit < 1000000000:
            return self.get_mill(self.digit)





#print(Number(9120461).number())












