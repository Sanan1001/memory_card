#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout,QWidget,QGroupBox, QRadioButton, QVBoxLayout, QPushButton,QLabel,QButtonGroup,
    )
from random import shuffle

app = QApplication([])

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Синий','Белый'))
question_list.append(Question('Какого цвета нет в флаге России', 'Зеленый', 'Красный', 'Синий','Белый'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('Чего нет в флаге Казахстана', 'Рыба', 'Беркут', 'Солнце', 'Арнамент'))



window = QWidget()
window.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Государственный язык Бразилии')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Португальский')
rbtn_2 = QRadioButton('Бразильский')
rbtn_3 = QRadioButton('Английский')
rbtn_4 = QRadioButton('Испанский')



RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_correct = QLabel("Португальский")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct, alignment =Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

ResGroupBox = QGroupBox('Результат теста')
lb_result1 = QLabel('Правильно/Неправильно')
lb_correct1 = QLabel('Ответ будет тут')
layout_res1 = QVBoxLayout()
layout_res1.addWidget(lb_result1)
layout_res1.addWidget(lb_correct1, alignment =Qt.AlignHCenter, stretch=2)
ResGroupBox.setLayout(layout_res1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(ResGroupBox)
AnsGroupBox.hide()
ResGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK ,stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout( layout_line1 , stretch = 2 )
layout_card.addLayout( layout_line2 , stretch = 8 )
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ResGroupBox.hide()
    btn_OK.setText('Следуйщий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    ResGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
 
def show_test_res():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    ResGroupBox.show()
    btn_OK.setText('Начать заново')
    lb_result1.setText('Завершено')
    lb_correct1.setText('Результат теста' +str(window.points) +' из ' + str(window.questions) )
    lb_Question.hide()
    window.points = 0 
    window.questions = 0

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.points += 1
        window.questions += 1
    else:    
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct ( ' Hеверно ! ' )
            window.questions += 1

def show_correct(res):
    lb_result.setText(res)
    show_result()


def next_questinon():
    window.cur_question = window.cur_question +1
    if window.cur_question >= len(question_list):
        lb_correct.setText('Вопросы закончились')
        btn_OK.setText('Завершить тест')
        window.cur_question = -1
    else:
        lb_Question.show()
        q = question_list[window.cur_question]
        ask(q)    

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Завершить тест':
        show_test_res()
    else:
        next_questinon()



window = QWidget()
window.points = 0
window.cur_question = -1
window.questions = 0
window.setLayout(layout_card)
window.cur_question = -1
btn_OK.clicked.connect(click_ok)


window.resize(400,300)
window.show()

app.exec()