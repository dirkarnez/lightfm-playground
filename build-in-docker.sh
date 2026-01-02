# /bin/bash
python3.14 --version

python3.14 -m pip install --upgrade pip setuptools wheel
python3.14 -m pip install build
python3.14 -m pip install Cython
# python3.14 -m pip install ./playground/vendor/lightfm
python3.14 -m pip install -e .
python3.14 -m build
python3.14 ./playground/main.py

