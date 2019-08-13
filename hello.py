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
# NOTE: ffi.string() returns a bytes on Python 3, not a str, hence the extra decode
print("Loaded FBInk {}".format(ffi.string(FBInk.fbink_version()).decode("ascii")))

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
if FBInk.fbink_print(fbfd, b"Hello World", fbink_cfg) < 0:
	print("Failed to print that string!", file=sys.stderr)

# And now we can wind things down...
if FBInk.fbink_close(fbfd) < 0:
	raise SystemExit("Failed to close the framebuffer, aborting . . .")
"""

# Or, the same but in a slightly more Pythonic approach ;).
fbfd = FBInk.fbink_open()
try:
	FBInk.fbink_init(fbfd, fbink_cfg)
	# NOTE: On Python 3, cFFI maps char to bytes, not str
	FBInk.fbink_print(fbfd, b"Hello World", fbink_cfg)

	# And a few other random examples...
	"""
	# A full-screen, flashing refresh
	fbink_cfg.is_flashing = True
	FBInk.fbink_refresh(fbfd, 0, 0, 0, 0, FBInk.HWD_PASSTHROUGH, fbink_cfg)

	fbink_cfg.is_flashing = False


	# A (fairly useless) dump & restore cycle (with nightmode enabled for a free inversion)
	dump = ffi.new("FBInkDump *")
	FBInk.fbink_region_dump(fbfd, 350, 350, 250, 250, fbink_cfg, dump)

	fbink_cfg.is_nightmode = True
	fbink_cfg.is_flashing = True
	FBInk.fbink_restore(fbfd, fbink_cfg, dump)

	FBInk.fbink_free_dump_data(dump)

	fbink_cfg.is_nightmode = False
	fbink_cfg.is_flashing = False


	# Fancy OT/TTF printing
	FBInk.fbink_add_ot_font(b"Foo_Bold.ttf", FBInk.FNT_BOLD)
	fbink_ot_cfg = ffi.new("FBInkOTConfig *")
	fbink_ot_cfg.margins.top = 500
	fbink_ot_cfg.margins.bottom = 600
	fbink_ot_cfg.margins.left = 400
	fbink_ot_cfg.margins.right = 50
	fbink_ot_cfg.size_pt = 14.0
	fbink_ot_cfg.is_formatted = True
	FBInk.fbink_print_ot(fbfd, b"**Wheeeee!**", fbink_ot_cfg, fbink_cfg, ffi.NULL)

	FBInk.fbink_free_ot_fonts()

	# Another refresh example, this time with nightmode enabled (i.e., invert the current screen)
	fbink_cfg.is_nightmode = True
	fbink_cfg.is_flashing = True
	FBInk.fbink_refresh(fbfd, 0, 0, 0, 0, FBInk.HWD_PASSTHROUGH, fbink_cfg)

	fbink_cfg.is_nightmode = False
	fbink_cfg.is_flashing = False
	# NOTE: We'd just need to disable nightmode to get back the original colors,
	#       as is_nightmode doesn't actually affect the framebuffer content,
	#       the inversion is done by the eInk controller on its own private buffer.
	"""
finally:
	FBInk.fbink_close(fbfd)
