# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Diellza Mehmeti,11/20/2024,Assignment06
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the data variables
students: list = []  # a table of student data
menu_choice: str ='' # Hold the choice made by the user.

class FileProcessor:
    """A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        DMehmeti, 11.20.2024,Created Class
        """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function reads the file data into a list of dictionaries

           ChangeLog: (Who, When, What)
           DMehmeti, 11.20.2024,created a function
           :return: list
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message="Text file must exist before running this script!", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a problem reading the file", error=e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes the file data into a json file

             ChangeLog: (Who, When, What)
             DMehmeti, 11.20.2024,created a function
             :return: list
              """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            message="Error: There was a problem with writing to the file.\n"
            message+= "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if not file.closed:
                file.close()

class IO:
    """
       A collection of presentation layer functions that manage user input and output
    
       ChangeLog: (Who, When, What)
       DMehmeti, 11.20.2024,Created Class
       DMehmeti, 11.20.2024,Added menu output and input functions
       DMehmeti, 11.20.2024,Added a function to display the data
       DMehmeti, 11.20.2024,Added a function to display custom error messages
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        DMehmeti,11.20.2024,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu choice to the user

        ChangeLog: (Who, When, What)
        DMehmeti, 11.20.2024,Created function

        :return: str
        """
        print() #extra space
        print(menu)
        print() #extra space

    @staticmethod
    def input_menu_choice():
        """ This function displays a menu choice to the user and the user chooses the menu choice

        ChangeLog: (Who, When, What)
        DMehmeti, 11.20.2024,Created function

        :return: str
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1","2","3","4"):
                raise Exception ("Please only choose between 1-4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student names and course names to the user

       ChangeLog: (Who, When, What)
       DMehmeti, 11.20.2024,Created function

       :return: list
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student data (first name, last name, and course name) from the user

               ChangeLog: (Who, When, What)
               DMehmeti, 11.20.2024,Created function

               :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct data type",error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a problem with your data",error=e)
        return student_data


#Start of main body
students=FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    #present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students=IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
