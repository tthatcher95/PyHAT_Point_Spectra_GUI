from PyQt5 import QtWidgets

from point_spectra_gui.ui.Interpolation import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Interpolation(Ui_Form, Modules):
    """
    Interpolates two datasets
    """

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def updateWidgets(self):
        self.setComboBox(self.interpolateDataComboBox, self.datakeys)
        self.setComboBox(self.referenceDataComboBox, self.datakeys)
        [self.interpolateDataComboBox.currentIndexChanged.connect(x) for x in [self.setCurrentData, self.set_data_idx]]

    def connectWidgets(self):
        pass

    def run(self):
        datakey_to_interp = self.interpolateDataComboBox.currentText()
        datakey_ref = self.referenceDataComboBox.currentText()
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            print(e)

    def __init__(self, _):
        self.data_idx = 0

    def set_data_idx(self, val):
        self.data_idx = val

    def refresh(self):
        # Repopulating the combobox sets idx to 0 and loses info. There has to be
        # a better way to do this.
        tmp = self.data_idx
        self.setComboBox(self.interpolateDataComboBox, self.datakeys)
        self.data_idx = tmp
        self.setDataBox(self.data_idx)

    def setDataBox(self, datakey):
        try:
            if isinstance(datakey, str):
                self.interpolateDataComboBox.setCurrentIndex(self.interpolateDataComboBox.findText(self.current_data))
            elif isinstance(datakey, int):
                self.interpolateDataComboBox.setCurrentIndex(datakey)
        except IndexError:
            self.interpolateDataComboBox.setCurrentIndex(-1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Interpolation()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
