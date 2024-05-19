#!/usr/bin/python3
"""
Command interpreter for HBNB.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help information for the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Ensures the prompt goes to the next line on EOF
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
