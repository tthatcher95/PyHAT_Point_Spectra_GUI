from PyQt5 import QtWidgets,QtCore
from sklearn.linear_model import ElasticNet
import numpy as np
from point_spectra_gui.ui.cv_ElasticNet import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, ElasticNet, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.updateWidget()

    def get_widget(self):
        return self.elasticNetGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def updateWidget(self):
        en = ElasticNet()

        self.minalpha_spin.setValue(0.0000001)
        self.maxalpha_spin.setValue(0.01)
        self.nalpha_spin.setValue(100)

        self.enl1_ratioLineEdit.setText('0.1, 0.5, 0.7, 0.9, 0.95, 0.99, 1.0')
        self.enfit_intercept_list.setCurrentItem(self.enfit_intercept_list.findItems(str(en.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.ennormalize_list.setCurrentItem(self.ennormalize_list.findItems(str(en.normalize),QtCore.Qt.MatchExactly)[0])
        #self.enprecomputeCheckBox.setChecked(en.precompute)
        self.enmax_iterLineEdit.setText(str(en.max_iter))
        #self.encopy_XCheckBox.setChecked(en.copy_X)
        self.entolLineEdit.setText(str(en.tol))
        self.enwarm_start_list.setCurrentItem(self.enwarm_start_list.findItems(str(en.warm_start),QtCore.Qt.MatchExactly)[0])
        self.enpositive_list.setCurrentItem(self.enpositive_list.findItems(str(en.positive),QtCore.Qt.MatchExactly)[0])
        #self.setComboBox(self.enselectionComboBox, ['cyclic', 'random'])
        #self.defaultComboItem(self.enselectionComboBox, en.selection)


    def run(self):
        fit_intercept_items = [i.text() == 'True' for i in self.enfit_intercept_list.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.ennormalize_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.enpositive_list.selectedItems()]
        alphas = np.logspace(np.log10(self.minalpha_spin.value()), np.log10(self.maxalpha_spin.value()),
                             num=self.nalpha_spin.value())
        params = {
            'alpha': alphas,
            'l1_ratio': [float(i) for i in self.enl1_ratioLineEdit.text().split(',')],
            'fit_intercept': fit_intercept_items,
            'normalize': normalize_items,
            'precompute': [True],
            'max_iter': [int(i) for i in self.enmax_iterLineEdit.text().split(',')],
            'copy_X': [True],
            'tol': [float(i) for i in self.entolLineEdit.text().split(',')],
            'warm_start': [True],
            'positive': positive_items,
            'selection': ['random']}

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
