import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Currency converter')
        self.setWindowIcon(QIcon(f'content\\exchange_arrows.png'))

        self.ui.input_amount.setPlaceholderText('I have:')
        self.ui.output_amount.setPlaceholderText('I will have:')
        self.ui.pushButton.clicked.connect(self.converter)
        currencies = list({'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN',
                           'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK', 'TRY', 'AUD',
                           'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW',
                           'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR', 'EUR'})
        self.ui.comboBox.addItems(currencies)
        self.ui.comboBox_2.addItems(currencies)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.comboBox.currentText()
        input_amount = int(self.ui.input_amount.text())
        output_currency = self.ui.comboBox_2.currentText()

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec_())