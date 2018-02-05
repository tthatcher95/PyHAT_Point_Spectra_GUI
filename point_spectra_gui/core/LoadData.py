import pandas as pd
from PyQt5 import QtWidgets
from libpysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.LoadData import Ui_loadData
from point_spectra_gui.util.Modules import Modules


class LoadData(Ui_loadData, Modules):
    """
    Loads the data into the UI.
    The data needs to be a *.csv in order for this application to work
    """

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.fileNameLineEdit))

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def setup(self):
        params = self.getGuiParams()
        self.filename = params['fileNameLineEdit']
        self.keyname = params['dataSetNameLineEdit']
        if self.keyname not in self.datakeys:
            self.datakeys.append(self.keyname)
        else:
            pass
            # TODO we really should be checking when the user is using the same name for their datasets, however this should be done at run()
            # print("That data set name is already in use. Try something else?")

    def run(self):
        self.setup()
        print('Loading data file: ' + str(self.filename))
        # TODO: `header=[0,1]` will most likely make the code brittle, better alternative?
        self.data[self.keyname] = spectral_data(pd.read_csv(self.filename, header=[0, 1], verbose=True))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LoadData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
