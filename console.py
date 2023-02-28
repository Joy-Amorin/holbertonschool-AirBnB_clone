#!/usr/bin/python3
"""console"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""

        if not arg:
            print("""** class name missing **""")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            inst = BaseModel()
            storage.save()
            print(inst.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""

        argg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if argg[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(argg) == 1:
            print("** instance id missing **")
            return

        strr = str(argg[0]) + "." + str(argg[1])
        print(strr)

        if strr in storage.all():
            print(storage.all()[strr])
        else:
            print("** no instance found ** ")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        argg = arg.split()
        if not argg:
            print("** class name missing **")
        elif argg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argg) == 1:
            print("** instance id missing **")

        else:
            strr = str(argg[0]) + "." + argg[1]
            if strr in storage.all():
                storage.all().pop(strr)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
