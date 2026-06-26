# Version 1
# Program, that parse users input and bash do all the work

import subprocess, os

cmd_list = ['cd', 'pwd', 'exit', 'echo', 'export', 'unset', 'env', 'history', 'kill']


class Command:
    def __init__(self):
        self.name_cmd = ''
        self.argv = ''

    def set_cmd(self, cmd):
        self.name_cmd = cmd
    
    def set_argv(self, argv):
        self.argv += argv

    def set_input(self, output):
        cmd_line = output.split()

        flag = 0

        for line in cmd_line:
            if flag == 0:
                self.name_cmd = line
                flag = 1
            else:
                self.set_argv(line)
                self.set_argv(' ')

    def execute_command(self):
        value = self.commands_rules(self.name_cmd, self.argv)
        os.system(f'{self.name_cmd} {self.argv}')

        self.__init__()

        return True

 
if __name__ == "__main__":
    cmd = Command()

    exit = True

    while (exit != False):
        print('mshell> ', end='')
        output = input()

        cmd.set_input(output)

        exit = cmd.execute_command()
