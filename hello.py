#!/usr/bin/env python2
"""
Barebones example of FBInk usage through Python's cFFI module
"""

import sys
# Load the wrapper module, it's linked against fbink, so the dynamic loader will take care of pulling in the actual FBInk library
from _fbink import ffi, lib as fbink

# Let's check which FBInk version we're using...
print("Loaded FBInk {}".format(ffi.string(fbink.fbink_version())))

# And now we're good to go! Let's print "Hello World" in the center of the screen...
# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True

# Open the FB...
fbfd = fbink.fbink_open()
if fbfd == -1:
	print("Failed to open the framebuffer, aborting . . .")
	sys.exit(-1)

# Initialize FBInk...
if fbink.fbink_init(fbfd, fbink_cfg) < 0:
	print("Failed to initialize FBInk, aborting . . .")
	sys.exit(-1)

# Do stuff!
if fbink.fbink_print(fbfd, "Hello World", fbink_cfg) < 0:
	print("Failed to print that string!")

# And now we can wind things down...
if fbink.fbink_close(fbfd) < 0:
	print("Failed to close the framebuffer, aborting . . .")
	sys.exit(-1)
