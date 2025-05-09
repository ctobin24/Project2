from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that represents the logic for the grading gui
    """
    def __init__(self):
        """
        Method that sets up the default logic for the grading gui
        """
        super().__init__()
        self.setupUi(self)
        self.num_scores = 0

        #Intially hides all the score until user press a button for the number of scores
        self.score_1_label.hide()
        self.score_2_label.hide()
        self.score_3_label.hide()
        self.score_4_label.hide()
        self.score_1_input.hide()
        self.score_2_input.hide()
        self.score_3_input.hide()
        self.score_4_input.hide()

        #Connects the buttons to the gui
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())
        self.one_score_button.clicked.connect(lambda: self.one_score())
        self.two_score_button.clicked.connect(lambda: self.two_scores())
        self.three_score_button.clicked.connect(lambda: self.three_scores())
        self.four_score_button.clicked.connect(lambda: self.four_scores())

    def submit(self):
        """
         Method that is called upon when the user presses the SUMBIT button in the grading gui, then saves students name, inputted grades, and calculates highest, lowest, and average
        :return:None
        """
        #Get the name from the gui and checks if it is valid
        name = str(self.name_input.text().strip())
        try:
            if not name.isalpha():
                raise TypeError
        except:
            self.info_message_label.setStyleSheet("color : red;")
            self.info_message_label.setText('Invalid input for name')

        #Creates the list for the inputted grades
        grade_list = [int(self.score_1_input.text().strip())]
        if self.num_scores >= 2:
            grade_list.append(int(self.score_2_input.text().strip()))
        if self.num_scores >= 3:
            grade_list.append(int(self.score_3_input.text().strip()))
        if self.num_scores >= 4:
            grade_list.append(int(self.score_4_input.text().strip()))

        #Checks the inputted grades to make sure they are valid
        try:
            for grade in grade_list:
                if 0 <= grade <= 100:
                    continue
                raise ValueError
        except ValueError:
                self.info_message_label.setStyleSheet("color : red;")
                self.info_message_label.setText('Grades must be 0-100')

        #Calculates the highest, lowest, and average for the inputted scores
        highest = max(grade_list)
        lowest = min(grade_list)
        average = sum(grade_list) / len(grade_list)

        #Fills the list 0s as placeholders
        if len(grade_list) == 3:
            grade_list.append(0)
        elif len(grade_list) == 2:
            grade_list.append(0)
            grade_list.append(0)
        elif len(grade_list) == 1:
            grade_list.append(0)
            grade_list.append(0)
            grade_list.append(0)

        #Added the highest, lowest, and average to the end of the list
        grade_list.append(highest)
        grade_list.append(lowest)
        grade_list.append(average)

        #Puts the username into the first index of the list
        grade_list.insert(0, name)

        #Writes the entire list to the csvfile
        with open('final_score.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(grade_list)
            csvfile.close()

        self.clear()

    def clear(self):
        """
        Method that is called upn when the user presses the CLEAR button in the voting gui, then wipes all the input boxes to blank
        :return:None
        """
        self.name_input.clear()
        self.score_1_input.clear()
        self.score_2_input.clear()
        self.score_3_input.clear()
        self.score_4_input.clear()
        self.one_score()

    def one_score(self):
        """
        When the user presses the 1 button to specify how many score there are, then displays only one input line
        :return:None
        """
        self.num_scores = 1
        self.score_1_label.show()
        self.score_1_input.show()
        self.score_2_label.hide()
        self.score_2_input.hide()
        self.score_3_label.hide()
        self.score_3_input.hide()
        self.score_4_label.hide()
        self.score_4_input.hide()
        self.score_2_input.clear()
        self.score_3_input.clear()
        self.score_4_input.clear()

    def two_scores(self):
        """
        When the user presses the 2 button to specify how many scores there are, then displays only two input lines
        :return:None
        """
        self.num_scores = 2
        self.score_1_label.show()
        self.score_1_input.show()
        self.score_2_label.show()
        self.score_2_input.show()
        self.score_3_label.hide()
        self.score_3_input.hide()
        self.score_4_label.hide()
        self.score_4_input.hide()
        self.score_3_input.clear()
        self.score_4_input.clear()

    def three_scores(self):
        """
        When the user presses the 3 button to specify how many scores there are, then displays only three input lines
        :return:None
        """
        self.num_scores = 3
        self.score_1_label.show()
        self.score_1_input.show()
        self.score_2_label.show()
        self.score_2_input.show()
        self.score_3_label.show()
        self.score_3_input.show()
        self.score_4_label.hide()
        self.score_4_input.hide()
        self.score_4_input.clear()

    def four_scores(self):
        """
        When the user presses the 4 button to specify how many scores there are, then displays only four input lines
        :return:None
        """
        self.num_scores = 4
        self.score_1_label.show()
        self.score_1_input.show()
        self.score_2_label.show()
        self.score_2_input.show()
        self.score_3_label.show()
        self.score_3_input.show()
        self.score_4_label.show()
        self.score_4_input.show()
