#!/usr/bin/python3
import cmd
import sys
import datetime
import json


class Hnbb(cmd.Cmd):
    prompt = "(hbnb) "
# implement commands in my command line console

    def do_quit(self, arg):

        """This command exits the shell when run.
        do_quit: A fuction that contains the command name
        args:
            arg: Represents the whole command line other than the command name.
        return:
            always true.
        """
        return True

    def do_EOF(self, arg):

        """This command exits the shell with end of file.
        do_EOF: A fuction that contains the command name
        args:
            arg: Represents the whole command line other than the command name.
        return:
            always true.
        """
        return True

    def do_help(self, arg):
        """This function implements the help command.
        do_quit: A fuction that contains the command name
        args:
            arg: Represents the whole command line other than the command name.
        return:
            always true.
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Handles empty line i.e when enter is pressed without any command"""
        pass

    def do_create(self, line):
        arg = line.split()
        if arg[0].lower() != "create":
            print("Ivalid syntax: use create <name>")
            return
        name = arg[1]
        new_user = User(name)
        myuser[new_user.id] = new_user
        print(f"New user created with user id: {new_user.id} and name: {new_user.name}")

if __name__ == "__main__":
    myshell = Hnbb()
    # check if command is from interactive or non interactive mode
    if sys.stdin.isatty:
        myshell.cmdloop()
    else:
        command = sys.stdin.read()
        for command in commands:
            myshell.onecmd(command)
