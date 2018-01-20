from PyQt5 import QtWidgets, QtCore
from sklearn.svm.classes import SVR

from point_spectra_gui.ui.cv_SVR import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.updateWidget()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidget(self):
        pass

    def updateWidget(self):
        svr = SVR()
        self.cLineEdit.setText(str(svr.C))
        self.epsilonLineEdit.setText(str(svr.epsilon))
        self.kernel_list.setCurrentItem(self.kernel_list.findItems('Radial Basis Function', QtCore.Qt.MatchExactly)[0])
        self.degreeLineEdit.setText(str(svr.degree))
        self.coeff0LineEdit.setText(str(svr.coef0))
        self.shrinking_list.setCurrentItem(self.shrinking_list.findItems(str(svr.shrinking), QtCore.Qt.MatchExactly)[0])
        self.toleranceLineEdit.setText(str(svr.tol))
        self.maxIterationsLineEdit.setText(str(svr.max_iter))

    def run(self):
        kernels = [str(i.text()) for i in self.kernel_list.selectedItems()]
        shrinking_items = [i.text() == 'True' for i in self.shrinking_list.selectedItems()]
        params = {'C': [float(i) for i in self.cLineEdit.text().split(',')],
                  'epsilon': [float(i) for i in self.epsilonLineEdit.text().split(',')],
                  'kernel': kernels,
                  'degree': [int(i) for i in self.degreeLineEdit.text().split(',')],
                  'gamma': ['auto'],
                  'coef0': [float(i) for i in self.coeff0LineEdit.text().split(',')],
                  'shrinking': shrinking_items,
                  'tol': [float(i) for i in self.toleranceLineEdit.text().split(',')],
                  'cache_size': [200],
                  'verbose': [True],
                  'max_iter': [int(i) for i in self.maxIterationsLineEdit.text().split(',')]}
        modelkey = str(params)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
