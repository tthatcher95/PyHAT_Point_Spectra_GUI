import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util import Qtickle
from libpysat.regression import regression
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.core.regressionMethods import *
from point_spectra_gui.ui.LocalRegression import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LassoCV
from sklearn.model_selection import GroupKFold

class LocalRegression(Ui_Form, Modules):
    count = -1

    def __init__(self):
        LocalRegression.count += 1
        self.curr_count = LocalRegression.count

    def delete(self):
        try:
            LocalRegression.count -= 1
            del self.models[self.modelkeys[-1]]
            del self.modelkeys[-1]
        except:
            pass

        LocalRegression.count -= 1
        self.modelkeys = self.modelkeys[:-1]

    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupLayout

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        #print(alg)
        try:
            self.alg[alg].setHidden(False)
        except:
            pass

    def connectWidgets(self):
        self.setComboBox(self.choosedata_train, self.datakeys)
        self.setComboBox(self.choosedata_predict, self.datakeys)
        self.changeComboListVars(self.yVariableList, self.yvar_choices())
        self.changeComboListVars(self.xVariableList, self.xvar_choices())
        self.xvar_choices()
        self.choosedata_train.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.yVariableList, self.yvar_choices()))
        self.choosedata_train.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.xVariableList, self.xvar_choices()))

    def setup(self):
        pass

    def run(self):
        method = 'Local '+self.chooseAlgorithmComboBox.currentText()
        xvars = [str(x.text()) for x in self.xVariableList.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.yVariableList.selectedItems()]
        fit_intercept = self.fit_intercept.isChecked()
        force_positive = self.forcepositive.isChecked()

        traindata = self.data[self.choosedata_train.currentText()]
        predictdata = self.data[self.choosedata_predict.currentText()]

        x_predict = predictdata.df[xvars]
        neighbors = NearestNeighbors(n_neighbors=self.n_neighbors_spin.value())
        neighbors.fit(traindata.df[xvars])
        predictions = []
        coeffs = []
        for i in range(x_predict.shape[0]):
            print('Predicting spectrum ' + str(i+1))
            x_temp = np.array(x_predict.iloc[i])
            foo, ind = neighbors.kneighbors([x_temp])
            local_training_data = traindata.df.iloc[np.squeeze(ind)]
            cv = GroupKFold(n_splits=3)
            cv = cv.split(local_training_data[xvars], local_training_data[yvars],
                          groups=local_training_data[yvars])
            local_lasso = LassoCV(fit_intercept=fit_intercept, n_jobs=-1, max_iter=10000, cv=cv, positive=force_positive)
            local_lasso.fit(local_training_data[xvars], local_training_data[yvars])
            predictions.append(local_lasso.predict([x_temp])[0])
            coeffs.append(local_lasso.coef_)

            try:
                coef = np.squeeze(local_lasso.coef_)
                coef = pd.DataFrame(coef)
                coef.index = pd.MultiIndex.from_tuples(self.data[self.choosedata_predict.currentText()].df[xvars].columns.values)
                coef = coef.T
                coef[('meta', 'Local LASSO')] = str(i+1)
                try:
                    coef[('meta', 'Intercept')] = local_lasso.intercept_
                except:
                    pass
                try:
                    self.data['Model Coefficients'] = spectral_data(pd.concat([self.data['Model Coefficients'].df, coef]))
                except:
                    self.data['Model Coefficients'] = spectral_data(coef)
                    self.datakeys.append('Model Coefficients')
            except:
                pass


        predictname = ('predict', 'Local LASSO - ' + self.choosedata_predict.currentText() + ' - Predict')
        self.data[self.choosedata_predict.currentText()].df[predictname] = predictions

    def yvar_choices(self):
        try:
            yvarchoices = self.data[self.choosedata_train.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.choosedata_train.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LocalRegression()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
