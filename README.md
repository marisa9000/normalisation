# normalisation
This repository contains files to read in raw text and output the same text, but with the currencies (currency symbols followed by digits) converted into strings.
To run it, run the function "read_and_norm()" with 2 arguments, the input file and the currency table. For example: read_and_norm('input.txt','currency_table.txt')

Limitations: 
-The number normalisation only goes up to a million.
-The current version can't read fractional currencies, such as 50p.
