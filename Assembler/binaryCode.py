#Project6 code

class Code:

    def __init__(self):
        pass

    def get_binary_command(self,command:list) -> str:
        '''translates to binary command'''
        if command == []:
            return ''
        result = ''
        if command[0] == 'A':
            result = '0' + f'{int(command[1]):015b}'
        elif command[0] == 'C':
            result = '111'
            result += self.get_comp_bin(command[2])
            result += self.get_dest_bin(command[1])
            result += self.get_jump_bin(command[3])
        return result
    
    def get_dest_bin(self, dest:str) -> str:
       options = {
           '': '000',
           'M': '001',
           'D': '010',
           'MD': '011',
           'A': '100',
           'AM': '101',
           'AD': '110',
           'AMD': '111'
       }
       return options.get(dest, '')

    def get_comp_bin(self, comp:str) -> str:
       aEQ0 = {
           '0': '101010',
           '1': '111111',
           '-1': '111010',
           'D': '001100',
           'A': '110000',
           '!D': '001101',
           '!A': '110001',
           '-D': '001111',
           '-A': '110011',
           'D+1': '011111',
           'A+1': '110111',
           'D-1': '001110',
           'A-1': '110010',
           'D+A': '000010',
           'D-A': '010011',
           'A-D': '000111',
           'D&A': '000000',
           'D|A': '010101'
       }
       aEQ1 = {
           'M': '110000',
           '!M': '110001',
           '-M': '110011',
           'M+1': '110111',
           'M-1': '110010',
           'D+M': '000010',
           'D-M': '010011',
           'M-D': '000111',
           'D&M': '000000',
           'D|M': '010101'
       }
       a0 = aEQ0.get(comp, '')
       a1 = aEQ1.get(comp, '')
       if a0 == '':
           if a1 == '':
               return ''
           return '1' + a1
       return '0' + a0

    def get_jump_bin(self, jump:str) -> str:
       options = {
           '': '000',
           'JGT': '001',
           'JEQ': '010',
           'JGE': '011',
           'JLT': '100',
           'JNE': '101',
           'JLE': '110',
           'JMP': '111'
       }
       return options.get(jump, '')





