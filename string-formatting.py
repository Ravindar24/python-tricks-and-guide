"""This module gives a brief explanation about how we can
format the strings in python using best practices.

Example use for illustration uses information such 
as firstname,lastname,age,profession of a person and
by the use of string formatting will generate an introduction
string.


variables:
    first_name : First name of person
    last_name : Last name of person
    age : age of person
    profession : profession or designation of person

Method:
    take_input() : It accepts information from user and returns a tuple of info.

    generate_formatted_introduction() :this function takes input above and print the introduction.
"""


def take_input():
    print("Enter First Name")
    first_name = input()
    print("Enter Last Name")
    last_name = input()
    print("Enter age")
    age = input()
    print("Enter profession")
    profession = input()
    print("Enter Formatting type!! please provide sf for formatting using str.format() or fs for fstring.")
    formatting_type = input()

    while(formatting_type.lower() not in ["fs", "sf"]):
        print("You have given wrong input for format.please provide either sf or fs to continue......")
        formatting_type = input()

    return (first_name, last_name, age, profession, formatting_type)


def generate_formatted_introduction():
    first_name, last_name, age, profession, formatting_type = take_input()

    introduction = ""
    if formatting_type.lower() == "fs":
        introduction = f"Hi My name is {first_name} {last_name}.I am {age} years old.I am a {profession}."
    elif formatting_type.lower() == "sf":
        introduction = "Hi My name is {0} {1}.I am {2} years old.I am a {3}.".format(
            first_name, last_name, age, profession)

    print(introduction)


if __name__ == "__main__":
    generate_formatted_introduction()
