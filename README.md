# Slandroid

![PyPI](https://img.shields.io/pypi/v/slandroid)
![License](https://img.shields.io/pypi/l/slandroid)


**Slandroid** is a universal script runner designed to simplify the execution of scripts written in multiple programming languages. It automatically detects the language of a script, installs the required interpreter or runtime if missing, and runs the script seamlessly. Whether you're working with Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, or other languages, Slandroid has you covered.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Supported Languages](#supported-languages)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **Multi-Language Support**: Run scripts in Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, and more.
- **Automatic Dependency Installation**: Installs missing interpreters or runtimes automatically.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Easy to Use**: Just run `slandroid <script_path>` and let Slandroid handle the rest.
- **Extensible**: Add support for new languages by updating the configuration.

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

### Example Commands

- Run a Python script:
  ```bash
  slandroid script.py
  ```

- Run a JavaScript script:
  ```bash
  slandroid script.js
  ```

- Run a Bash script:
  ```bash
  slandroid script.sh
  ```

---

## Supported Languages

Slandroid supports the following programming languages:

| Language   | File Extension | Command       | Installation Command       |
|------------|----------------|---------------|----------------------------|
| Python     | `.py`          | `python`      | `pip install`              |
| JavaScript | `.js`          | `node`        | `npm install -g`           |
| Bash       | `.sh`          | `bash`        | None                       |
| Ruby       | `.rb`          | `ruby`        | `gem install`              |
| Java       | `.java`        | `java`        | None                       |
| Go         | `.go`          | `go run`      | `go install`               |
| PHP        | `.php`         | `php`         | `sudo apt install php`     |
| Perl       | `.pl`          | `perl`        | `sudo apt install perl`    |
| C          | `.c`           | `gcc`         | `sudo apt install gcc`     |
| C++        | `.cpp`         | `g++`         | `sudo apt install g++`     |
| Rust       | `.rs`          | `rustc`       | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` |
| TypeScript | `.ts`          | `ts-node`     | `npm install -g ts-node`   |
| PowerShell | `.ps1`         | `pwsh`        | `sudo apt install powershell` |
| Lua        | `.lua`         | `lua`         | `sudo apt install lua5.3`  |
| R          | `.r`           | `Rscript`     | `sudo apt install r-base`  |
| Swift      | `.swift`       | `swift`       | `sudo apt install swift`   |
| Kotlin     | `.kt`          | `kotlin`      | `sudo apt install kotlin`  |
| Dart       | `.dart`        | `dart`        | `sudo apt install dart`    |
| Haskell    | `.hs`         | `runhaskell`  | `sudo apt install haskell-platform` |
| Elixir     | `.exs`        | `elixir`      | `sudo apt install elixir`  |

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
echo "Hello from Bash!"
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
