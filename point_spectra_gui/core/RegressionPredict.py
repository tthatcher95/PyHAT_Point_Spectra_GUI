from PyQt5 import QtWidgets

from point_spectra_gui.ui.RegressionPredict import Ui_Form
from point_spectra_gui.util.Modules import Modules


class RegressionPredict(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)
        self.refresh()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.data)
        self.setComboBox(self.chooseModelComboBox, self.modelkeys)

    def refresh(self):
        self.connectWidgets()
        self.setDataBox(self.current_data)
        self.setModelBox(self.current_model)

    def setDataBox(self, datakey):
        try:
            self.chooseDataComboBox.setCurrentIndex(self.chooseDataComboBox.findText(datakey))
        except:
            self.chooseDataComboBox.setCurrentIndex(-1)

    def setModelBox(self, modelkey):
        try:
            self.chooseModelComboBox.setCurrentIndex(self.chooseModelComboBox.findText(modelkey))
        except:
            self.chooseModelComboBox.setCurrentIndex(-1)

    def run(self):
        datakey = self.chooseDataComboBox.currentText()
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

        self.current_data = datakey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RegressionPredict()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
