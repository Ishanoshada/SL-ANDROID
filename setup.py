# setup.py
from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="slandroid",
    version="0.3.5",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "slandroid = slandroid.tool:main",  # This creates the `slandroid` command
        ],
    },
    description="A universal script runner for multiple programming languages. Automatically detects and runs scripts in Python, JavaScript, Bash, Ruby, Java, Go, PHP, Perl, C, C++, Rust, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify the format of the long description
    author="Ishan Oshada (SL ANDROID TEAM)",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    url="https://github.com/ishanoshada/slandroid",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    keywords=[
        "script runner",
        "multi-language",
        "python",
        "javascript",
        "bash",
        "ruby",
        "java",
        "go",
        "php",
        "perl",
        "c",
        "c++",
        "rust",
        "automation",
        "developer tools",
    ],
    install_requires=["requests","packaging"],  # Add dependencies if needed
    project_urls={
        "Source": "https://github.com/ishanoshada/slandroid",
        "Bug Reports": "https://github.com/ishanoshada/slandroid/issues",
        "Documentation": "https://github.com/ishanoshada/slandroid#readme",
    },
)