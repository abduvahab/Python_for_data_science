# [build-system]
# requires = ["hatchling"]
# build-backend = "hatchling.build"

# [tool.hatchling]
# name = "ft_package",
# version = "0.0.1",
# authors = [{name = "areheman", email = "areheman@example.com"}],
# description = "A sample test package",
# readme = "README.md",
# requires = [],
# required-by = [],
# classifiers = [],
# license = "MIT",
# installer = "pip",
# entry-points = [],
# metadata-version = "2.1",

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.build_meta]
requires = ["setuptools", "wheel"]
