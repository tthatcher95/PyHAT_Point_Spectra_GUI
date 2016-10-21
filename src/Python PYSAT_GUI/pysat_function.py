from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QThread

def error_print(message):
    """
    Warning Message Box
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

class pysat_func(object):
    def __init__(self):
        self.data = {}
        self.data_keys = []

    def set_file_outpath(self, outpath):
        try:
            self.outpath = outpath
            print("Output path folder has been set")
        except Exception as e:
            error_print(e)

    def get_data(self, filename, keyname):
        try:
            print('Loading data file: ' + str(filename))
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1]))
            self.data_keys.append(keyname)
        except Exception as e:
            error_print("Problem reading data: {}".format(e))

    def set_interp(self, data1, data2):
        try:
            data1.interp(data2.df['wv1'].columns)
            print("Interpolation has been applied")
        except Exception as e:
            error_print(e)

    def set_mask(self, data):
        pass

    def do_strat_folds(self, datakey=None, nfolds=None, testfold=None, colname=None):
        try:
            self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)
            self.data[datakey+'-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
            self.data[datakey+'-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
            print(self.data.keys())
            print(self.data[datakey+'-Test'].df.index.shape)
            print(self.data[datakey+'-Train'].df.index.shape)
        except Exception as e:
            error_print(e)


    def set_testfold(self):
        try:
            return self.testfold_test
        except Exception as e:
            error_print(e)


    def set_compranges(self, compranges):
        try:
            self.compranges = compranges
            print("{}".format(compranges))
            print("Submodel ranges has been applied")
        except Exception as e:
            error_print(e)


    def get_number_components(self, ncs):
        # ncs = [7, 7, 5, 9]
        try:
            self.ncs = ncs
            print("{}".format(ncs))
            print("Applying components")
        except Exception as e:
            error_print(e)


    def set_sm(self):
        self.sm = pls_sm()


    def get_sm_fit(self):
        print("Beginning SM fit")
        self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, figpath=self.outpath)
        self.predictions_train = self.sm.predict(self.traindata)
        self.predictions_test = self.sm.predict(self.testdata)
        self.blended_train = self.sm.do_blend(self.predictions_train, self.traindata[0]['meta'][self.el])
        self.blended_test = self.sm.do_blend(self.predictions_test)
        print("Finishing up...")


    def get_plots(self):
        print("Now outputting plots to output folder")
        self.sm.final(self.testdata[0]['meta'][self.el],
                      self.blended_test,
                      el=self.el,
                      xcol='Ref Comp Wt. %',
                      ycol='Predicted Comp Wt. %',
                      figpath=self.outpath)
        print("All finished")

