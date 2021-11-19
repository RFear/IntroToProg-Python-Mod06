# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2021,Created started script
# RRoot,1.1.2021,Added code to complete assignment 5
# RFear,11.17.2021,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        dicRow = {"Task": task.capitalize(), "Priority": priority.capitalize()}
        list_of_rows.append(dicRow)  # Add new data to the lstTable
        return 'Success'

    @staticmethod
    def remove_data_from_list(opt, list_of_rows):
        list_of_rows.pop(opt - 1)
        return 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        f = open(file_name, "w")
        for row in list_of_rows:
            f.write(row["Task"] + "," + row["Priority"] + "\n")
        f.close()
        return 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current tasks to do are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task = input("Enter new task: ")
        valid = ["high", "med", "low"]  # Temporary list of valid inputs.  Used in while loop.
        while True:
            priority = input("Enter new task priority [High, Med, Low]: ")
            if priority.lower() in valid:
                break
        return task, priority

    @staticmethod
    def input_task_to_remove(list_of_rows):
        print("Current stored data: ")
        for i in range(0, len(list_of_rows)):
            print(f"Line [{i + 1}]: {list_of_rows[i]}")
        opt = None
        while opt not in range(1, len(list_of_rows) + 1):
            opt = int(input("\nWhich line would you like to remove? "))
            print(f"You selected to remove {list_of_rows[opt - 1]}")
        return opt


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':
        strTask, strPriority = IO.input_new_task_and_priority()
        strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == '2':
        intRemove = IO.input_task_to_remove(lstTable)
        strStatus = Processor.remove_data_from_list(intRemove, lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == '3':
        valid = ["y", "n"]
        while True:
            strChoice = IO.input_yes_no_choice("Save this data to file? (y/n): ")
            if strChoice in valid:
                if strChoice.lower() == "y":
                    strStatus = Processor.write_data_to_file(strFileName, lstTable)
                    IO.input_press_to_continue(strStatus)
                else:
                    IO.input_press_to_continue("Save Cancelled!")
                break

    elif strChoice == '4':  # Reload Data from File
        valid = ["y", "n"]
        print("Warning: Unsaved Data Will Be Lost!")
        while True:
            strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n): ")
            if strChoice in valid:
                if strChoice.lower() == "y":
                    strStatus = Processor.read_data_from_file(strFileName, lstTable)
                    IO.input_press_to_continue(strStatus)
                else:
                    IO.input_press_to_continue("File Reload  Cancelled!")
                break

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
