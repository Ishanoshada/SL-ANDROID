# SlAndroid

![PyPI](https://img.shields.io/pypi/v/slandroid)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slandroid)
![GitHub issues](https://img.shields.io/github/issues/ishanoshada/sl-android)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ishanoshada/sl-android)
![GitHub contributors](https://img.shields.io/github/contributors/ishanoshada/sl-android)
![GitHub last commit](https://img.shields.io/github/last-commit/ishanoshada/sl-android)
![GitHub forks](https://img.shields.io/github/forks/ishanoshada/sl-android)
![GitHub Repo stars](https://img.shields.io/github/stars/ishanoshada/sl-android)
![GitHub watchers](https://img.shields.io/github/watchers/ishanoshada/sl-android)
![GitHub Sponsors](https://img.shields.io/github/sponsors/ishanoshada)
![GitHub top language](https://img.shields.io/github/languages/top/ishanoshada/sl-android)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ishanoshada/sl-android)


**Slandroid** is a universal script runner designed to simplify the execution of scripts written in multiple programming languages. It automatically detects the language of a script, installs the required interpreter or runtime if missing, and runs the script seamlessly. Whether you're working with Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, or other languages, Slandroid has you covered.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Supported Languages](#supported-languages)
5. [Examples](#examples)
6. [SlandroidScript(.sa)](#slandroidscript-a-custom-language)
6. [Contributing](#contributing)
7. [License](#license)
8. [Support](#support)

---

## Features

- **Multi-Language Support**: Run scripts in Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, and more.
- **Automatic Dependency Installation**: Installs missing interpreters or runtimes automatically.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Easy to Use**: Just run `slandroid <script_path>` and let Slandroid handle the rest.
- **Extensible**: Add support for new languages by updating the configuration.
- **Advanced Options**: Supports environment variables, timeouts, output redirection, and more.

---

## Installation

You can install Slandroid via `pip`:

```bash
pip install slandroid
```

---

## Usage

### Running a Script

To run a script, simply use the `slandroid` command followed by the path to the script:

```bash
slandroid path/to/script.py
```

Slandroid will automatically detect the script's language, install any required dependencies, and execute the script.


### Advanced Options

- **Set Environment Variables**:
  ```bash
  slandroid --env MY_VAR=value script.py
  ```

- **Set a Timeout**:
  ```bash
  slandroid --timeout 10 script.py
  ```

- **Redirect Output to a File**:
  ```bash
  slandroid --output result.txt script.py
  ```

- **Checks if all required dependencies for the script are installed**
  ```bash
  slandroid --check script.py
  ```

- **Simulates running the script without actually executing it.**
  ```bash
  slandroid --dry-run script.py
  ```

- **List Supported Languages**:
  ```bash
  slandroid --list-languages
  ```

- **Display Help**:
  ```bash
  slandroid --help
  ```

- **Display Version**:
  ```bash
  slandroid --version
  ```

- **Update Slandroid**:
  ```bash
  slandroid --update
  ```

- **SlAndroid Youtube open**
  ```bash
  slandroid --yt
  ```

---

## Supported Languages

Slandroid supports the following programming languages:


| Language   | File Extension | Command       | Installation Command (Linux) | Installation Command (macOS) | Installation Command (Windows) |
|------------|----------------|---------------|-------------------------------|------------------------------|--------------------------------|
| Python     | `.py`          | `python`      | `sudo apt install python3`    | `brew install python`        | `choco install python`         |
| JavaScript | `.js`          | `node`        | `sudo apt install nodejs`     | `brew install node`          | `choco install nodejs`         |
| SlandroidScript | `.sa` | `python`      | None                          | None                         | None                           |
| Bash       | `.sh`          | `bash`        | None                          | None                         | None                           |
| Ruby       | `.rb`          | `ruby`        | `sudo apt install ruby`       | `brew install ruby`          | `choco install ruby`           |
| Java       | `.java`        | `java`        | `sudo apt install default-jdk`| `brew install openjdk`       | `choco install jdk8`           |
| Go         | `.go`          | `go run`      | `sudo apt install golang`     | `brew install go`            | `choco install golang`         |
| PHP        | `.php`         | `php`         | `sudo apt install php`        | `brew install php`           | `choco install php`            |
| Perl       | `.pl`          | `perl`        | `sudo apt install perl`       | `brew install perl`          | `choco install strawberryperl` |
| C          | `.c`           | `gcc`         | `sudo apt install gcc`        | `brew install gcc`           | `choco install mingw`          |
| C++        | `.cpp`         | `g++`         | `sudo apt install g++`        | `brew install gcc`           | `choco install mingw`          |
| Rust       | `.rs`          | `rustc`       | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` | Same as Linux | `choco install rust` |
| TypeScript | `.ts`          | `ts-node`     | `npm install -g ts-node`      | `npm install -g ts-node`     | `npm install -g ts-node`       |
| PowerShell | `.ps1`         | `pwsh`        | `sudo apt install powershell` | `brew install powershell`    | `choco install powershell-core`|
| Lua        | `.lua`         | `lua`         | `sudo apt install lua5.3`     | `brew install lua`           | `choco install lua`            |
| R          | `.r`           | `Rscript`     | `sudo apt install r-base`     | `brew install r`             | `choco install r.project`      |
| Swift      | `.swift`       | `swift`       | `sudo apt install swift`      | `brew install swift`         | `choco install swift`          |
| Kotlin     | `.kt`          | `kotlin`      | `sudo apt install kotlin`     | `brew install kotlin`        | `choco install kotlin`         |
| Dart       | `.dart`        | `dart`        | `sudo apt install dart`       | `brew install dart`          | `choco install dart-sdk`       |
| Haskell    | `.hs`          | `runhaskell`  | `sudo apt install haskell-platform` | `brew install ghc` | `choco install haskell-dev`    |
| Elixir     | `.exs`         | `elixir`      | `sudo apt install elixir`     | `brew install elixir`        | `choco install elixir`         |
| Scala      | `.scala`       | `scala`       | `sudo apt install scala`      | `brew install scala`         | `choco install scala`          |
| Groovy     | `.groovy`      | `groovy`      | `sudo apt install groovy`     | `brew install groovy`        | `choco install groovy`         |
| Clojure    | `.clj`         | `clojure`     | `sudo apt install clojure`    | `brew install clojure`       | `choco install clojure`        |
| Julia      | `.jl`          | `julia`       | `sudo apt install julia`      | `brew install julia`         | `choco install julia`          |
| F#         | `.fs`          | `dotnet fsi`  | `sudo apt install dotnet-sdk-6.0` | `brew install dotnet-sdk` | `choco install dotnet-sdk`     |
| Erlang     | `.erl`         | `erl`         | `sudo apt install erlang`     | `brew install erlang`        | `choco install erlang`         |
| OCaml      | `.ml`          | `ocaml`       | `sudo apt install ocaml`      | `brew install ocaml`         | `choco install ocaml`          |
| Nim        | `.nim`         | `nim`         | `sudo apt install nim`        | `brew install nim`           | `choco install nim`            |
| Crystal    | `.cr`          | `crystal`     | `sudo apt install crystal`    | `brew install crystal-lang`  | `choco install crystal`        |
| Zig        | `.zig`         | `zig`         | `sudo apt install zig`        | `brew install zig`           | `choco install zig`            |
| V          | `.v`           | `v`           | `git clone https://github.com/vlang/v && cd v && make` | Same as Linux | `choco install vlang` |
| Prolog     | `.pl`          | `swipl`       | `sudo apt install swi-prolog` | `brew install swi-prolog`    | `choco install swi-prolog`     |
| Scheme     | `.scm`         | `scheme`      | `sudo apt install mit-scheme` | `brew install mit-scheme`    | `choco install mit-scheme`     |
| Racket     | `.rkt`         | `racket`      | `sudo apt install racket`     | `brew install racket`        | `choco install racket`         |
| Smalltalk  | `.st`          | `gst`         | `sudo apt install gnu-smalltalk` | `brew install gnu-smalltalk` | `choco install gnu-smalltalk`  |
| Forth      | `.fs`          | `gforth`      | `sudo apt install gforth`     | `brew install gforth`        | `choco install gforth`         |
| COBOL      | `.cbl`         | `cobc`        | `sudo apt install open-cobol` | `brew install gnu-cobol`     | `choco install open-cobol`     |
| Fortran    | `.f90`         | `gfortran`    | `sudo apt install gfortran`   | `brew install gcc`           | `choco install gfortran`       |
| Ada        | `.adb`         | `gnat`        | `sudo apt install gnat`       | `brew install gnat`          | `choco install gnat`           |
| Pascal     | `.pas`         | `fpc`         | `sudo apt install fpc`        | `brew install fpc`           | `choco install fpc`            |
| Lisp       | `.lisp`        | `sbcl`        | `sudo apt install sbcl`       | `brew install sbcl`          | `choco install sbcl`           |
| Tcl        | `.tcl`         | `tclsh`       | `sudo apt install tcl`        | `brew install tcl-tk`        | `choco install tcl`            |
| D          | `.d`           | `dmd`         | `sudo apt install dmd`        | `brew install dmd`           | `choco install dmd`            |
| Vala       | `.vala`        | `vala`        | `sudo apt install valac`      | `brew install vala`          | `choco install vala`           |


---


## Examples

### Python Script (`script.py`)

```python
# script.py
print("Hello from Python!")
```

Run the script:
```bash
slandroid script.py
```

Output:
```
Hello from Python!
```

---

### JavaScript Script (`script.js`)

```javascript
// script.js
console.log("Hello from JavaScript!");
```

Run the script:
```bash
slandroid script.js
```

Output:
```
Hello from JavaScript!
```

---

### Bash Script (`script.sh`)

```bash
#!/bin/bash
echo("Hello from Bash!");
```

Run the script:
```bash
slandroid script.sh
```

Output:
```
Hello from Bash!
```

---

### Rust Script (`script.rs`)

```rust
// script.rs
fn main() {
    println!("Hello from Rust!");
}
```

Run the script:
```bash
slandroid script.rs
```

Output:
```
Hello from Rust!
```

---

## SlandroidScript: A Custom Language

Slandroid now supports **SlandroidScript**, a custom language with a shorter and more intuitive syntax than Python. SlandroidScript files use the `.sa` extension and are automatically compiled into Python before execution.

### SlandroidScript Syntax

| SlandroidScript | Python Equivalent |
|-----------------|-------------------|
| `penn "Hello"`  | `print("Hello")`  |
| `penn x`        | `print(x)`        |
| `for i in 1 to 5:` | `for i in range(1, 6):` |
| `func add(a, b):` | `def add(a, b):`  |
| `if x > 10:`    | `if x > 10:`      |
| `else:`         | `else:`           |
| `while x > 0:`  | `while x > 0:`    |
| `ganin math`    | `import math`     |

### Example `.sa` File

```plaintext
# SlandroidScript Example
x = 5
while x > 0:
    penn x
    x = x - 1
```

### Run the Script

```bash
slandroid script.sa
```

### Output

```
5
4
3
2
1
```

---

### Advanced Options for SlandroidScript

- **Check Dependencies**:
  ```bash
  slandroid --check script.sa
  ```

- **Dry Run (Simulate Execution)**:
  ```bash
  slandroid --dry-run script.sa
  ```

- **Keep Compiled File**:
  ```bash
  slandroid --keep script.sa


---


## Contributing

We welcome contributions to Slandroid! If you'd like to contribute, please follow these steps:

1. Fork the repository on [GitHub](https://github.com/ishanoshada/slandroid).
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

For bug reports or feature requests, please open an issue on the [GitHub Issues page](https://github.com/ishanoshada/slandroid/issues).

---

## License

Slandroid is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Support

If you have any questions or need assistance, feel free to reach out:

- **Email**: ishan.kodithuwakku.offcial@gmail.com
- **GitHub Issues**: [https://github.com/ishanoshada/slandroid/issues](https://github.com/ishanoshada/slandroid/issues)

---


Happy scripting with Slandroid! 🚀


**Repository Views** ![Views](https://profile-counter.glitch.me/slandroid-package/count.svg)
