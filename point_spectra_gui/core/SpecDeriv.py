from PyQt5 import QtWidgets

from point_spectra_gui.ui.SpecDeriv import Ui_Form
from point_spectra_gui.util.Modules import Modules


class SpecDeriv(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataToDerivComboBox, self.datakeys)
        [self.chooseDataToDerivComboBox.currentIndexChanged.connect(x) for x in
         [self.setCurrentData, self.set_data_idx]]

    def run(self):
        datakey = self.chooseDataToDerivComboBox.currentText()
        new_datakey = datakey + ' - Derivative'
        self.datakeys.append(new_datakey)
        self.data[new_datakey] = self.data[datakey].deriv()
        print("Derivative Applied")

    def __init__(self, _):
        super().__init__()
        self.data_idx = 0

    def set_data_idx(self, val):
        self.data_idx = val

    def refresh(self):
        # Repopulating the combobox sets idx to 0 and loses info. There has to be
        # a better way to do this.
        tmp = self.data_idx
        self.setComboBox(self.chooseDataToDerivComboBox, self.datakeys)
        self.data_idx = tmp
        self.setDataBox(self.data_idx)

    def setDataBox(self, datakey):
        try:
            if isinstance(datakey, str):
                self.chooseDataToDerivComboBox.setCurrentIndex(
                    self.chooseDataToDerivComboBox.findText(self.current_data))
            elif isinstance(datakey, int):
                self.chooseDataToDerivComboBox.setCurrentIndex(datakey)
        except IndexError:
            self.chooseDataToDerivComboBox.setCurrentIndex(-1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = SpecDeriv()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
