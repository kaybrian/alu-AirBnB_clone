#!/usr/bin/python3
"""
This module defines the console for the AirBnB clone project
"""

import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """
    This class defines the console for the AirBnB clone project
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        all_instances = storage.all()
        if len(line) == 0:
            all_objs = []
            for k, obj in all_instances.items():
                all_objs.append(str(obj))
            print(all_objs)
        elif line in HBNBCommand.valid_classes.keys():
            objs = []
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    key = line + "." + str(v.id)
                    objs.append(str(all_instances[key]))
            print(objs)
        else:
            self.perror(2)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()


if __name__ == '__main__':
    """
    Main function
    """
    HBNBCommand().cmdloop()
