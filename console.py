#!/usr/bin/python3
""" module that contains the entry point of the command interpreter """

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit from the program"""
        return True

    def do_EOF(self, line):
        """Handle end of file"""
        print()
        return True

    def help_quit(self):
        """help command of quit"""
        print("\n".join(["Quit command to exit the program"]))

    def emptyLine(self):
        """emptyline method"""
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            elms = line.split(" ")
            if elms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(elms) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(elms[0], elms[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            elms = line.split(" ")
            if elms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(elms) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(elms[0], elms[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    storage.all().pop(k)
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name."""
        if line:
            elms = line.split(" ")
            if elms[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_list = [
                    str(val)
                    for key, val in storage.all().items()
                    if type(val).__name__ == elms[0]
                ]
                print(new_list)
        else:
            list = [str(val) for key, val in storage.all().items()]
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating
        attribute (save the change into the JSON file)."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            elms = line.split(" ")
            if elms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(elms) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(elms[0], elms[1])
                if k not in storage.all():
                    print("** no instance found **")
                elif len(line) < 3:
                    print("** attribute name missing **")
                    return
                elif len(line) < 4:
                    print("** value missing **")
                    return
                else:
                    setattr(storage.all()[k], elms[2], elms[3])
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
