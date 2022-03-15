import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="add-issue-id-hook",
    version="1.1.0",
    author="Piotr Betkier, packaged by Thomas Hemmert-Pottmann",
    author_email="thomas.hemmert-pottmann@tum.de",
    description="pre-commit hook for adding the issue id to commit message",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">=3.8",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ]
)