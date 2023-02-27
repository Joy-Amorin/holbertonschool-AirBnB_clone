#!/usr/bin/python3
"""console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file"""
        print()
        return True

    def emptyline(self):
        """emptyline"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
