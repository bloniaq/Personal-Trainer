import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bloniaq-personal_trainer",
    version="0.0.1",
    description="Manage your body parameters",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bloniaq/Personal-Trainer",
    author="Jakub Błoński",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["trainer"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bloniaq=trainer.__main__:main",
        ]
    },
)