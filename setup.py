#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
	name="FBInk",
	version="1.23.0",
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
	license="GPLv3+",
	keywords="fbink ffi cffi",
	url="https://github.com/NiLuJe/py-fbink/",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console :: Framebuffer",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Natural Language :: English",
		"Operating System :: POSIX :: Linux",
		"Programming Language :: C",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: Implementation :: CPython",
		"Topic :: Multimedia :: Graphics",
		"Topic :: Software Development :: Libraries",
	],
)
