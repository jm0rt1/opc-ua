from setuptools import setup, find_packages

setup(
    name="opc_ua",
    version="0.1",
    description="A pluggable PyQt plugin system",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
