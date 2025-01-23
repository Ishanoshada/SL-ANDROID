import subprocess
import sys
import shutil
from pathlib import Path

# Mapping of file extensions to their respective language interpreters
LANGUAGE_MAPPING = {
    ".py": {"command": "python", "install": "pip install"},
    ".js": {"command": "node", "install": "npm install -g"},
    ".sh": {"command": "bash", "install": None},
    ".rb": {"command": "ruby", "install": "gem install"},
    ".java": {"command": "java", "install": None},
    ".go": {"command": "go run", "install": "go install"},
    ".php": {"command": "php", "install": "sudo apt install php"},
    ".pl": {"command": "perl", "install": "sudo apt install perl"},
    ".c": {"command": "gcc", "install": "sudo apt install gcc"},
    ".cpp": {"command": "g++", "install": "sudo apt install g++"},
    ".rs": {"command": "rustc", "install": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"},
    ".ts": {"command": "ts-node", "install": "npm install -g ts-node"},
    ".ps1": {"command": "pwsh", "install": "sudo apt install powershell"},
    ".lua": {"command": "lua", "install": "sudo apt install lua5.3"},
    ".r": {"command": "Rscript", "install": "sudo apt install r-base"},
    ".swift": {"command": "swift", "install": "sudo apt install swift"},
    ".kt": {"command": "kotlin", "install": "sudo apt install kotlin"},
    ".dart": {"command": "dart", "install": "sudo apt install dart"},
    ".hs": {"command": "runhaskell", "install": "sudo apt install haskell-platform"},
    ".exs": {"command": "elixir", "install": "sudo apt install elixir"},
}

def install_python_packages(script_path):
    """Install missing Python packages required by the script."""
    try:
        # Extract imports from the script
        with open(script_path, "r") as file:
            lines = file.readlines()
            imports = [line.split()[1] for line in lines if line.startswith("import ") or line.startswith("from ")]
        
        # Install missing packages
        for package in imports:
            try:
                __import__(package)
            except ImportError:
                print(f"Installing missing package: {package}")
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    except Exception as e:
        print(f"Error installing dependencies: {e}")

def detect_language(script_path):
    """Detect the language based on the file extension."""
    ext = Path(script_path).suffix
    return LANGUAGE_MAPPING.get(ext)

def install_interpreter(language_info):
    """Install the required interpreter or runtime."""
    if language_info["install"]:
        print(f"Installing {language_info['command']}...")
        try:
            subprocess.run(language_info["install"].split(), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {language_info['command']}: {e}")
            return False
    return True

def run_script(script_path):
    """Run the script using the appropriate interpreter."""
    language_info = detect_language(script_path)
    if not language_info:
        print(f"Unsupported file type: {Path(script_path).suffix}")
        return

    # Check if the interpreter is installed
    if not shutil.which(language_info["command"].split()[0]):
        print(f"{language_info['command']} is not installed.")
        if not install_interpreter(language_info):
            print(f"Please install {language_info['command']} manually and try again.")
            return

    # For Python scripts, install missing dependencies
    if language_info["command"] == "python":
        install_python_packages(script_path)

    # Run the script
    try:
        command = language_info["command"].split() + [script_path]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
    except FileNotFoundError:
        print(f"Script file not found: {script_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: slandroid <script_path>")
    else:
        run_script(sys.argv[1])

if __name__ == "__main__":
    main()