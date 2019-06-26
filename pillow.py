#!/usr/bin/env python2
"""
Another example on how to print image data via Pillow.

This example basically swaps FBInk's decoding for Pillow's,
but the intent is simply to show how it can be used,
ideally for image data *created* via Pillow ;).

(Because if your aim was actually simply to print an image file,
simply doing FBInk.fbink_print_image(fbfd, sys.argv[1], 0, 0, fbink_cfg) would be faster ;p).
"""

# To get a Py3k-like print function
from __future__ import print_function

import sys
# Load the wrapper module, it's linked against FBInk, so the dynamic loader will take care of pulling in the actual FBInk library
from _fbink import ffi, lib as FBInk

# Let's check which FBInk version we're using...
print("Loaded FBInk {}".format(ffi.string(FBInk.fbink_version())))

# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True
fbink_cfg.is_verbose = True
fbink_cfg.is_flashing = True

# Abort if we weren't passed a filepath...
if len(sys.argv) < 2:
	raise SystemExit("Expected a path to an image file as the first argument!")

# NOTE: No error checking is done here!
fbfd = FBInk.fbink_open()
try:
	FBInk.fbink_init(fbfd, fbink_cfg)

	# Load the image specified on the command line...
	from PIL import Image
	im = Image.open(sys.argv[1])
	print("Image mode: {}".format(im.mode))
	print("Image size: {}x{}".format(im.width, im.height))

	# Now, make sure we'll pass raw data in a format FBInk/stb knows how to handle, doing as few conversions as possible.
	# If image is paletted, translate that to actual values, because stb won't know how to deal with paletted raw data...
	if im.mode is "P":
		print("Image is paletted, translating to actual values")
		# NOTE: No mode means "just honor the palette". Usually, that's RGB.
		#       We could also enforce Grayscale (L), but FBInk/stb will take care of that if needed.
		im = im.convert()

	# If image is not grayscale, RGB or RGBA (f.g., might be a CMYK JPEG) convert that to RGBA.
	if im.mode not in ["L", "RGB", "RGBA"]:
		print("Image data is packed in an unsupported mode, converting to RGBA")
		im = im.convert("RGBA")

	# And finally, get that image data as raw packed pixels.
	raw_data = im.tobytes("raw")
	raw_len = len(raw_data)
	print("Raw data buffer length: {}".format(raw_len))

	FBInk.fbink_print_raw_data(fbfd, raw_data, im.width, im.height, raw_len, 0, 0, fbink_cfg)
finally:
	FBInk.fbink_close(fbfd)
