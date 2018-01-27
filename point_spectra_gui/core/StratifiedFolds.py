from PyQt5 import QtWidgets

from point_spectra_gui.ui.StratifiedFolds import Ui_Form
from point_spectra_gui.util.Modules import Modules


class StratifiedFolds(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.nFoldsSpinBox.setValue(2)
        self.testFoldsSpinBox.setValue(2)
        self.setComboBox(self.chooseDataToStratifyComboBox, self.datakeys)
        try:  # Some instances where perhaps there is no data to load
            data = self.data[self.chooseDataToStratifyComboBox.currentText()].df['comp'].columns.values
            self.setComboBox(self.chooseVarComboBox, data)
        except:
            pass
        self.chooseDataToStratifyComboBox.activated[int].connect(self.strat_fold_change_vars)
        self.nFoldsSpinBox.valueChanged.connect(self.strat_fold_change_testfolds)
        [self.chooseDataToStratifyComboBox.currentIndexChanged.connect(x) for x in [self.setCurrentData, self.set_data_idx]]

    def __init__(self, _):
        self.data_idx = 0

    def set_data_idx(self, val):
        self.data_idx = val

    def refresh(self):
        #Repopulating the combobox sets idx to 0 and loses info. There has to be
        # a better way to do this.
        tmp = self.data_idx
        self.setComboBox(self.chooseDataToStratifyComboBox, self.datakeys)
        self.data_idx = tmp
        self.setDataBox(self.data_idx)


    def setDataBox(self, datakey):
        try:
            if isinstance(datakey, str):
                self.chooseDataToStratifyComboBox.setCurrentIndex(self.chooseDataToStratifyComboBox.findText(self.current_data))
            elif isinstance(datakey, int):
                self.chooseDataToStratifyComboBox.setCurrentIndex(datakey)
        except IndexError:
            self.chooseDataToStratifyComboBox.setCurrentIndex(-1)




    def run(self):
        datakey = self.chooseDataToStratifyComboBox.currentText()
        nfolds = self.nFoldsSpinBox.value()
        try:
            testfold = int(self.testFoldsSpinBox.value())
        except:
            testfold = 1
        colname = ('comp', self.chooseVarComboBox.currentText())
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys.append(datakey + '-Train')
        self.datakeys.append(datakey + '-Test')

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    def strat_fold_change_vars(self):
        self.chooseVarComboBox.clear()
        try:
            choices = self.data[self.chooseDataToStratifyComboBox.currentText()].df['comp'].columns.values
        except:
            choices = ['No composition columns!']

        self.chooseVarComboBox.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.testFoldsSpinBox.clear()
        self.testFoldsSpinBox.setMaximum(self.nFoldsSpinBox.value())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = StratifiedFolds()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
