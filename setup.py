import setuptools
import mmcs


with open("README.md") as rm:
    long_description = rm.read()


setuptools.setup(
    name='mmcs',
    version='0.0',
    author='Maksim Buzikov',
    author_email="me.buzikov@physics.msu.ru",
    description="Toolkit for specific mathematical models of control systems",
    long_decription=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shmax3/mmcs",
    packages=setuptools.find_packages(),
    install_requires=['numba', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)