from setuptools import setup, find_packages

setup(
    name="sha3-py",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    description="An implementation of the SHA-3 hashing algorithm in Python",
    author="Aravindh",
    license="MIT",
)
