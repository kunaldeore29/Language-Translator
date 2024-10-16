# Instructions:
#1. Copy the script into a file named install_packages.py.

#2. Open a terminal or command prompt.

#3. Navigate to the directory where you saved the script.

#4. Run the script using Python
# Command - python install_packages.py
import subprocess
import sys

# List of packages to install with their versions
packages = [
    "asttokens==2.4.1",
    "certifi==2024.8.30",
    "chardet==3.0.4",
    "charset-normalizer==3.3.2",
    "colorama==0.4.6",
    "comm==0.2.1",
    "comtypes==1.4.7",
    "debugpy==1.8.0",
    "decorator==5.1.1",
    "executing==2.0.1",
    "forex-python==1.8",
    "googletrans==4.0.0rc1",
    "h11==0.9.0",
    "h2==3.2.0",
    "hpack==3.0.0",
    "hstspreload==2024.9.1",
    "httpcore==0.9.1",
    "httpx==0.13.3",
    "hyperframe==5.2.0",
    "idna==2.10",
    "ipykernel==6.29.0",
    "ipython==8.20.0",
    "jedi==0.19.1",
    "jupyter_client==8.6.0",
    "jupyter_core==5.7.1",
    "matplotlib-inline==0.1.6",
    "nest-asyncio==1.5.9",
    "packaging==23.2",
    "parso==0.8.3",
    "pillow==10.4.0",
    "pip==23.2.1",
    "platformdirs==4.1.0",
    "prompt-toolkit==3.0.43",
    "psutil==5.9.7",
    "pure-eval==0.2.2",
    "PyAudio==0.2.14",
    "Pygments==2.17.2",
    "pypiwin32==223",
    "python-dateutil==2.8.2",
    "pyttsx3==2.91",
    "pywin32==306",
    "pyzmq==25.1.2",
    "requests==2.32.3",
    "rfc3986==1.5.0",
    "setuptools==65.5.0",
    "simplejson==3.19.3",
    "six==1.16.0",
    "sniffio==1.3.1",
    "SpeechRecognition==3.10.4",
    "stack-data==0.6.3",
    "tornado==6.4",
    "traitlets==5.14.1",
    "typing_extensions==4.12.2",
    "urllib3==2.2.3",
    "wcwidth==0.2.13"
]

def install_packages(packages):
    # Use pip to install each package
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

if __name__ == "__main__":
    install_packages(packages)
