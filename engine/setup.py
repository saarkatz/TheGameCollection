from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="engine",
    version="0.0.1",
    author="Saar Katz",
    author_email="kats.saar@gmail.com",
    description="A simple game engine to provide a better interface for game "
                "development in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saarkatz/TheGameCollection/tree/game_editor/engine",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: Microsoft Windows",
    ],
    python_requires='>=3',

    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
