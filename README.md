# DASS-Assignment-1
Contains solutions for assignment 1 of course DASS which primarily focussed on python implementations for databases and interactive games.

## Question 1: Marks Directory

The implementation has been done using a csv file.
Open the terminal and enter the command 'python3 mdirectory.py'
This shall open up a Marks Directory Management Menu for you

Functionalities
You can do the following using the above code:
1.  Add a new entry : 
    - The code checks is an exact same entry (all fields having matching values) already exists.
    - If it exists, the system will prompt this message. If not the entry will be added to the database. 
    - Assumption: Multiple entries of the same roll number can exist as the course name/semester/exam type might be different for each entry.
    - Run : Select option 1 from menu
2.  Add records from another file
    - This feature allows loading entries from an external csv file.
    - Enter the file name (relative path from current directory)
    - Assumption: File has attributes in same order as in original directory
    - Run : Select option 2 from menu
        - Input: File name
        - Output: Status of addition of each entry into directory
3.  Display directory
    - Display current state of directory
    - Run : Select option 3 from menu
        - Input : None
        - Output : Records in tabular format
4.  Delete an entry
    - Run : Select option 4 from menu
        - Input : Roll number for which you want to delete records. This will display all records corresponding to that roll number. Then enter the index of the record for which you want to delete.
        - Output : Status on whether the delete has been successful or no such record was found
5.  Update an entry
    - Run : Select option 5 from menu
        - Input : Roll number for which you want to update records. This will display all records corresponding to that roll number. Then enter the index of the record for which you want to delete. Then select the column you want to update from the list of columns displayed. Further enter y for more changes in the same record or n for no more changes
        - Output : Status on whether the update has been successful or no such record was found     
6.  Search for an entry
    - Run : Select option 6 from menu
        - Input : Select the column on the basis of which you want to Search. Enter the value of the field for searching.
        - Output : Matching records will be displayed in tabular format. If no matching records are present, message will be shown
    - Assumption : Search is based on a single attribute
7.  Exit
    - Run : Select option 6 from menu
        - Input : None
        - Output : Exit the program

## Question 2: 2-D Map

- Open the terminal and enter the command 'python3 map.py'
- Input : Select the mode of input from the menu displayed (file or command line)
    - If file is selected, write the relative path of the file from the current directory
    - If terminal input is opted for, follow the input format strictly i.e 3mm/cm,N for example
- Output : Graph showing movement of person in 2D space. Co-ordinates are numbered to denote the sequence of visit.
- On closing the graph, the relative direction and distance is displayed on the terminal
- Assumptions: Initial co-ordinate is (0,0)
    - Direction must be in capital letters
    - In the input file, each command is on a separate line following the input format

## Question 3: Kaooa Game

- Implementation is done using Turtle library of python. The game is designed as Human vs Human and both users can play turn by turn on the same device.
- Open the terminal and enter the command 'python3 kaooa.py'
- This will start a turtle window showing the board.
- First move is played by crow. Click on the circle you want to place the crow in. For the first 7 crows, crow will be placed simply where you click. From the next movement, first select the crow you want to move by clicking (only single click) on the circle, then click on the new position. 
- For vulture, simply single click on the new position is enough.
- Standard rules of the game have been implemented like all 7 crows need to be placed before moving them.
- If some move is not allowed, the corresponding error message is printed on the screen and you get a chance to play again.
- At the end of the game, the winner is displayed on the center of the screen. Click on the close icon to exit the game.
- Run the code again to play another game.