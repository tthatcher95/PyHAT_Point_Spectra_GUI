from PyQt5 import QtWidgets

from point_spectra_gui.ui.RegressionPredict import Ui_Form
from point_spectra_gui.util.Modules import Modules


class RegressionPredict(Ui_Form, Modules):
    """
    You will need to have ran the RegressionTrain module for this to work.
    """

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def updateWidgets(self):
        self.setListWidget(self.chooseDataListWidget, self.data)
        self.setComboBox(self.chooseModelComboBox, self.modelkeys)

    def connectWidgets(self):
        pass

    def run(self):
        datakey = [i.text() == 'True' for i in self.chooseDataListWidget.selectedItems()]
        modelkey = self.chooseModelComboBox.currentText()
        predictname = ('predict', modelkey + ' - ' + datakey + ' - Predict')

        data_tmp = self.data[datakey].df[self.model_xvars[modelkey]]
        data_tmp.fillna(value=0, inplace=True)
        try:
            prediction = self.models[modelkey].predict(data_tmp)
            self.data[datakey].df[predictname] = prediction
            pass
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RegressionPredict()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
