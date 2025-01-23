import subprocess
import sys
import shutil
import os
import json
import time
from pathlib import Path

# Mapping of file extensions to their respective language interpreters
LANGUAGE_MAPPING = {
    # Python
    ".py": {
        "command": "python",
        "install": {
            "linux": "sudo apt install python3",
            "macos": "brew install python",
            "windows": "choco install python",
        },
    },

    ".sa": {
        "command": "python",
        "install": {
            "linux": "sudo apt install python3",
            "macos": "brew install python",
            "windows": "choco install python",
        },
    },
    
    # JavaScript (Node.js)
    ".js": {
        "command": "node",
        "install": {
            "linux": "sudo apt install nodejs",
            "macos": "brew install node",
            "windows": "choco install nodejs",
        },
    },
    
    # Bash
    ".sh": {
        "command": "bash",
        "install": None,  # Bash is pre-installed on most systems
    },
    
    # Ruby
    ".rb": {
        "command": "ruby",
        "install": {
            "linux": "sudo apt install ruby",
            "macos": "brew install ruby",
            "windows": "choco install ruby",
        },
    },
    
    # Java
    ".java": {
        "command": "java",
        "install": {
            "linux": "sudo apt install default-jdk",
            "macos": "brew install openjdk",
            "windows": "choco install jdk8",
        },
    },
    
    # Go
    ".go": {
        "command": "go run",
        "install": {
            "linux": "sudo apt install golang",
            "macos": "brew install go",
            "windows": "choco install golang",
        },
    },
    
    # PHP
    ".php": {
        "command": "php",
        "install": {
            "linux": "sudo apt install php",
            "macos": "brew install php",
            "windows": "choco install php",
        },
    },
    
    # Perl
    ".pl": {
        "command": "perl",
        "install": {
            "linux": "sudo apt install perl",
            "macos": "brew install perl",
            "windows": "choco install strawberryperl",
        },
    },
    
    # C
    ".c": {
        "command": "gcc",
        "install": {
            "linux": "sudo apt install gcc",
            "macos": "brew install gcc",
            "windows": "choco install mingw",
        },
    },
    
    # C++
    ".cpp": {
        "command": "g++",
        "install": {
            "linux": "sudo apt install g++",
            "macos": "brew install gcc",
            "windows": "choco install mingw",
        },
    },
    
    # Rust
    ".rs": {
        "command": "rustc",
        "install": {
            "linux": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "macos": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "windows": "choco install rust",
        },
    },
    
    # TypeScript
    ".ts": {
        "command": "ts-node",
        "install": {
            "linux": "npm install -g ts-node",
            "macos": "npm install -g ts-node",
            "windows": "npm install -g ts-node",
        },
    },
    
    # PowerShell
    ".ps1": {
        "command": "pwsh",
        "install": {
            "linux": "sudo apt install powershell",
            "macos": "brew install powershell",
            "windows": "choco install powershell-core",
        },
    },
    
    # Lua
    ".lua": {
        "command": "lua",
        "install": {
            "linux": "sudo apt install lua5.3",
            "macos": "brew install lua",
            "windows": "choco install lua",
        },
    },
    
    # R
    ".r": {
        "command": "Rscript",
        "install": {
            "linux": "sudo apt install r-base",
            "macos": "brew install r",
            "windows": "choco install r.project",
        },
    },
    
    # Swift
    ".swift": {
        "command": "swift",
        "install": {
            "linux": "sudo apt install swift",
            "macos": "brew install swift",
            "windows": "choco install swift",
        },
    },
    
    # Kotlin
    ".kt": {
        "command": "kotlin",
        "install": {
            "linux": "sudo apt install kotlin",
            "macos": "brew install kotlin",
            "windows": "choco install kotlin",
        },
    },
    
    # Dart
    ".dart": {
        "command": "dart",
        "install": {
            "linux": "sudo apt install dart",
            "macos": "brew install dart",
            "windows": "choco install dart-sdk",
        },
    },
    
    # Haskell
    ".hs": {
        "command": "runhaskell",
        "install": {
            "linux": "sudo apt install haskell-platform",
            "macos": "brew install ghc",
            "windows": "choco install haskell-dev",
        },
    },
    
    # Elixir
    ".exs": {
        "command": "elixir",
        "install": {
            "linux": "sudo apt install elixir",
            "macos": "brew install elixir",
            "windows": "choco install elixir",
        },
    },
    
    # Scala
    ".scala": {
        "command": "scala",
        "install": {
            "linux": "sudo apt install scala",
            "macos": "brew install scala",
            "windows": "choco install scala",
        },
    },
    
    # Groovy
    ".groovy": {
        "command": "groovy",
        "install": {
            "linux": "sudo apt install groovy",
            "macos": "brew install groovy",
            "windows": "choco install groovy",
        },
    },
    
    # Clojure
    ".clj": {
        "command": "clojure",
        "install": {
            "linux": "sudo apt install clojure",
            "macos": "brew install clojure",
            "windows": "choco install clojure",
        },
    },
    
    # Julia
    ".jl": {
        "command": "julia",
        "install": {
            "linux": "sudo apt install julia",
            "macos": "brew install julia",
            "windows": "choco install julia",
        },
    },
    
    # F#
    ".fs": {
        "command": "dotnet fsi",
        "install": {
            "linux": "sudo apt install dotnet-sdk-6.0",
            "macos": "brew install dotnet-sdk",
            "windows": "choco install dotnet-sdk",
        },
    },
    
    # Erlang
    ".erl": {
        "command": "erl",
        "install": {
            "linux": "sudo apt install erlang",
            "macos": "brew install erlang",
            "windows": "choco install erlang",
        },
    },
    
    # OCaml
    ".ml": {
        "command": "ocaml",
        "install": {
            "linux": "sudo apt install ocaml",
            "macos": "brew install ocaml",
            "windows": "choco install ocaml",
        },
    },
    
    # Nim
    ".nim": {
        "command": "nim",
        "install": {
            "linux": "sudo apt install nim",
            "macos": "brew install nim",
            "windows": "choco install nim",
        },
    },
    
    # Crystal
    ".cr": {
        "command": "crystal",
        "install": {
            "linux": "sudo apt install crystal",
            "macos": "brew install crystal-lang",
            "windows": "choco install crystal",
        },
    },
    
    # Zig
    ".zig": {
        "command": "zig",
        "install": {
            "linux": "sudo apt install zig",
            "macos": "brew install zig",
            "windows": "choco install zig",
        },
    },
    
    # V
    ".v": {
        "command": "v",
        "install": {
            "linux": "git clone https://github.com/vlang/v && cd v && make",
            "macos": "git clone https://github.com/vlang/v && cd v && make",
            "windows": "choco install vlang",
        },
    },
    
    # Prolog
    ".pl": {
        "command": "swipl",
        "install": {
            "linux": "sudo apt install swi-prolog",
            "macos": "brew install swi-prolog",
            "windows": "choco install swi-prolog",
        },
    },
    
    # Scheme
    ".scm": {
        "command": "scheme",
        "install": {
            "linux": "sudo apt install mit-scheme",
            "macos": "brew install mit-scheme",
            "windows": "choco install mit-scheme",
        },
    },
    
    # Racket
    ".rkt": {
        "command": "racket",
        "install": {
            "linux": "sudo apt install racket",
            "macos": "brew install racket",
            "windows": "choco install racket",
        },
    },
    
    # Smalltalk
    ".st": {
        "command": "gst",
        "install": {
            "linux": "sudo apt install gnu-smalltalk",
            "macos": "brew install gnu-smalltalk",
            "windows": "choco install gnu-smalltalk",
        },
    },
    
    # Forth
    ".fs": {
        "command": "gforth",
        "install": {
            "linux": "sudo apt install gforth",
            "macos": "brew install gforth",
            "windows": "choco install gforth",
        },
    },
    
    # COBOL
    ".cbl": {
        "command": "cobc",
        "install": {
            "linux": "sudo apt install open-cobol",
            "macos": "brew install gnu-cobol",
            "windows": "choco install open-cobol",
        },
    },
    
    # Fortran
    ".f90": {
        "command": "gfortran",
        "install": {
            "linux": "sudo apt install gfortran",
            "macos": "brew install gcc",
            "windows": "choco install gfortran",
        },
    },
    
    # Ada
    ".adb": {
        "command": "gnat",
        "install": {
            "linux": "sudo apt install gnat",
            "macos": "brew install gnat",
            "windows": "choco install gnat",
        },
    },
    
    # Pascal
    ".pas": {
        "command": "fpc",
        "install": {
            "linux": "sudo apt install fpc",
            "macos": "brew install fpc",
            "windows": "choco install fpc",
        },
    },
    
    # Lisp
    ".lisp": {
        "command": "sbcl",
        "install": {
            "linux": "sudo apt install sbcl",
            "macos": "brew install sbcl",
            "windows": "choco install sbcl",
        },
    },
    
    # Tcl
    ".tcl": {
        "command": "tclsh",
        "install": {
            "linux": "sudo apt install tcl",
            "macos": "brew install tcl-tk",
            "windows": "choco install tcl",
        },
    },
    
    # D
    ".d": {
        "command": "dmd",
        "install": {
            "linux": "sudo apt install dmd",
            "macos": "brew install dmd",
            "windows": "choco install dmd",
        },
    },
    
    # Vala
    ".vala": {
        "command": "vala",
        "install": {
            "linux": "sudo apt install valac",
            "macos": "brew install vala",
            "windows": "choco install vala",
        },
    },
    
    # Zig
    ".zig": {
        "command": "zig",
        "install": {
            "linux": "sudo apt install zig",
            "macos": "brew install zig",
            "windows": "choco install zig",
        },
    },

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
CURRENT_VERSION = "0.3.7"

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
        # Check if update was successful, if not try again
        if check_for_updates():
            print("Update verification failed. Trying again...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "slandroid"], check=True)
            if not check_for_updates():
                print("Update completed successfully on second attempt.")
            else:
                print("Update failed on second attempt, try install manually.")
                
    except subprocess.CalledProcessError as e:
        print(f"Failed to update Slandroid: {e}")

def detect_language(script_path):
    """Detect the language based on the file extension."""
    ext = Path(script_path).suffix
    return LANGUAGE_MAPPING.get(ext)

def get_platform():
    import platform
    system = platform.system().lower()
    if system == "linux":
        return "linux"
    elif system == "darwin":
        return "macos"
    elif system == "windows":
        return "windows"
    else:
        raise Exception("Unsupported platform")
    
def install_interpreter(language_info):
    """Install the required interpreter or runtime."""
    if language_info["install"]:
        platform_name = get_platform()
        install_command = language_info["install"].get(platform_name)
        if install_command:
            print(f"Installing {language_info['command']}...")
            try:
                subprocess.run(install_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {language_info['command']}: {e}")
                return False
        else:
            print(f"No installation command found for {platform_name}.")
            return False
    return True

def run_script(script_path, env_vars=None, timeout=None, output_file=None, keep_compiled=False):
    """Run the script using the appropriate interpreter."""
    language_info = detect_language(script_path)
    if not language_info:
        print(f"Unsupported file type: {Path(script_path).suffix}")
        return

    # For SlandroidScript (.sa), compile into Python first
    compiled_file = None
    if Path(script_path).suffix == ".sa":
        try:
            from .slandroid_compiler import compile_sa_file
            compiled_file = compile_sa_file(script_path)
            script_path = compiled_file  # Use the compiled file for execution
        except Exception as e:
            print(f"Error compiling SlandroidScript: {e}")
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
            process = subprocess.run(command, env=env, stdout=sys.stdout, stderr=subprocess.PIPE, timeout=timeout)
        
        if process.returncode != 0:
            stderr_output = process.stderr.decode() if process.stderr else "Unknown error"
            print(f"Error running script: {stderr_output}")
    except subprocess.TimeoutExpired:
        print(f"Script timed out after {timeout} seconds.")
    except Exception as e:
        print(f"Error running script: {e}")
    finally:
        # Clean up the compiled file (if it exists and --keep is not set)
        if compiled_file and os.path.exists(compiled_file) and not keep_compiled:
            os.remove(compiled_file)
            #print(f"Cleaned up compiled file: {compiled_file}")

def check_dependencies(script_path):
    """
    Check if all required dependencies for the script are installed.
    """
    language_info = detect_language(script_path)
    if not language_info:
        print(f"Unsupported file type: {Path(script_path).suffix}")
        return False

    # Check if the interpreter is installed
    if not shutil.which(language_info["command"].split()[0]):
        print(f"{language_info['command']} is not installed.")
        return False

    # For Go scripts, check module dependencies
    if language_info["command"] == "go run":
        try:
            result = subprocess.run(['go', 'list', '-deps'], cwd=str(Path(script_path).parent), capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Missing Go dependencies: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error checking Go dependencies: {e}")
            return False

    # For Node.js scripts, check package.json
    if language_info["command"] == "node":
        package_json = Path(script_path).parent / "package.json"
        if package_json.exists():
            try:
                subprocess.run(['npm', 'list'], cwd=str(Path(script_path).parent), check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print("Missing Node.js dependencies. Run 'npm install' first.")
                return False

    # For Ruby scripts, check for missing gems
    if language_info["command"] == "ruby":
        try:
            subprocess.run(['gem', 'list'], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("Error checking Ruby gems.")
            return False

    # For Java scripts, check for Maven/Gradle dependencies
    if language_info["command"] == "java":
        pom_file = Path(script_path).parent / "pom.xml"
        gradle_file = Path(script_path).parent / "build.gradle"
        if pom_file.exists():
            try:
                subprocess.run(['mvn', 'dependency:resolve'], cwd=str(Path(script_path).parent), check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print("Missing Maven dependencies. Run 'mvn install' first.")
                return False
        elif gradle_file.exists():
            try:
                subprocess.run(['gradle', 'dependencies'], cwd=str(Path(script_path).parent), check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print("Missing Gradle dependencies. Run 'gradle build' first.")
                return False

    # For Rust scripts, check Cargo dependencies
    if language_info["command"] == "rustc":
        cargo_file = Path(script_path).parent / "Cargo.toml"
        if cargo_file.exists():
            try:
                subprocess.run(['cargo', 'check'], cwd=str(Path(script_path).parent), check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print("Missing Rust dependencies. Run 'cargo build' first.")
                return False
            
    # For Python scripts, check for missing packages
    if language_info["command"] == "python":
        try:
            with open(script_path, "r") as file:
                lines = file.readlines()
                imports = [line.split()[1] for line in lines if line.startswith("import ") or line.startswith("from ")]
            
            missing_packages = []
            for package in imports:
                try:
                    __import__(package)
                except ImportError:
                    missing_packages.append(package)
            
            if missing_packages:
                print(f"Missing Python packages: {', '.join(missing_packages)}")
                return False
        except Exception as e:
            print(f"Error checking Python dependencies: {e}")
            return False

    print("All dependencies are installed.")
    return True

def dry_run_script(script_path):
    """
    Simulate running the script without actually executing it.
    """
    language_info = detect_language(script_path)
    if not language_info:
        print(f"Unsupported file type: {Path(script_path).suffix}")
        return

    # Display the command that would be executed
    command = language_info["command"].split() + [script_path]
    print(f"Dry run: Command to be executed: {' '.join(command)}")

    # For Python scripts, display missing packages (if any)
    if language_info["command"] == "python":
        try:
            with open(script_path, "r") as file:
                lines = file.readlines()
                imports = [line.split()[1] for line in lines if line.startswith("import ") or line.startswith("from ")]
            
            missing_packages = []
            for package in imports:
                try:
                    __import__(package)
                except ImportError:
                    missing_packages.append(package)
            
            if missing_packages:
                print(f"Missing Python packages: {', '.join(missing_packages)}")
        except Exception as e:
            print(f"Error checking Python dependencies: {e}")

def list_languages():
    """List all supported languages."""
    print("Supported Languages:")
    for ext, info in LANGUAGE_MAPPING.items():
        print(f"- {ext}: {info['command']}")

def show_help():
    """Display the help message."""
    print(f"""
SlAndroid v{CURRENT_VERSION} - A universal script runner for multiple programming languages.

SlAndroid automatically detects the language of a script, installs the required
interpreter or runtime if missing, and runs the script seamlessly. It supports
Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, and more.

    Usage: slandroid [OPTIONS] <script_path>
          
Options:
  --install       Install dependencies without running the script.
  --verbose       Display detailed output for debugging.
  --list-languages  List all supported languages.
  --compile       Compile the script before running (for compiled languages).
  --env KEY=VALUE Set environment variables for the script.
  --timeout SEC   Set a timeout for script execution.
  --output FILE   Redirect script output to a file.
  --keep          Keep the compiled file after running a SlandroidScript (.sa).
  --update        Update Slandroid to the latest version.
  --version       Display the version of slandroid.
  --yt            Open the SL Android YouTube channel.
  --check         Check if all dependencies are installed for the script.
  --dry-run       Simulate running the script without executing it.
  --help          Display this help message.
          
For more information, visit: https://github.com/IshanOshada/sl-android
""")

def open_youtube_channel():
    import webbrowser
    """Open the SL Android YouTube channel in the default web browser."""
    youtube_url = "https://www.youtube.com/@SLAndroid"
    print(f"Opening {youtube_url} in your browser...")
    webbrowser.open(youtube_url)


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
    
    if "--check" in sys.argv:
        if len(sys.argv) < 3:
            print("Usage: slandroid --check <script_path>")
            return
        script_path = sys.argv[2]
        check_dependencies(script_path)
        return

    if "--dry-run" in sys.argv:
        if len(sys.argv) < 3:
            print("Usage: slandroid --dry-run <script_path>")
            return
        script_path = sys.argv[2]
        dry_run_script(script_path)
        return

    
    if "--yt" in sys.argv:
        open_youtube_channel()
        return
    
    keep_compiled = "--keep" in sys.argv

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

    run_script(script_path, env_vars, timeout, output_file, keep_compiled=keep_compiled)

if __name__ == "__main__":
    main()