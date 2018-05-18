import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.ui.Lookup import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.io import lookup
from point_spectra_gui.util.spectral_data import spectral_data

class Lookup(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.choosedata, self.datakeys)
        try:
            self.setComboBox(self.left_on,self.data[self.choosedata.currentText()].df['meta'].columns.values)
        except:
            self.setComboBox(self.left_on, [''])
        #self.lookupfilename = self.lookupfile.text()
        self.choosedata.currentIndexChanged.connect(self.set_left_on)
        self.filebrowse.clicked.connect(self.on_filebrowse_clicked)
        self.lookupfile.textChanged.connect(self.read_lookupdata)
        self.skiprows_spin.valueChanged.connect(self.read_lookupdata)

    def set_left_on(self):
        try:
            left_on_choices = self.data[self.choosedata.currentText()].df['meta'].columns.values
            self.setComboBox(self.left_on, left_on_choices)
        except:
            pass


    def read_lookupdata(self):
        try:
            self.lookupdata = pd.read_csv(self.lookupfilename[0],skiprows=self.skiprows_spin.value())
            self.setComboBox(self.right_on, self.lookupdata.columns.values)
        except:
            pass


    def on_filebrowse_clicked(self):
        self.lookupfilename, null = QtWidgets.QFileDialog.getOpenFileNames(parent=None,
                                                                          caption="Select metadata file",
                                                                          directory='.')
        self.lookupfile.setText(str(self.lookupfilename[0]))


    def setup(self):
        # TODO this file needs to be redone to fit the similar setup to `LoadData`
        pass

    def run(self):
        self.lookupfilename = self.lookupfile.text()
        self.read_lookupdata()
        data =self.data[self.choosedata.currentText()]
        data = spectral_data(
            lookup.lookup(data.df, lookupdf=self.lookupdata, left_on=self.left_on.currentText(), right_on=self.right_on.currentText()))
        self.data[self.choosedata.currentText()] = data


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Lookup()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
