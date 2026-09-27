from setuptools import setup, find_packages

setup(
    name="bloom_utils",
    version="0.1.0",
    description="Small-business pricing and inventory utilities.",
    author="Dorcas Agyenim Boateng",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7",
)
