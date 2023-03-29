import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="confluencetools", # Replace with your own username
    version="0.0.1",
    author="Daniel Hettich",
    author_email="daniel.hettich@nintendo.de",
    description=" set of convienient functions to work the Atlassian's Confluence REST-API",
    url="https://github.com/Elynvalur/confluencetools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)