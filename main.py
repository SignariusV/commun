from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("mydesign.ui")  # расположение вашего файла .ui
win.setWindowTitle('Расчет стоимости коммунальных услуг')



def process():
    gas_cur = float(win.lineEdit.text())
    water_cur=float(win.lineEdit_6.text())
    electr_cur=float(win.lineEdit_11.text())

    gas_prev = float(win.lineEdit_2.text())
    water_prev = float(win.lineEdit_7.text())
    electr_prev = float(win.lineEdit_12.text())

    gas_dif=gas_cur-gas_prev
    water_dif=water_cur-water_prev
    electr_dif=electr_cur-electr_prev
    if electr_dif>150:
        electr_dif_1=150.0
        electr_dif_2=electr_dif-150
    else:
        electr_dif_1 = electr_dif
        electr_dif_2 = 0

    win.lineEdit_3.setText(str(gas_dif))
    win.lineEdit_8.setText(str(water_dif))
    win.lineEdit_13.setText(str(electr_dif_1))
    win.lineEdit_16.setText(str(electr_dif_2))

    gas_tarif=float(win.lineEdit_4.text())
    water_tarif = float(win.lineEdit_9.text())
    electr_tarif_1 = float(win.lineEdit_18.text())
    electr_tarif_2 = float(win.lineEdit_19.text())

    gas_total=gas_tarif*gas_dif
    water_total=water_tarif*water_dif
    electr_total=electr_tarif_1*electr_dif_1+electr_tarif_2*electr_dif_2
    communal_total=float(win.lineEdit_20.text())
    summary=gas_total+water_total+electr_total+communal_total

    win.lineEdit_5.setText(str(gas_total))
    win.lineEdit_10.setText(str(water_total))
    win.lineEdit_15.setText(str(electr_total))
    win.lineEdit_21.setText(str(summary))

win.pushButton.clicked.connect(process)

win.show()
sys.exit(app.exec())
