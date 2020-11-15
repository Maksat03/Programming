from ui import Ui_Calculator
import sys
from PySide2.QtWidgets import QWidget, QApplication

# Create application
app = QApplication(sys.argv)

# Create form and init UI
Form = QWidget()
ui = Ui_Calculator()
ui.setupUi(Form)
Form.show()
text = ""

# Hook logic
def add_number(num):
	if globals()['text'] == "OUTPUT":
		globals()['text'] = ""
	globals()['text'] += str(num)
	ui.btn_clear.setEnabled(True)
	ui.OUTPUT.setText(globals()['text'])

def add_operation(operator):
	if globals()['text'] == "OUTPUT":
		globals()['text'] = ""
	globals()['text'] += str(operator)
	ui.btn_clear.setEnabled(True)
	ui.OUTPUT.setText(globals()['text'])

def res():
	try: res = eval(globals()['text'])
	except: res = "ERROR!!!"
	ui.OUTPUT.setText(str(res))
	globals()['text'] = "OUTPUT"

def clear():
	globals()['text'] = ""
	ui.OUTPUT.setText(globals()['text'])
	ui.btn_clear.setEnabled(False)

def text_changed(text):
	ui.OUTPUT.setText(text)
	globals()['text'] = text
	ui.btn_clear.setEnabled(True)

ui.btn1.clicked.connect(lambda: add_number(1))
ui.btn2.clicked.connect(lambda: add_number(2))
ui.btn3.clicked.connect(lambda: add_number(3))
ui.btn4.clicked.connect(lambda: add_number(4))
ui.btn5.clicked.connect(lambda: add_number(5))
ui.btn6.clicked.connect(lambda: add_number(6))
ui.btn7.clicked.connect(lambda: add_number(7))
ui.btn8.clicked.connect(lambda: add_number(8))
ui.btn9.clicked.connect(lambda: add_number(9))
ui.btn0.clicked.connect(lambda: add_number(0))

ui.btn_plus.clicked.connect(lambda: add_operation("+"))
ui.btn_minus.clicked.connect(lambda: add_operation("-"))
ui.btn_division.clicked.connect(lambda: add_operation("/"))
ui.btn_multiplication.clicked.connect(lambda: add_operation("*"))

ui.btn_equals.clicked.connect(res)
ui.btn_clear.clicked.connect(clear)

ui.OUTPUT.textChanged.connect(text_changed)

# Run main loop
sys.exit(app.exec_())