from PyQt6.QtWidgets import *
from gui import *
import random


def end_game():
    '''
    Function: quits game
    '''
    quit()


class Logic(QMainWindow, Ui_mainWindow):
    '''
    Function: Sets the game up.
              Gathers player name.
              chooses random word to be guessed
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.guess_count = 0
        self.column = 0
        self.word_guessed_correct = False

        self.lineEdit_input.setEnabled(True)

        self.label_topheader.setText("Let\'s play Wordle!")
        self.pushButton_middle.setText('Enter')
        self.lineEdit_input.setPlaceholderText("Type name and click enter")
        self.pushButton_middle.clicked.connect(lambda: self.get_name())

        with (open('FiveLetterWords.csv', 'r') as wordsList):
            content = wordsList.readlines()
            self.word = random.choice(content).lower().strip()

        print(self.word)  # print word to see in console

        self.pushButton_middle.clicked.connect(lambda: self.play())

    def get_name(self) -> str:
        '''
        Function: creates player name variable
                  clears line edit
        '''
        self.name = self.lineEdit_input.displayText()
        self.lineEdit_input.clear()

        if self.name:
            self.play()
        else:
            return

    def play(self):
        '''
        Function: creates submit, end game, and scores buttons depending if the word is guessed or not.
                  creates pathway to correct function once button is clicked
        '''
        self.lineEdit_input.setEnabled(True)
        self.lineEdit_input.clear()
        self.label_inputbox.clear()
        if not self.word_guessed_correct:
            if self.guess_count < 5:
                self.pushButton_middle.setText('Submit')
                self.pushButton_left.setText('End Game')
                self.pushButton_right.setText('Scores')

                self.lineEdit_input.setPlaceholderText('Make your guess and click submit')

                self.pushButton_middle.clicked.disconnect()
                self.pushButton_middle.clicked.connect(lambda: self.entered_guess())
                self.pushButton_left.clicked.connect(lambda: end_game())
                self.pushButton_right.clicked.connect(lambda: self.show_scores())

            else:
                self.pushButton_middle.setText('')
                self.pushButton_left.setText('End Game')
                self.pushButton_right.setText('Scores')
                self.label_topheader.setText('Out of tries. Play again')
                self.pushButton_left.clicked.connect(lambda: end_game())
                self.pushButton_right.clicked.connect(lambda: self.show_scores())
        else:
            self.pushButton_middle.setEnabled(False)
            self.pushButton_right.setText('Show Scores')
            self.pushButton_left.clicked.connect(lambda: end_game())
            self.pushButton_right.clicked.connect(lambda: self.show_scores())

    def entered_guess(self):
        '''
        Function: gathers player's guess input.
                  checks if guess is correct word, then displays and cuts to guess correct function
                  if not, runs guess throw valid check and display functions
        '''
        guess = str(self.lineEdit_input.text().lower().strip())
        self.lineEdit_input.clear()

        if guess == self.word:
            self.guess_count += 1

            num = 1
            color = "green"
            for i in range(5):
                self.change_letter_box_color(i, color, num)

            self.display_guess(guess)
            self.guessed_correct()
        else:
            if self.valid_guess_check(guess):
                self.guess_count += 1
                self.check_for_correct_letters(guess)
                self.display_guess(guess)
                if self.guess_count <= 5:
                    self.play()
            else:
                self.play()

    def valid_guess_check(self, guess: str):
        '''
        Function: checks if guess is 5-letters and displays message accordingly
        returns: returns True if text is 5-letters, if not False
        '''
        valid = True
        if len(guess) != 5:
            self.label_topheader.setText('Enter a 5-letter word.\nTry again')
            self.lineEdit_input.clear()
            valid = False
        else:
            if guess.isalpha():
                pass
            else:
                self.label_topheader.setText('Only letters.\nTry Again')
                valid = False
        return valid

    def check_for_correct_letters(self, guess: str):
        '''
        Function: compares letters in valid guess to letters in word for match
        :param guess: valid guess
        :return: False if guess is not word, if not True
        '''
        valid = True

        guessed_word = [letter for letter in guess]
        official_word = [letter for letter in self.word]

        for i in range(len(guess)):
            if guessed_word[i] in official_word:

                if guessed_word[i] == official_word[i]:

                    num = 1
                    color = "green"
                    self.change_letter_box_color(i, color, num)

                else:
                    if guess.count(guessed_word[i]) > official_word.count(guessed_word[i]):
                        pass
                    else:
                        num = 2
                        color = "yellow"
                        self.change_letter_box_color(i, color, num)

            else:
                pass

        return valid

    def change_letter_box_color(self, index, color, circumstance):
        match circumstance:
            case 1:
                if self.guess_count == 1:
                    match index + 1:
                        case 1:
                            self.label_row1letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            self.label_row1letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            self.label_row1letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            self.label_row1letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            self.label_row1letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 2:
                    match index + 1:
                        case 1:
                            self.label_row2letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            self.label_row2letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            self.label_row2letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            self.label_row2letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            self.label_row2letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 3:
                    match index + 1:
                        case 1:
                            self.label_row3letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            self.label_row3letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            self.label_row3letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            self.label_row3letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            self.label_row3letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 4:
                    match index + 1:
                        case 1:
                            self.label_row4letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            self.label_row4letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            self.label_row4letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            self.label_row4letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            self.label_row4letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 5:
                    match index + 1:
                        case 1:
                            self.label_row5letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            self.label_row5letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            self.label_row5letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            self.label_row5letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            self.label_row5letter5.setStyleSheet(f"background-color: {color}")

            case 2:
                if self.guess_count == 1:
                    match index + 1:
                        case 1:
                            if not self.label_row1letter1.setStyleSheet(f"background-color: green") :
                                self.label_row1letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            if not self.label_row1letter2.setStyleSheet(f"background-color: green") :
                                self.label_row1letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            if not self.label_row1letter3.setStyleSheet(f"background-color: green") :
                                self.label_row1letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            if not self.label_row1letter4.setStyleSheet(f"background-color: green") :
                                self.label_row1letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            if not self.label_row1letter5.setStyleSheet(f"background-color: green") :
                                self.label_row1letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 2:
                    match index + 1:
                        case 1:
                            if not self.label_row2letter1.setStyleSheet(f"background-color: green") :
                                self.label_row2letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            if not self.label_row2letter2.setStyleSheet(f"background-color: green") :
                                self.label_row2letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            if not self.label_row2letter3.setStyleSheet(f"background-color: green") :
                                self.label_row2letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            if not self.label_row2letter4.setStyleSheet(f"background-color: green") :
                                self.label_row2letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            if not self.label_row2letter5.setStyleSheet(f"background-color: green") :
                                self.label_row2letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 3:
                    match index + 1:
                        case 1:
                            if not self.label_row3letter1.setStyleSheet(f"background-color: green") :
                                self.label_row3letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            if not self.label_row3letter2.setStyleSheet(f"background-color: green") :
                                self.label_row3letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            if not self.label_row3letter3.setStyleSheet(f"background-color: green") :
                                self.label_row3letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            if not self.label_row3letter4.setStyleSheet(f"background-color: green") :
                                self.label_row3letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            if not self.label_row3letter5.setStyleSheet(f"background-color: green") :
                                self.label_row3letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 4:
                    match index + 1:
                        case 1:
                            if not self.label_row4letter1.setStyleSheet(f"background-color: green") :
                                self.label_row4letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            if not self.label_row4letter2.setStyleSheet(f"background-color: green") :
                                self.label_row4letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            if not self.label_row4letter3.setStyleSheet(f"background-color: green") :
                                self.label_row4letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            if not self.label_row4letter4.setStyleSheet(f"background-color: green") :
                                self.label_row4letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            if not self.label_row4letter5.setStyleSheet(f"background-color: green") :
                                self.label_row4letter5.setStyleSheet(f"background-color: {color}")
                elif self.guess_count == 5:
                    match index + 1:
                        case 1:
                            if not self.label_row5letter1.setStyleSheet(f"background-color: green") :
                                self.label_row5letter1.setStyleSheet(f"background-color: {color}")
                        case 2:
                            if not self.label_row5letter2.setStyleSheet(f"background-color: green") :
                                self.label_row5letter2.setStyleSheet(f"background-color: {color}")
                        case 3:
                            if not self.label_row5letter3.setStyleSheet(f"background-color: green") :
                                self.label_row5letter3.setStyleSheet(f"background-color: {color}")
                        case 4:
                            if not self.label_row5letter4.setStyleSheet(f"background-color: green") :
                                self.label_row5letter4.setStyleSheet(f"background-color: {color}")
                        case 5:
                            if not self.label_row5letter5.setStyleSheet(f"background-color: green") :
                                self.label_row5letter5.setStyleSheet(f"background-color: {color}")

    def display_guess(self, guess: str):
        '''
        Function: displays letters for each attempt in correcr position
        :param guess: valid guess
        '''
        if self.guess_count == 1:
            self.label_row1letter1.setText(guess[0])
            self.label_row1letter2.setText(guess[1])
            self.label_row1letter3.setText(guess[2])
            self.label_row1letter4.setText(guess[3])
            self.label_row1letter5.setText(guess[4])
        elif self.guess_count == 2:
            self.label_row2letter1.setText(guess[0])
            self.label_row2letter2.setText(guess[1])
            self.label_row2letter3.setText(guess[2])
            self.label_row2letter4.setText(guess[3])
            self.label_row2letter5.setText(guess[4])
        elif self.guess_count == 3:
            self.label_row3letter1.setText(guess[0])
            self.label_row3letter2.setText(guess[1])
            self.label_row3letter3.setText(guess[2])
            self.label_row3letter4.setText(guess[3])
            self.label_row3letter5.setText(guess[4])
        elif self.guess_count == 4:
            self.label_row4letter1.setText(guess[0])
            self.label_row4letter2.setText(guess[1])
            self.label_row4letter3.setText(guess[2])
            self.label_row4letter4.setText(guess[3])
            self.label_row4letter5.setText(guess[4])
        elif self.guess_count == 5:
            self.label_row5letter1.setText(guess[0])
            self.label_row5letter2.setText(guess[1])
            self.label_row5letter3.setText(guess[2])
            self.label_row5letter4.setText(guess[3])
            self.label_row5letter5.setText(guess[4])

    def show_scores(self):
        '''
        Function: displays previous scores
        '''
        self.lineEdit_input.setEnabled(False)
        with open('scores1.csv', 'r') as scores_file:
            self.label_inputbox.setText(f'{scores_file.read()}')

        self.pushButton_right.setText('Go Back')
        self.pushButton_left.setText('End Game')
        self.pushButton_right.clicked.connect(lambda: self.play())
        self.pushButton_left.clicked.connect(lambda: end_game())

    def guessed_correct(self):
        '''
        Function: after guess is matched is word, displays messages and buttons accordindgly
        '''
        self.pushButton_middle.setEnabled(False)
        self.word_guessed_correct = True
        with open('scores.csv', 'a') as scores_file:
            scores_file.write(f'{self.name}, {self.guess_count}\n')
        self.label_topheader.setText(f'You guessed it!\nThanks for playing!')
        self.lineEdit_input.setPlaceholderText('Yay!')
        self.lineEdit_input.setEnabled(False)
        self.pushButton_middle.setText('')
        self.pushButton_left.setText('End Game')
        self.pushButton_right.setText('Show scores')
        self.pushButton_left.clicked.connect(lambda: end_game())
        self.pushButton_right.clicked.connect(lambda: self.show_scores())

    def __str__(self):
        '''
        Function: clears lines
        '''
        self.lineEdit_input.clear()
        self.label_inputbox.clear()
        self.pushButton_left.setText('')
        self.pushButton_middle.setText('')
        self.pushButton_right.setText('')
