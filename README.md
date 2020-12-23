# Qiskit Metal [![](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/Qiskit/qiskit-metal) [![](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/Qiskit/qiskit-metal)
>  Quantum hardware design and analysis

![Welcome to Qiskit Metal!](docs/images/zkm_banner.png 'Welcome to Qiskit Metal')

## Early Access
https://qiskit.org/metal/

This is the unpolished, early-access version for a first-of-its-kind, open-source project for engineers and scientists to design superconducting quantum devices with ease.

This early-access program will start in November and proceed through March, 2021, during which time we will work closely to develop Metal and design quantum devices with it.

Through this early-access program, we are thrilled to ask you to join this journey to revolutionize quantum devices.


###### Get help: Slack
Use the [Slack channel (Join here!)](https://join.slack.com/share/zt-jjgzilxu-1u2FGivroQi64fHajpTWiw) to communicate with other developers and  early-access participants. (Troubleshooting: If the Slack invitation has expired, request one by opening a GitHub issue.)


## Installation
#### Video Instructions


<a href="https://www.youtube.com/watch?v=sYVDtnJb-ZM&ab_channel=Qiskit">
 Click for YouTube Video <br>
	<img src="https://www.gstatic.com/youtube/img/branding/youtubelogo/svg/youtubelogo.svg" alt="Qiskit Metal Install" width=150>
</a>


### Text Instructions
Notes:

* For your own sanity, it is recommended to read this document in its entirety before proceeding.
* On Windows, the conda environment is strongly recommended because Shapely is difficult to install directly via pip.

#### Downloading
You could download the code as a zip file at the top of this page.
However we recommend investing into setting up a proper git linkage, which will simplify the retrieval of code updates and the possible contributions back to the source code.

To do that, you will need to `git clone` this repository's main branch following one of two ways.

1. Open any command line shell that has been configured with git and execute the following command:
``` sh
git clone https://github.com/Qiskit/qiskit-metal.git
```
2. Alternatively, you can download and use the user interface [GitHub Desktop GUI](https://desktop.github.com/) and refer to these [notes](https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop).

Now that you have a local copy of the code, you can install Qiskit Metal either in a virtual [conda environment](https://docs.conda.io/en/latest/miniconda.html) or in a virtual Python environment, as described below. We recommend conda.



#### Setup (Preferred)

##### Install Conda
Install Conda, a python environment manager. Please follow these [instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

For this section you will need to use the command line (or terminal). If you use github desktop, you can open one from the menu `Repository -> Open In....`


###### Create Conda Environment

First navigate to the folder created by the clone. For example:

```
cd qiskit-metal
```

If you are in the folder qiskit-metal folder, there will be an `environment.yml` file.
Create the environment and activate the environment.
```
conda env create -n <env_name> environment.yml
conda activate <env_name>
```

###### Install Qiskit Metal in Conda Environment
You must still be inside the qiskit-metal folder and have the desired conda environment activated. There is a `setup.py` file in that folder which is used when you run the code below.
```
python -m pip install -ve .
```

This creates a new environment with name `<env_name>` with all the necessary library dependencies.
Then it activates the new environment.
Finally installs the local qiskit-metal code inside that environment.


Notes:

* It is possible that you may run into version conflicts during the above installation, as qiskit-metal requires specific library versions to work correctly on every OS.
* Remember the period (".") at the end of the third command.
* **Important**: Remember to `conda activate <env_name>` if you intend to use qiskit-metal.  See what a [conda environment is](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

At this point you can already use qiskit-metal through jupyter notebook.
However, if you prefer using jupyter lab, you will need to execute a couple of extra steps.

##### (Optional) Jupyter lab

Launching jupyter lab will execute python code in the conda `base` environment by default.
To change environment to the one you just finished setting up, you will need first to "assign" the environment to a kernel label.
To do so, from a command line inside the active <env_name>, run the following lines:

```
conda install ipykernel
ipython kernel install --user --name=<any_name_for_kernel>
```

This will create a kernel for the conda environment that is active at the moment.

Once inside `jupyter lab`, switch to the newly created kernel to be able to work with qiskit-metal.

#### Alternative Setup (no Conda):
##### Virtual environment setup

**On Windows, do this first:** It is recommended that you first install `Visual C++ 14.0`, it is required for a successful install of `gdspy`.
If you do not have `Visual C++ 14.0` installed you will be notified to install it when `gdspy` attempts to install.
You can do this by downloading and installing [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
Be sure to select the latest versions of `MSVCv142 - VS 2019 C++ x64/x86 build tools` and `Windows 10 SDK` in the installer as suggested in [this wiki](https://wiki.python.org/moin/WindowsCompilers) referenced by the gdspy documentation.

To use a Python virtual environment, execute these commands in the top-level of the repository:

```
python -m venv <virtual_env_path>
source <virtual_env_path>/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt -r requirements-dev.txt -e .
```

where `<virtual_env_path>` is where you want the Python virtual environment to be installed.
On Windows, replace `source <virtual_env_path>/bin/activate` with `.\<virtual_env_path>\Scripts\activate`.


###### Installation hints

Here are some things to consider when setting up a development environment:

* If using a virtual environment, make sure `pip` is up to date. In initial environment testing, PySide2 is installable with only the latest version of `pip`.

* Add the path of your qiskit-metal folder to your PATH


### For Developers
If you are planning to develop the qiskit metal codebase, you'll want to use these instructions to [setup user environment](/docs/NEW_DEVELOPER_SETUP.md)


## Common Issues

#### pyqode/pyside
Please be aware that the environment.xml and requirements.txt each use a different `pyside` version. This is done for Windows OS users to prevent a ipython kernel crash caused by the installation of a library incompatible with `pyqode`.

For other OS users, this setup might cause `pyqode.qt` to be upgraded automatically after it is first installed. If you still observe `pyqode`-related errors, try forcing the upgrade of the pyqode.python library with `pip install pyqode.python --upgrade`.

If Windows users continue to experience GUI or other issues, try rerunning `python setup.py install` or creating a new, pristine conda environment as per above instructions. Pay particular attention to the python version, which must remain 3.7.8 for as long as qiskit-metal utilizes pyqode.

#### Jupyter Lab
If you can not start Jupyter Lab in the new environment.

Based on: https://anaconda.org/conda-forge/jupyterlab
Install Jupyter lab by
```
conda install -c conda-forge jupyterlab
```
Then change directory to top level of repository.
```
python -m pip install -e .
```

#### qutip
`qutip` may have issues finding your path if using VSCode, resulting in a `KeyError: 'physicalcpu'`. If the error occurs, please add your PATH to VSCode's settings as follows.


 ##### Windows:
 Open Windows Command Prompt and type in
 ```
 $Env:Path
 ```
Copy the resulting output. Example: `"PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"`
Then open the applicable settings.json in your VS Code. (See how to open command palette [here](https://code.visualstudio.com/docs/getstarted/tips-and-tricks). Search "settings" and click Open Workspace Settings (JSON)). Paste:
```
 "terminal.integrated.env.windows": {
        "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
        }
```

##### MacOs:
 Open Terminal and type in
 ```
echo $PATH
 ```
Copy the resulting output. Example: `"PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"`
Then open the applicable settings.json in your VS Code. (See how to open command palette [here](https://code.visualstudio.com/docs/getstarted/tips-and-tricks). Search "settings" and click Open Workspace Settings (JSON)). Paste:
```
    "terminal.integrated.env.osx": {
        "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
        }
```

## Docs and how to use

[Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

[Python Setup and Usage](https://docs.python.org/3/using/)

[Python Language Reference](https://docs.python.org/3/reference/index.html)

[Python How-To's](https://docs.python.org/3/howto/index.html)

[Python Tutorials](https://docs.python.org/3/tutorial/index.html)

[Python Style Guide](https://www.python.org/dev/peps/pep-0008/)

[Metal Docs](/docs)

[Docstring cheat sheet](/docs/docstring_cheat_sheet.md)


## Authors and Citation

Qiskit Metal is the work of [many people](https://github.com/Qiskit/qiskit-metal/pulse/monthly) who contribute to the project at different levels. Metal was conceived and developed by Zlatko Minev at IBM, then co-led with Thomas McConkey. If you use Qiskit, please cite as per the included [BibTeX file](https://github.com/Qiskit/qiskit/blob/master/Qiskit.bib).For icon attributions, see [here](/qiskit_metal/_gui/_imgs/icon_attributions.txt).


## License

[Apache License 2.0](LICENSE.txt)
