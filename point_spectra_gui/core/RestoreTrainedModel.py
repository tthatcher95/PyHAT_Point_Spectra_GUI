import pickle

from PyQt5 import QtWidgets, QtGui

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

    def run(self):
        # load pickled data
        self.modelkeys = pickle.load(self.filename)
        pass

    def on_restorePushButton_clicked(self, lineEdit):
        # list[0] will hold the dictionary data of the UI
        # list[1] will hole the self.models data
        # load the json file into the restoreTextBrowser

        self.filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.tram)")
        lineEdit.setText(self.filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.tram")
        try:
            # Load the json file into the restoreTextBrowser to be viewed
            pass
        except:
            pass

    def display(self, text):
        cursor = self.restoreTextBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.restoreTextBrowser.setTextCursor(cursor)
        self.restoreTextBrowser.ensureCursorVisible()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RestoreTrainedModel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
