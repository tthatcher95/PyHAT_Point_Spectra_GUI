from time import sleep
from threading import Thread
from point_spectra_gui.core.MainWindow import main

t = Thread(target=main)
t.daemon = True
t.start()
sleep(10)