from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QMainWindow):
    #Making the Window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100,
                         300, 750)
        self.UiComponents()
        self.show()

    # method for components
    def UiComponents(self):
        #Keeps track of each player's scores
        self.player1_total = 0
        self.player2_total = 0

        #Setting up turns
        self.turn = 0
        self.times = 0

        # creating a push button list
        self.push_list = []

        # creating 2d list
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)

        # setting coordiantes
        x = 90
        y = 90

        # traversing through push button list
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)
                # putting code into the buttons
                self.push_list[i][j].setFont(QFont(QFont('Times', 17)))
                self.push_list[i][j].clicked.connect(self.action_called)

        # creating label to tell the score
        self.label = QLabel(self)
        self.label.setGeometry(20, 300, 260, 60)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Times', 20))

        # creating push button to restart the board
        reset_game = QPushButton("Reset_Game", self)
        reset_game.setGeometry(50, 380, 200, 50)
        reset_game.clicked.connect(self.reset_game_action)

        # creating push button to reset the score
        reset_score = QPushButton("Reset_Score", self)
        reset_score.setGeometry(50, 460, 200, 50)
        reset_score.clicked.connect(self.reset_score_action)

        font = QtGui.QFont()
        font.setPointSize(15)
        # creating label for both players
        self.label_player1 = QLabel(self)
        self.label_player1.setGeometry(20, 550, 100, 60)
        self.label_player1.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : red;"
                                 "}")
        self.label_player1.setText("Player O")
        self.label_player1.setAlignment(Qt.AlignCenter)
        self.label_player1.setFont(font)

        self.label_player2 = QLabel(self)
        self.label_player2.setGeometry(170, 550, 100, 60)
        self.label_player2.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : yellow;"
                                 "}")
        self.label_player2.setText("Player X")
        self.label_player2.setAlignment(Qt.AlignCenter)
        self.label_player2.setFont(font)

        # creating labels to show the scores of each player
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_player1_score = QLabel(self)
        self.label_player1_score.setGeometry(20, 625, 100, 60)
        self.label_player1_score.setText('0')
        self.label_player1_score.setFont(font)
        self.label_player1_score.setAlignment(Qt.AlignCenter)

        self.label_player2_score = QLabel(self)
        self.label_player2_score.setGeometry(170, 625, 100, 60)
        self.label_player2_score.setText('0')
        self.label_player2_score.setFont(font)
        self.label_player2_score.setAlignment(Qt.AlignCenter)

    # method used to reset the board
    def reset_game_action(self):
        self.turn = 0
        self.times = 0
        self.label.setText("")
        for buttons in self.push_list:
            for button in buttons:
                # resetting the buttons
                button.setEnabled(True)
                button.setText("")

    # method used to reset the score
    def reset_score_action(self):
        self.player2_total = 0
        self.player1_total = 0

        self.label_player1_score.setText('0')
        self.label_player2_score.setText('0')

    # code for buttons used as board
    def action_called(self):
        self.times += 1

        # getting button which called the action
        button = self.sender()

        # making button disabled
        button.setEnabled(False)

        # checking the turn
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0


        win = self.who_wins()
        text = ""

        # checking for winner
        if win == True:
            if self.turn == 0:
            # O has won
                text = "O Won"
                self.player1_total += 1
                self.label_player1_score.setText(str(self.player1_total))
            # X has won
            else:
                text = "X Won"
                self.player2_total += 1
                self.label_player2_score.setText(str(self.player2_total))

            # disabling all the buttons
            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)

        # code used in case of draw
        elif self.times == 9:
            text = "Match is Draw"

        # displaying winner through label
        self.label.setText(text)

    # method to check who wins
    def who_wins(self):

        # checking for row win
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True

        # checking for column win
        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True

        # checking for top left -- bottom right win
        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True

        # checking for top right -- bottom left win
        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        # if nothing is crossed
        return False


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())