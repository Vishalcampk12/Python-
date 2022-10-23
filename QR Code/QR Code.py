import pyqrcode
import png
from pyqrcode import QRCode
wp = "www.codepen.io/Vishal-P/full/KKqYxeZ"
url = pyqrcode.create(wp)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)
