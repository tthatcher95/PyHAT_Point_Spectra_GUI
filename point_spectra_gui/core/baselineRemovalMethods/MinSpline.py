from PyQt5 import QtWidgets
from libpyhat.transform.baseline_code.min_spline import minimum_spline
from point_spectra_gui.ui.MinSpline import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass


    def run(self):
        methodParameters = {'window': self.winsizeSpin.value()}

        return methodParameters, self.getChangedValues(methodParameters, minimum_spline())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
