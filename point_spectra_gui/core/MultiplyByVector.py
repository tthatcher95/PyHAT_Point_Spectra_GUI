from PyQt5 import QtWidgets

from point_spectra_gui.ui.MultiplyByVector import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.SingleData import SingleData


class MultiplyByVector(Ui_Form, SingleData):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def updateWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

    def connectWidgets(self):
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.vectorFileLineEdit))
        [self.chooseDataComboBox.currentIndexChanged.connect(x) for x in [self.setCurrentData, self.set_data_idx]]

    def run(self):
        datakey = self.chooseDataComboBox.currentText()
        vectorfile = self.vectorFileLineEdit.text()

        try:
            self.data[datakey].multiply_vector(vectorfile)
        except Exception as e:
            print(e)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Vector Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = MultiplyByVector()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
