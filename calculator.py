from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLineEdit
)
import sys

def on_btn_click(text, result_field):
    current_text = result_field.text()
    if text == '=':
        try:
            result = str(eval(current_text))
            result_field.setText(result)
        except:
            result_field.setText('Error')
    elif text == 'C':
        result_field.clear()
    else:
        result_field.setText(current_text + text)


def create_button(text, result_field):
    btn = QPushButton(text)
    btn.setStyleSheet("""
                     QPushButton{ 
                        background-color:black;
                        color:white;
                        font-size:14px;
                        font-weight:900;
                    }
                    QPushButton:hover{
                        background-color:darkblue;
                      }
                      
                      """)
    btn.clicked.connect(lambda: on_btn_click(text, result_field))
    return btn

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Calculator')
    window.resize(300,400)
    window.setStyleSheet("background-color:white;")

    result = QLineEdit(window)
    result.setStyleSheet("""
                      background-color:white;
                      color:black;
                      font-size:14px;
                      font-weight:900;
                      """)
    result.setReadOnly(True)
    result.setAlignment(Qt.AlignmentFlag.AlignRight)
    result.setFixedHeight(50)

    layout = QVBoxLayout()
    layout.addWidget(result)

    btn_layout = QVBoxLayout()

    #
    btn_h1 = QHBoxLayout()
    btn_h1.addWidget(create_button('7', result))
    btn_h1.addWidget(create_button('8', result))
    btn_h1.addWidget(create_button('9', result))
    btn_h1.addWidget(create_button('/', result))

    #
    btn_h2 = QHBoxLayout()
    btn_h2.addWidget(create_button('4', result))
    btn_h2.addWidget(create_button('5', result))
    btn_h2.addWidget(create_button('6', result))
    btn_h2.addWidget(create_button('*', result))

    #
    btn_h3 = QHBoxLayout()
    btn_h3.addWidget(create_button('1', result))
    btn_h3.addWidget(create_button('2', result))
    btn_h3.addWidget(create_button('3', result))
    btn_h3.addWidget(create_button('-', result))

    #
    btn_h4 = QHBoxLayout()
    btn_h4.addWidget(create_button('0', result))
    btn_h4.addWidget(create_button('.', result))
    btn_h4.addWidget(create_button('=', result))
    btn_h4.addWidget(create_button('+', result))

    btn_layout.addLayout(btn_h1)
    btn_layout.addLayout(btn_h2)
    btn_layout.addLayout(btn_h3)
    btn_layout.addLayout(btn_h4)

    #
    clear_layout = QHBoxLayout()
    clear_layout.addWidget(create_button('C', result))
    btn_layout.addLayout(clear_layout)

    layout.addLayout(btn_layout)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()