from pathlib import Path
from setuptools import setup

# This is where you add any fancy path resolution to the local lib:
local_path: str = (Path(__file__).parent / "playground" / "vendor" / "lightfm" ).as_uri()
print(local_path)

setup(
    install_requires=[
        f"lightfm @ {local_path}",
        "numpy==2.4.0",
        "scipy==1.16.3", 
        "requests==2.32.5",
        "scikit-learn==1.8.0",
        "pandas==2.3.3",
        "unidecode==1.4.0"
    ]
)
