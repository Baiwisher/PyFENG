from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyfeng",
    version="0.2.4",
    description="Python Financial Engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jaehyuk Choi",
    author_email="pyfe@eml.cc",
    url="https://github.com/PyFE/PyFENG",
    project_urls={
        "Documentation": "https://pyfeng.readthedocs.io/",
        "Bug Tracker": "https://github.com/PyFE/PyFENG/issues",
    },
    packages=["pyfeng"],
    test_suite="tests",
    install_requires=["numpy", "scipy"],
    package_data={'pyfeng': ['data/*.xlsx']}
)
