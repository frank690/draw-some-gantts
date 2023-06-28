# -*- coding: utf-8 -*-

import re

import setuptools

with open("CHANGELOG.md", "r") as fh:
    changelog = fh.read().splitlines()

compiler = re.compile(
    pattern=r"^\s*Version\s+\d+(\.\d+)*\s*\(\d{2}\.\d{2}\.\d{4}\)$", flags=re.IGNORECASE
)
raw_changelog_version = list(filter(compiler.match, changelog))[0]
changelog_version_with_date = re.sub(
    pattern=r"^\s*version\s+",
    repl="",
    string=raw_changelog_version,
    flags=re.IGNORECASE,
)
changelog_version = re.sub(
    pattern=r"\s*\(\d{2}\.\d{2}\.\d{4}\)\s*$",
    repl="",
    string=changelog_version_with_date,
    flags=re.IGNORECASE,
)

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("dev-requirements", "r") as fh:
    dev_requirements = fh.read().splitlines()

with open("requirements", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="draw-some-gantts",
    version=changelog_version,
    author="Frank Eschner",
    author_email="frank.eschner@gmx.de",
    description="Draws some gantt charts from given json data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frank690/draw-some-gantts",
    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "*.tests.*", "*.tests", "docs"]
    ),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows ",
    ],
    python_requires="~=3.7",
    entry_points={
        "console_scripts": [
            "draw_some_gantts=draw_some_gantts:start",
        ]
    },
)
