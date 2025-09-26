import subprocess
import sys

libraries = [
    "numpy",
    "matplotlib",
    "tensorflow",
    "scikit-learn",
    "yfinance"
]

for library in libraries:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print(f"{library} installed successfully.")
    except Exception as e:
        print(f"Error installing {library}: {e}")


print("\n\nIf any libraries did not install, please go to your terminal and install them manually using:\npip install LIBRARY ")
