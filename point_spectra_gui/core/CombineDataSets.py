# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.
import pandas as pd
from PyQt5 import QtWidgets

from point_spectra_gui.ui.CombineDataSets import Ui_Form
from point_spectra_gui.util.Modules import Modules


class CombineDataSets(Ui_Form, Modules):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.dataSet1ComboBox, self.datakeys)
        self.setComboBox(self.dataSet2ComboBox, self.datakeys)
        self.setComboBox(self.outputToDataSetComboBox, self.datakeys)

    # @@TODO ask which values should be propagated
    def refresh(self):
        pass

    def run(self):
        dataSet1 = self.dataSet1ComboBox.currentText()
        dataSet2 = self.dataSet2ComboBox.currentText()
        dataIn = self.outputToDataSetComboBox.currentText()
        self.data[dataIn] = pd.concat([dataSet1, dataSet2])
        self.setCurrentData(dataIn)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
