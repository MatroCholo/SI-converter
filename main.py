import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

class Converter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Перевод в СИ') 
        self.setWindowIcon(QIcon('exchanging.png'))
        self.ui.input_currency.setPlaceholderText('Исходная единица измерения')
        self.ui.input_amount.setPlaceholderText('Исходное число')
        self.ui.output_amount.setPlaceholderText('Число в СИ')     
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        try:
            input_currency = self.ui.input_currency.text()
            input_amount = int(self.ui.input_amount.text())     
            if input_currency.lower() == 'г':
                output_amount = input_amount / 1000
            elif input_currency.lower() == 'ц':
                output_amount = input_amount * 100
            elif input_currency.lower() == 'мг':
                output_amount = input_amount / 1000000
            elif input_currency.lower() == 'т':
                output_amount = input_amount * 1000

            elif input_currency.lower() == 'кн':
                output_amount = input_amount * 1000
            elif input_currency == 'мн' or input_currency == 'мН':
                output_amount = input_amount / 1000
            elif input_currency == 'МН':
                output_amount = input_amount * 1000000

            elif input_currency.lower() == 'км':
                output_amount = input_amount * 1000
            elif input_currency.lower() == 'см':
                output_amount = input_amount / 100
            elif input_currency.lower() == 'дм':
                output_amount = input_amount / 10
            elif input_currency.lower() == 'мм':
                output_amount = input_amount / 1000

            elif input_currency.lower() == 'км2':
                output_amount = input_amount * 1000000
            elif input_currency.lower() == 'см2':
                output_amount = input_amount / 10000
            elif input_currency.lower() == 'дм2':
                output_amount = input_amount / 100
            elif input_currency.lower() == 'мм2':
                output_amount = input_amount / 1000000

            elif input_currency.lower() == 'км3':
                output_amount = input_amount * 1000000000
            elif input_currency.lower() == 'см3':
                output_amount = input_amount / 1000000
            elif input_currency.lower() == 'дм3' or input_currency.lower() == 'л':
                output_amount = input_amount / 1000
            elif input_currency.lower() == 'мм3':
                output_amount = input_amount / 1000000000

            elif input_currency.lower() == 'км/ч':
                output_amount = round(input_amount * 1000 / 3600, 2)
            elif input_currency.lower() == 'км/мин':
                output_amount = round(input_amount * 1000 / 60, 2)
            elif input_currency.lower() == 'км/с':
                output_amount = round(input_amount * 1000, 2)
            elif input_currency.lower() == 'м/ч':
                output_amount = round(input_amount / 3600, 2)
            elif input_currency.lower() == 'м/мин':
                output_amount = round(input_amount / 60, 2)
            elif input_currency.lower() == 'см/ч':
                output_amount = round(input_amount / 360000, 2)
            elif input_currency.lower() == 'см/мин':
                output_amount = round(input_amount / 6000, 2)
            elif input_currency.lower() == 'см/с':
                output_amount = round(input_amount / 100, 2)

            elif input_currency.lower() == 'ч':
                output_amount = input_amount * 3600
            elif input_currency.lower() == 'мин':
                output_amount = input_amount * 60
            elif input_currency.lower() == 'сутки' or input_currency.lower() == 'день':
                output_amount = input_amount * 86400
                
            else:
                output_amount = 'Не поддерживается!'
            self.ui.output_amount.setText(str(output_amount))
        except:
            output_amount = 'Возникла непредвиденная ошибка!'
            self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = Converter()
application.show()
sys.exit(app.exec())
