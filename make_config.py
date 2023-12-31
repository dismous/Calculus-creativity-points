"""
main
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from taylor_calculator import *
from PyQt5.QtGui import QIcon
from sympy import sympify
from sympy import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.base_expr_entry = QLineEdit(self)
        self.development_point_entry = QLineEdit(self)
        self.grade_entry = QLineEdit(self)
        self.plot_range_entry = QLineEdit(self)
        self.calculate_button = QPushButton('Calculate and Plot', self)
        self.calculate_button.clicked.connect(self.calculate_and_plot_wrapper)
        self.setWindowIcon(QIcon('images/images.jpg'))
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Введіть функцію f(x):"))
        layout.addWidget(self.base_expr_entry)
        layout.addWidget(QLabel("Точка розвитку [0]: "))
        layout.addWidget(self.development_point_entry)
        layout.addWidget(QLabel("Ступінь [4]: "))
        layout.addWidget(self.grade_entry)
        layout.addWidget(QLabel("Діапазон побудови [3]: "))
        layout.addWidget(self.plot_range_entry)
        layout.addWidget(self.calculate_button)

    def calculate_and_plot_wrapper(self):
        function_mapping = {'tg': 'tan', 'ctg': '1/tan', 'arctg': 'atan', 'arcctg': 'acotan', 'arcsin': 'asin'}
        user_input = self.base_expr_entry.text() or 'cos(x)'
        for user_func in sorted(function_mapping.keys(), key=len, reverse=True):
            user_input = user_input.replace(user_func, function_mapping[user_func])
        BASE_EXPR = sympify(user_input)
        DEVELOPMENT_POINT = float(self.development_point_entry.text() or '0')
        GRADE = int(self.grade_entry.text() or '4')
        PLOT_RANGE = int(self.plot_range_entry.text() or '3')
        calculate_and_plot(base_expr=BASE_EXPR, development_point=DEVELOPMENT_POINT, grade=GRADE, plot_range=PLOT_RANGE)

app = QApplication([])
window = MyApp()
window.show()
app.exec_()
