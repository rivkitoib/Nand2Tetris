#Project 6 - Symbol Table

class Symbol_Table:
    def __init__(self):
        self.table={}
        for i in range(16):
            self.table['R'+str(i)]=i
        self.table.update({
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        })

    def add_Entry(self,newSymbol:str,numAdress:int):
        '''insert new pair for the table'''
        self.table.update({newSymbol:numAdress})

    def Is_Contains(self,key:str)->bool:
        '''return if the table contains the key or not'''
        result = self.table.get(key,-1);
        return result != -1

    def get_Address(self,key:str)->int:
        '''get the address of a key'''
        return self.table.get(key, -1)


