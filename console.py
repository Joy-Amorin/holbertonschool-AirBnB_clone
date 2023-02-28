#!/usr/bin/python3
"""console"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __class_t = {"BaseModel": BaseModel(), "User": User()}

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
        """Creates a new instance of Classes"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__class_t:
            print("** class doesn't exist **")
        else:
            inst = self.__class_t[arg]
            storage.save()
            print(inst.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args_l = arg.split()
        if not args_l:
            print("** class name missing **")
            return
        if args_l[0] not in self.__class_t:
            print("** class doesn't exist **")
            return
        if len(args_l) == 1:
            print("** instance id missing **")
            return
        strr = str(args_l[0]) + "." + str(args_l[1])
        if strr in storage.all():
            print(storage.all()[strr])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based
        on the class name and id"""
        args_l = arg.split()
        if not args_l:
            print("** class name missing **")
            return
        if args_l[0] not in self.__class_t:
            print("** class doesn't exist **")
            return
        if len(args_l) == 1:
            print("** instance id missing **")
            return
        strr = str(args_l[0]) + "." + str(args_l[1])
        if strr in storage.all():
            del(storage.all()[strr])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        if not arg:
            print([value.__str__() for value in storage.all().values()])
        elif arg in self.__class_t:
            print([storage.all()[key].__str__() for key in storage.all().keys()
                   if key.split('.')[0] == arg])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        args_l = arg.split()
        if not args_l:
            print("** class name missing **")
            return
        if args_l[0] not in self.__class_t:
            print("** class doesn't exist **")
            return
        if len(args_l) == 1:
            print("** instance id missing **")
            return
        strr = str(args_l[0]) + "." + str(args_l[1])
        if strr not in storage.all():
            print("** no instance found **")
            return
        if len(args_l) == 2:
            print("** attribute name missing **")
            return
        if len(args_l) == 3:
            print("** value missing **")
            return

        storage.all()[strr].__dict__.update({args_l[2]: args_l[3]})
        storage.all()[strr].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
