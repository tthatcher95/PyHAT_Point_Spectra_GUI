import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.ui.Lookup import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.spectral_data import spectral_data
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
        self.setComboBox(self.left_on,[''])
        self.choosedata.currentIndexChanged.connect(lambda: self.setComboBox(self.left_on,self.data[self.choosedata.currentText()].df['meta'].columns.values))
        self.filebrowse.clicked.connect(self.on_filebrowse_clicked)
        self.lookupfile.textChanged.connect(self.read_lookupdata)

    def read_lookupdata(self):
        self.lookupdata = pd.read_csv(self.lookupfilename)
        self.setComboBox(self.right_on,self.lookupdata.columns.values)

    def on_filebrowse_clicked(self):
        self.lookupfilename, null = QtWidgets.QFileDialog.getOpenFileNames(parent=None,
                                                                          caption="Select metadata file",
                                                                          directory='.')
        self.lookupfile.setText(str(self.lookupfilename))


    def setup(self):
        # TODO this file needs to be redone to fit the similar setup to `LoadData`
        pass

    def run(self):
        data =self.data[self.choosedata.currentText()]
        data = spectral_data(
            lookup.lookup(data.df, lookupdf=self.lookupdata, left_on=self.left_on.currentText(), right_on=self.right_on.currentText()))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Lookup()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
