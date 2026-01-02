from pathlib import Path
from setuptools import setup

# This is where you add any fancy path resolution to the local lib:
local_path: str = (Path(__file__).parent / "playground" / "vendor" / "lightfm" ).as_uri()
print(local_path)

setup(
    install_requires=[
        f"lightfm @ {local_path}",
        "numpy==2.4.0",
        "scipy>=0.17.0", 
        "requests",
        "scikit-learn"
    ]
)
