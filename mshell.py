# Version 2
# Program now have cd logic and checking all the exceptions

import time, os

cmd_list = ['cd', 'pwd', 'exit', 'echo', 'export', 'unset', 'env', 'history', 'kill']

PATH = os.getcwd()

class Command:
    def __init__(self):
        self.file = ''
        self.args = []
        self.env_table = dict(
            HOME = os.environ.get('HOME'),
            PATH = os.environ.get('PATH'),
            PS1 = 'mshell>'
        )
    
    def init_vals(self):
        self.file = ''
        self.args = []

    def set_file(self, cmd):
        self.file = cmd
    
    def set_argv(self, argv):
        self.args.append(argv)

    def set_input(self, output):
        cmd_line = output.split()

        self.args = cmd_line

        self.set_file(self.args[0])

    def set_env_table(self): 
        self.env_table.update({f'{self.file}' : f'{self.args[2]}'})
        print(self.env_table)

    def get_env_table(self, val):
        return self.env_table.get(val)

    def execute_command(self):
        try:
            if self.file == 'exit':
                return False
            elif self.file == 'cd':
                if len(self.args) == 1:
                    self.set_argv(self.env_table['HOME'])
                os.chdir(self.args[1])
                return True
            elif self.args[1] == '=' and not self.file.isdigit():
                self.set_env_table()
                return True
            
            pid = os.fork()

            if pid == 0:
                self.instructions_exec()
            else:
                os.waitpid(pid, 0)
        except FileNotFoundError:
            print(f'{self.args[1]}: No such file directory found')
        except IndexError:
            print(f'{self.file}: command not found')
        finally:
            self.init_vals()

        return True
    
    def instructions_exec(self):
        try:
            os.execvp(self.file, self.args)
            os._exit(0)
        except FileNotFoundError:
            print(f'{self.file}: command not found')
            os._exit(127)



            
 
if __name__ == "__main__":
    cmd = Command()

    exit = True

    while (exit != False):
        try:
            prompt_name = cmd.get_env_table('PS1')

            output = input(f'{prompt_name} ')
            if output != '':
                cmd.set_input(output)
                exit = cmd.execute_command()
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
