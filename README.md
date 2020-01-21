| OSX   | [![Build Status](https://travis-ci.org/USGS-Astrogeology/PyHAT_Point_Spectra_GUI.svg?branch=master)](https://travis-ci.org/USGS-Astrogeology/PyHAT_Point_Spectra_GUI) |
|Linux  | [![Build Status](https://travis-ci.org/USGS-Astrogeology/PyHAT_Point_Spectra_GUI.svg?branch=master)](https://travis-ci.org/USGS-Astrogeology/PyHAT_Point_Spectra_GUI) |
|Windows| [![Build status](https://ci.appveyor.com/api/projects/status/orfb1txhicspo7ap/branch/master?svg=true)](https://ci.appveyor.com/project/jlaura/pyhat-point-spectra-gui/branch/dev)|

[![Coverage Status](https://coveralls.io/repos/github/Kelvinrr/pyhat_Point_Spectra_GUI/badge.svg?branch=master)](https://coveralls.io/github/Kelvinrr/pyhat_Point_Spectra_GUI?branch=master)
[![Join the chat at https://gitter.im/USGS-Astrogeology/pyhat](https://badges.gitter.im/USGS-Astrogeology/pyhat.svg)](https://gitter.im/USGS-Astrogeology/pyhat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



## Installation


### 1. Install Anaconda (Skip to step 2 if you have Anaconda/Miniconda)

Install <a href="https://www.anaconda.com/download/">Anaconda</a>.


### 2. Open a terminal (on Windows, use the Anaconda prompt that gets installed with Anaconda) and type:

```bash
conda --v # this will give you your version, make sure it is 4 or greater, if not use the below command
conda install conda=4  # SKIP THIS LINE ON WINDOWS
conda env create -n ppsg # This creates a new environment named ppsg. Substitute your preferred name if desired.
conda install -c usgs-astrogeology ppsg # This installs the PyHAT Point Spectra GUI (ppsg) package from Anaconda
```

### 4. Done! How to use point_spectra_gui
From the terminal type:

```bash
conda activate ppsg  # This activates the environment where the tool is installed
point_spectra_gui # This runs the GUI
```

### 5. Update an existing installation

If you already have an earlier version of the PyHAT Point Spectra GUI installed as described above and you want to wipe it and update to the latest version, just do:

```bash
conda env remove -n point_spectra_gui
```
And then follow the instructions above to install a fresh version.

# Bugs

## Run into bugs or features that are missing? Let us know by reporting an issue!

# pyhat UI
![pyhat splash](./images/splash.png)  

- The UI's backend is designed and created in Python with the QT framework


