from PyQt5 import QtWidgets

from point_spectra_gui.ui.RestoreTrainedModel import Ui_Form
from point_spectra_gui.util.Modules import Modules


class RestoreTrainedModel(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.retorePushButton.clicked.connect(lambda: self.on_restorePushButton_clicked(self.restoreLineEdit))

    def setup(self):
        pass

    def run(self):
        #
        pass

    def on_restorePushButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.tram)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.tram")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RestoreTrainedModel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
