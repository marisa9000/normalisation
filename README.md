# normalisation
This repository was written for practice.
It contains files to read in raw text and output the same text, but with the currencies (currency symbols followed by digits) converted into strings.
To run it, run the function "read_and_norm()" with 2 arguments, the input file and the currency table. For example: read_and_norm('input.txt','currency_table.txt')

Limitations: 1.The number normalisation only goes up to a million. 2.The current version can't read fractional currencies, such as 50p. 3.There's no disambiguation for currencies that share the same symbol. So '$' will convert to dollar without specifying whether it's USD, Canadian or any other type of dollar. This becomes a problem in cases where the "$" symbol might refer to Cuban, Colombian, Chilean, Uruguayan and Argentinian pesos, which share the same symbol.
