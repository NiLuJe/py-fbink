#!/usr/bin/env python
"""
Barebones example of FBInk usage through Python's cFFI module
"""

# To get a Py3k-like print function
from __future__ import print_function

import sys
# Load the wrapper module, it's linked against FBInk, so the dynamic loader will take care of pulling in the actual FBInk library
from _fbink import ffi, lib as FBInk

# Let's check which FBInk version we're using...
print("Loaded FBInk {}".format(ffi.string(FBInk.fbink_version()).decode('ascii')))

# And now we're good to go! Let's print "Hello World" in the center of the screen...
# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True

"""
# Open the FB...
fbfd = FBInk.fbink_open()
if fbfd == -1:
	raise SystemExit("Failed to open the framebuffer, aborting . . .")

# Initialize FBInk...
if FBInk.fbink_init(fbfd, fbink_cfg) < 0:
	raise SystemExit("Failed to initialize FBInk, aborting . . .")

# Do stuff!
if FBInk.fbink_print(fbfd, "Hello World", fbink_cfg) < 0:
	print("Failed to print that string!", file=sys.stderr)

# And now we can wind things down...
if FBInk.fbink_close(fbfd) < 0:
	raise SystemExit("Failed to close the framebuffer, aborting . . .")
"""

# Or, the same but in a slightly more Pythonic approach ;).
fbfd = FBInk.fbink_open()
try:
	FBInk.fbink_init(fbfd, fbink_cfg)
	FBInk.fbink_print(fbfd, b"Hello World", fbink_cfg)
finally:
	FBInk.fbink_close(fbfd)
