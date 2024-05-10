# Vision
Vision code for reading 1-D and 2-D codes and OCR using OAK-D

## Installation
Follow the steps below to just install depthai api library dependencies for Windows.

For Windows 10/11, we recommend using the Chocolatey package manager to install DepthAI’s 
dependencies on Windows. Chocolatey is very similar to Homebrew for macOS.

To install [Chocolatey](https://docs.chocolatey.org/en-us/choco/setup)   and use it to install DepthAI’s dependencies do the following:

Right click on Start

Choose Windows PowerShell (Admin) and run the following:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

To install DepthAi dependancies using Python library via PyPi, open your IDE and run the following command.

```
python3 -m pip install depthai
```

## Test installation

We have a [set of examples](https://github.com/luxonis/depthai-python/tree/develop/examples) 
 that should help you verify if your setup was correct.

First, clone the depthai-python repository and change directory into this repo:

```
git clone https://github.com/luxonis/depthai-python.git
cd depthai-python
```
Next install the requirements for this repository. Note that we recommend installing the dependencies in a virtual environment, so that they don’t interfere with other Python tools/environments on your system.

For development machines like Mac/Windows/Ubuntu/etc., we recommend the PyCharm IDE, as it automatically makes/manages virtual environments for you, along with a bunch of other benefits. Alternatively, conda, pipenv, or virtualenv could be used directly (and/or with your preferred IDE).

For installations on resource-constrained systems, such as the Raspberry Pi or other small Linux systems, we recommend conda, pipenv, or virtualenv. To set up a virtual environment with virtualenv, run virtualenv venv && source venv/bin/activate.

Using a virtual environment (or system-wide, if you prefer), run the following to install the requirements for this example repository:

```
cd examples
python3 install_requirements.py
```
Now, run the rgb_preview.py script from within examples directory to make sure everything is working:

```
python3 ColorCamera/rgb_preview.py
```
