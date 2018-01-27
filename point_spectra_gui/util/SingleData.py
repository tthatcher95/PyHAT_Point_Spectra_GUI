from point_spectra_gui.util.Modules import Modules


class SingleData(Modules):
    def __init__(self, _):
        super().__init__()
        self.data_idx = 0

    def set_data_idx(self, val):
        self.data_idx = val

    def refresh(self):
        # Repopulating the combobox sets idx to 0 and loses info. There has to be
        # a better way to do this.
        tmp = self.data_idx
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.data_idx = tmp
        self.setDataBox(self.data_idx)

    def setDataBox(self, datakey):
        try:
            if isinstance(datakey, str):
                self.chooseDataComboBox.setCurrentIndex(self.chooseDataComboBox.findText(self.current_data))
            elif isinstance(datakey, int):
                self.chooseDataComboBox.setCurrentIndex(datakey)
        except IndexError:
            self.chooseDataComboBox.setCurrentIndex(-1)
