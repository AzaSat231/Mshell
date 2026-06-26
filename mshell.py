# Version 1
# Program use real forkk

import time, os

cmd_list = ['cd', 'pwd', 'exit', 'echo', 'export', 'unset', 'env', 'history', 'kill']


class Command:
    def __init__(self):
        self.file = ''
        self.args = []

    def set_cmd(self, cmd):
        self.file = cmd
    
    def set_argv(self, argv):
        self.args.append(argv)

    def set_input(self, output):
        cmd_line = output.split()

        self.args = cmd_line

        self.set_cmd(self.args[0])

        print(self.file, self.args)

    def execute_command(self):

        pid = os.fork()

        if pid == 0:
            os.execvp(self.file, self.args)
        else:
            self.__init__()

        time.sleep(1)

        return True

 
if __name__ == "__main__":
    cmd = Command()

    exit = True

    while (exit != False):

        print('mshell> ', end='')
        output = input()

        cmd.set_input(output)

        exit = cmd.execute_command()
