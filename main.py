import qrcode
import argparse
import os
import datetime

parser = argparse.ArgumentParser(description="QR Code Generator")
parser.add_argument("--url", type=str, default="http://github.com/Jvele12",
                    help="URL or text to generate QR code for")
args = parser.parse_args()

QR_DIR = "qr_codes"
LOG_DIR = "logs"

os.makedirs(QR_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

filename = f"qr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
filepath = os.path.join(QR_DIR, filename)

img = qrcode.make(args.url)
img.save(filepath)

log_message = f"[{datetime.datetime.now()}] Generated QR for: {args.url} -> {filepath}\n"
with open(os.path.join(LOG_DIR, "app.log"), "a", encoding="utf-8") as log_file:
    log_file.write(log_message)

print(log_message)
print(f"✅ QR code saved to: {filepath}")
