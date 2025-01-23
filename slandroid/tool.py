import subprocess
import sys
import shutil
import os
import json
import time
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

# Configuration file path
CONFIG_FILE = "slandroid.config.json"

def load_config():
    """Load configuration from the config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    """Save configuration to the config file."""
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def install_python_packages(script_path):
    """Install missing Python packages required by the script."""
    try:
        with open(script_path, "r") as file:
            lines = file.readlines()
            imports = [line.split()[1] for line in lines if line.startswith("import ") or line.startswith("from ")]
        
        for package in imports:
            try:
                __import__(package)
            except ImportError:
                print(f"Installing missing package: {package}")
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    except Exception as e:
        print(f"Error installing dependencies: {e}")

# Current version of Slandroid
CURRENT_VERSION = "0.3.5"

def check_for_updates():
    """Check if a newer version of Slandroid is available on PyPI."""
    try:
        import requests
        from packaging import version
        response = requests.get("https://pypi.org/pypi/slandroid/json")
        response.raise_for_status()
        latest_version = response.json()["info"]["version"]

        if version.parse(latest_version) > version.parse(CURRENT_VERSION):
            print(f"A new version of Slandroid is available: {latest_version}")
            return True
        else:
            print("You are using the latest version of Slandroid.")
            return False
    except Exception as e:
        print(f"Failed to check for updates: {e}")
        return False

def update_slandroid():
    """Update Slandroid to the latest version."""
    try:
        print("Updating Slandroid...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "slandroid"], check=True)
        print("Slandroid has been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update Slandroid: {e}")

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

def run_script(script_path, env_vars=None, timeout=None, output_file=None):
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

    # Prepare the command
    command = language_info["command"].split() + [script_path]

    # Set environment variables
    env = os.environ.copy()
    if env_vars:
        env.update(env_vars)

    # Run the script
    try:
        if output_file:
            with open(output_file, "w") as f:
                process = subprocess.run(command, env=env, stdout=f, stderr=subprocess.PIPE, timeout=timeout)
        else:
            process = subprocess.run(command, env=env, stdout=sys.stdout, stderr=sys.stderr, timeout=timeout)
        
        if process.returncode != 0:
            print(f"Error running script: {process.stderr.decode()}")
    except subprocess.TimeoutExpired:
        print(f"Script timed out after {timeout} seconds.")
    except Exception as e:
        print(f"Error running script: {e}")

def list_languages():
    """List all supported languages."""
    print("Supported Languages:")
    for ext, info in LANGUAGE_MAPPING.items():
        print(f"- {ext}: {info['command']}")

def show_help():
    """Display the help message."""
    print("""
Usage: slandroid [OPTIONS] <script_path>

Options:
  --install       Install dependencies without running the script.
  --verbose       Display detailed output for debugging.
  --list-languages  List all supported languages.
  --compile       Compile the script before running (for compiled languages).
  --env KEY=VALUE Set environment variables for the script.
  --timeout SEC   Set a timeout for script execution.
  --output FILE   Redirect script output to a file.
  --update        Update Slandroid to the latest version.
  --version       Display the version of slandroid.
  --help          Display this help message.
""")

def main():
    if "--help" in sys.argv:
        show_help()
        return

    if "--list-languages" in sys.argv:
        list_languages()
        return

    if "--version" in sys.argv:
        print(f"slandroid v{CURRENT_VERSION}")
        return

    if "--update" in sys.argv:
        if check_for_updates():
            update_slandroid()
        return
    
    if len(sys.argv) < 2:
        print("Usage: slandroid <script_path>")
        return

    script_path = sys.argv[-1]
    env_vars = {}
    timeout = None
    output_file = None

    for i, arg in enumerate(sys.argv):
        if arg == "--env" and i + 1 < len(sys.argv):
            key, value = sys.argv[i + 1].split("=")
            env_vars[key] = value
        elif arg == "--timeout" and i + 1 < len(sys.argv):
            timeout = int(sys.argv[i + 1])
        elif arg == "--output" and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]

    run_script(script_path, env_vars, timeout, output_file)

if __name__ == "__main__":
    main()