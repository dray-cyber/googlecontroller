import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="googlecontroller",
    version="5",
    description="control your google home",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dray-cyber/googlecontroller",
    author="dray-cyber",
    author_email="testerforpyt123@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["googlecontroller"],
    include_package_data=True,
    install_requires=["requests", "pychromecast"],
    entry_points={
        "console_scripts": [
            "googlecontroller=googlecontroller.__init__:main",
        ]
    },
)
