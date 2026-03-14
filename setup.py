from os import path
from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="hf-libero-pro",
    packages=[p for p in find_packages() if p.startswith("libero")],
    eager_resources=["*"],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "lifelong.main=libero.lifelong.main:main",
            "lifelong.eval=libero.lifelong.evaluate:main",
            "libero.config_copy=scripts.config_copy:main",
            "libero.create_template=scripts.create_template:main",
        ]
    },
)