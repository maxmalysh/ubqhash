[![Build Status](https://travis-ci.org/ethereum/ubqhash.svg?branch=master)](https://travis-ci.org/ethereum/ubqhash)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/debris/ubqhash?branch=master&svg=true)](https://ci.appveyor.com/project/debris/ubqhash-nr37r/branch/master)

# Ubqhash

For details on this project, please see the Ethereum wiki:
https://github.com/ethereum/wiki/wiki/Ubqhash

### Coding Style for C++ code:

Follow the same exact style as in [cpp-ethereum](https://github.com/ethereum/cpp-ethereum/blob/develop/CodingStandards.txt)

### Coding Style for C code:

The main thing above all is code consistency.

- Tabs for indentation. A tab is 4 spaces
- Try to stick to the [K&R](http://en.wikipedia.org/wiki/Indent_style#K.26R_style),
  especially for the C code.
- Keep the line lengths reasonable. No hard limit on 80 characters but don't go further
  than 110. Some people work with multiple buffers next to each other.
  Make them like you :)

### Python

To install: 

    pip3 install pyubqhash
    
To build:

    pyenv local 3.8.2
    pip3 install --upgrade pip wheel twine
    python3 setup.py build 
    python3 setup.py sdist bdist_wheel
    twine upload dist/*