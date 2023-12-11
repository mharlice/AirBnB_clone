#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""
import cmd
import sys

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Custom console class"""
    # prompt
    prompt = "(hbnb) " if sys.stdin.isatty() else ""

    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        print("")
        return True

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()  # to get rid of extra spaces
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def help_create(self):
        """Man Create"""
        print('\n'.join(["Create an instance of a class",
                         "Usage: create [Model]"]))

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                o_id = args[1]
                for i, j in models.storage.all().items():
                    key_arr = i.split('.')
                    if args[0] == key_arr[0] and o_id == key_arr[1]:
                        print(j)
                        return
                print("** no instance found **")

    def help_show(self):
        """Man Show"""
        print('\n'.join(["Show string representation of an instance",
                         "Usage: show [Model] <id>"]))

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                o_id = args[1]
                for i in models.storage.all():
                    key_arr = i.split('.')
                    if args[0] == key_arr[0] and o_id == key_arr[1]:
                        del models.storage.all()[i]
                        models.storage.save()
                        return
                print("** no instance found **")

    def help_destroy(self):
        """Man destroy"""
        print('\n'.join(["Deletes an instance",
                         "Usage: destroy [Model] <id>"]))

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()  # to get rid of extra spaces
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            list_a = []
            for value in models.storage.all().values():
                list_a.append(str(value))
            print(list_a)

    def help_all(self):
        """Man all"""
        print('\n'.join(["Prints string representation of all instances",
                         "Usage: all [Any exiting Model]"]))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()  # to get rid of extra spaces
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            o_id = args[1]
            # Check if the input is enclosed in quotes
            for i in range(2, 4):
                if args[i].startswith('"') and args[i].endswith('"'):
                    args[i] = args[i][1:-1]
            for i in models.storage.all():
                key_arr = i.split('.')
                if args[0] == key_arr[0] and o_id == key_arr[1]:
                    setattr(models.storage.all()[i], args[2], args[3])
                    models.storage.all()[i].save()
                    return
            print("** no instance found **")

    def do_count(self, line):
        """
        Retrieves the number of instances of a class
        """
        args = line.split()  # to get rid of extra spaces
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for value in models.storage.all():
                if value.__class__.__name == line:
                    count += 1
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
