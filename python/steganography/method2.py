from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

# hide text to image
path = "./input.jpg"
output_path = "./output.jpg"
text = "input text heree"
Steganography.encode(path, output_path, text)

# read secret text from image
jpg_unhide="./decode.jpg"
secret_text = Steganography.decode(jpg_unhide)



