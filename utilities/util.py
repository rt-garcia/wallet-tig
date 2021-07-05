import random
import string
import qrcode

def forgotCode():
    return ''.join(random.choices(string.digits, k=6))


def generate_qr(payment):
    dir = 'C:/wamp64/www/wallet/{}.png'.format(payment)
    qr = qrcode.QRCode(
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=5,
        border=4,
    )
    qr.add_data(payment)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(dir)
    return dir
