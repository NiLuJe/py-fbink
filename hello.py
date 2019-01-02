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

"""
# Open the FB...
fbfd = fbink.fbink_open()
if fbfd == -1:
	raise SystemExit("Failed to open the framebuffer, aborting . . .")

# Initialize FBInk...
if fbink.fbink_init(fbfd, fbink_cfg) < 0:
	raise SystemExit("Failed to initialize FBInk, aborting . . .")

# Do stuff!
if fbink.fbink_print(fbfd, "Hello World", fbink_cfg) < 0:
	print("Failed to print that string!", file=sys.stderr)

# And now we can wind things down...
if fbink.fbink_close(fbfd) < 0:
	raise SystemExit("Failed to close the framebuffer, aborting . . .")
"""

# Or, the same but in a slightly more Pythonic approach ;).
fbfd = fbink.fbink_open()
try:
	fbink.fbink_init(fbfd, fbink_cfg)
	fbink.fbink_print(fbfd, "Hello World", fbink_cfg)
finally:
	fbink.fbink_close(fbfd)
