#!/usr/bin/env python2

from setuptools import setup, find_packages
setup(
	name="FBInk",
	version="1.9.2",
	packages=find_packages(),
	scripts=['hello.py'],

	# We kinda need cffi ;).
	setup_requires=["cffi>=1.0.0"],
	cffi_modules=["fbink_build.py:ffibuilder"],
	install_requires=["cffi>=1.0.0"],

	# Metadata
	author="NiLuJe",
	author_email="ninuje@gmail.com",
	description="cFFI bindings for FBInk",
	license="AGPLv3+",
	keywords="fbink ffi cffi",
	url="https://github.com/NiLuJe/py-fbink/",
)
