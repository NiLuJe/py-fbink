#!/usr/bin/env python2
"""
Barebones example of FBInk usage through Python's cFFI module
"""

import os
# Load the wrapper module
from _fbink import ffi, lib as fbink

# And now we're good to go! Let's print "Hello World" in the center of the screen...
# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True

# Open the FB...
fbfd = fbink.fbink_open()
if fbfd == -1:
	print("Failed to open the framebuffer, aborting . . .")
	os.exit(-1)

# Initialize FBInk...
if fbink.fbink_init(fbfd, fbink_cfg) < 0:
	print("Failed to initialize FBInk, aborting . . .")
	os.exit(-1)

# Do stuff!
if fbink.fbink_print(fbfd, "Hello World", fbink_cfg) < 0:
	print("Failed to print that string!")

# And now we can wind things down...
if fbink.fbink_close(fbfd) < 0:
	print("Failed to close the framebuffer, aborting . . .")
	os.exit(-1)
