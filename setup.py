import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wgs2json",
    version="0.0.1",
    author="Volodymyr Sokolovskyi",
    author_email="vladimir.s@gowombat.team",
    description="A simple way to get json output of `wg show` command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Go-Wombat-Team/wgs2json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
