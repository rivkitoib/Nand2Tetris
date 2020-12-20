#Project6 Parser

class Parser:
    def __init__(self,fileName:str,labelsMode:bool):
        try:
            self.file= open(fileName)
        except:
            print('ERROR - could not open the file: ' + fileName)
        self.hasMoreCommands = True
        self.currentCommand = None
        self.commandCounter = 0
        self.labelsMode = labelsMode

    def advance(self) -> bool:
        command = self.file.readline()
        if command == '':
            self.hasMoreCommands = False
            self.file.close()
        self.currentCommand = command
        if command != '':
            self.strip_command()
        return self.hasMoreCommands

    def strip_command(self):
        command = self.currentCommand
        commentIndex = command.find('//')
        if commentIndex != -1:
            command = command[:commentIndex]
        if command == '':
            self.currentCommand = ''
            return
        striped = ''
        for i in range(len(command)):
            if command[i] not in (' ', '\t','\n'):
                striped += command[i]
        self.currentCommand = striped
    def get_parsed_command(self) ->list:
        commandList =[]
        cType = self.get_command_type()
        commandList.append(cType)
        if self.labelsMode:
            if cType == 'LABEL':
                index = self.currentCommand.find(')')
                commandList.append(self.currentCommand[1:index].strip())
                commandList.append(self.commandCounter)
                return commandList
            else:
                return []
        if cType == 'A':
           commandList.append(self.currentCommand[1:].strip())
        elif cType == 'C':
            commandList.append(self.get_dest())
            commandList.append(self.get_comp())
            commandList.append(self.get_jump())
        else:
            return []
        return commandList
    
    def get_command_type(self) -> str:
        if self.currentCommand == '':
            return 'EMPTY'
        if self.currentCommand[0] == '(':
            return 'LABEL'
        self.commandCounter += 1
        if self.currentCommand[0] == '@':
            return 'A'
        return 'C'

    def get_dest(self) -> str:
        equalIndex = self.currentCommand.find('=')
        if equalIndex == -1:
            return ''
        return self.currentCommand[:equalIndex].strip()

    def get_comp(self) -> str:
        equalIndex = self.currentCommand.find('=')
        equalIndex += 1
        semicolonIndex = self.currentCommand.find(';')
        if semicolonIndex == -1:
            semicolonIndex = len(self.currentCommand)
        return self.currentCommand[equalIndex:semicolonIndex].strip()

    def get_jump(self) -> str:
        semicolonIndex = self.currentCommand.find(';')
        if semicolonIndex == -1:
            return ''
        semicolonIndex += 1
        return self.currentCommand[semicolonIndex:].strip()
            
            
            
    
