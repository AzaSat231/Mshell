# Version 2
# Program now have cd logic and checking all the exceptions

import time, os

cmd_list = ['cd', 'pwd', 'exit', 'echo', 'export', 'unset', 'env', 'history', 'kill']

PATH = os.getcwd()

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

    def execute_command(self):
        try:
            if self.file == 'exit':
                return False
            elif self.file == 'cd':
                if len(self.args) == 1:
                    self.set_argv(os.environ.get('HOME'))
                os.chdir(self.args[1])
                return True
            
            pid = os.fork()

            if pid == 0:
                self.instructions_exec()
            else:
                os.waitpid(pid, 0)
        except FileNotFoundError:
            print(f'{self.args[1]}: No such file directory found')
        finally:
            self.__init__()

        return True
    
    def instructions_exec(self):
        try:
            os.execvp(self.file, self.args)
            os._exit(0)
        except FileNotFoundError:
            print(f'Command {self.file} is not found')
            os._exit(127)



            
 
if __name__ == "__main__":
    cmd = Command()

    exit = True

    while (exit != False):
        try:
            output = input('mshell> ')
            if output != '':
                cmd.set_input(output)
                exit = cmd.execute_command()
        except EOFError:
            break
        except KeyboardInterrupt:
            break
