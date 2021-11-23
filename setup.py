from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tkcolorpicker",
    version="2.1.3",
    description="Color picker dialog for Tkinter",
    long_description=long_description,
    url="https://github.com/j4321/tkColorPicker",
    author="Juliette Monsel",
    author_email="j_4321@protonmail.com",
    license="GPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Widget Sets",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "Natural Language :: English",
        "Natural Language :: French",
        "Operating System :: OS Independent",
    ],
    keywords=["tkinter", "color", "colorchooser"],
    py_modules=["tkcolorpicker"],
    packages=["tkcolorpicker"],
    install_requires=["Pillow"],
)
# test
