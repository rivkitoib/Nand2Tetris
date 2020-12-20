#Project6 main

import sys

from symbolTable import *
from myParser import *
from binaryCode import *

fileName = sys.argv[1]
_parser = Parser(fileName, True)
symbol_table = Symbol_Table()
code = Code()


#Read the lables:
HasLine = _parser.advance()
while HasLine:
    parsedCommand =  _parser.get_parsed_command()
    if parsedCommand != []:
        symbol_table.add_Entry(parsedCommand[1], parsedCommand[2])
    HasLine = _parser.advance()

#init
index = fileName.find('.asm')
out_name = fileName[:index] + '.hack'
out_file = open(out_name, 'w')
#new _parser
_parser = Parser(fileName, False)


#second loop - translate to binary:
counter = 16
HasLine = _parser.advance()
while HasLine:
    parsedCommand =  _parser.get_parsed_command()
    if parsedCommand != []:
        if parsedCommand[0] == 'A' and not parsedCommand[1].isnumeric():
            if symbol_table.Is_Contains(parsedCommand[1]):
                parsedCommand[1] = symbol_table.get_Address(parsedCommand[1])
            else:
                symbol_table.add_Entry(parsedCommand[1],counter)
                parsedCommand[1] = counter
                counter += 1
        commandInBinary = code.get_binary_command(parsedCommand)
        out_file.write(commandInBinary + '\n')
    HasLine = _parser.advance()
out_file.close()
print("finished---")

