import os
import pytest
import numpy as np
from pandas.util.testing import assert_frame_equal
import pandas as pd

from PyQt5 import QtCore, QtWidgets
from point_spectra_gui.util.spectral_data import spectral_data

from point_spectra_gui import core
from point_spectra_gui.core.CombineDataSets import CombineDataSets



def test_combine_datasets(qtbot):
    form = QtWidgets.QWidget()
    gui = CombineDataSets()
    gui.setupUi(form)

    key1 = 'test1'
    key2 = 'test2'
    outkey = 'data'

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    filename = os.path.join(__location__, 'dataset.csv')

    gui.data[key1] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=True))
    gui.data[key2] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=True))

    gui.dataSet1ComboBox.addItem(key1)
    gui.dataSet1ComboBox.setItemText(0, key1)
    gui.dataSet2ComboBox.addItem(key2)
    gui.dataSet2ComboBox.setItemText(0, key2)
    gui.outputToDataSetLineEdit.setText(outkey)

    gui.run()

    print(gui.dataSet1ComboBox.currentText(),gui.dataSet2ComboBox.currentText())
    print(gui.data)

    try:
        assert_frame_equal(gui.data['data'].df, spectral_data(pd.concat([gui.data[key1].df, gui.data[key2].df])).df)
        assert True
    except:
        assert False
