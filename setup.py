from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="trulens_explain",
    packages=find_namespace_packages(include=["trulens_explain", "trulens_explain.*"]),
    python_requires='>=3.8',
    install_requires=['numpy>=1.23.5']
)
