from PyQt5 import QtWidgets

from point_spectra_gui.ui.KK import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'top_width': int(self.topWidthSpinBox.value()),
                            'bottom_width': int(self.bottomWidthSpinBox.value()),
                            'tangent': self.tangentCheckBox.isChecked(),
                            'exponent': int(self.exponentSpinBox.value())}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())