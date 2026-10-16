#!/usr/bin/env python3
"""Build a photo-app-friendly QR card using a stable Pages URL, not a versioned APK URL."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import qrcode

URL = "https://sui-0825.github.io/smart-scroll-apk/"
outdir = Path("site")
outdir.mkdir(exist_ok=True)
W, H = 1200, 1600
NAVY, GOLD = "#173769", "#F3C36C"
img = Image.new("RGB", (W, H), "#FBFCFF")
d = ImageDraw.Draw(img)
font_dir = Path("/usr/share/fonts/opentype/noto")
regular = font_dir / "NotoSansCJK-Regular.ttc"
bold = font_dir / "NotoSansCJK-Bold.ttc"
if not (regular.exists() and bold.exists()):
    raise RuntimeError("Install fonts-noto-cjk before building QR poster.")
def f(size, heavy=True):
    return ImageFont.truetype(str(bold if heavy else regular), size)
def center(text, y, size, color=NAVY, heavy=True):
    d.text((W // 2, y), text, font=f(size, heavy), fill=color, anchor="ma")

for x,y,rx,ry,c in [
 (80,245,160,160,"#E5F4FF"),(1090,186,170,115,"#E5F4FF"),
 (75,1080,143,122,"#E7F7FF"),(1130,1140,173,165,"#F3F2FF"),
 (100,1460,125,130,"#EAF6FF"),(1050,1470,146,105,"#E8F6FF")]:
    d.ellipse((x-rx,y-ry,x+rx,y+ry), fill=c)
d.rounded_rectangle((24,24,1176,1576), radius=84, fill="white", outline=NAVY, width=15)
for x,y,s in [(153,161,35),(1060,161,35),(143,1038,32),(1050,1016,32),(185,1465,26),(1034,1453,26)]:
    pts=[(x,y-s),(x+s*.25,y-s*.25),(x+s,y),(x+s*.25,y+s*.25),(x,y+s),(x-s*.25,y+s*.25),(x-s,y),(x-s*.25,y-s*.25)]
    d.polygon(pts,fill=GOLD)
    d.line(pts+[pts[0]],fill=NAVY,width=4,joint="curve")
center("Smart Scroll",116,95)
d.rounded_rectangle((105,278,1095,402), radius=55, fill=NAVY)
center("共通インストール QRコード",303,57,"white")
d.rounded_rectangle((243,424,957,520),radius=48,fill="#E4F3FF")
center("Android用  •  いつでも最新版",442,42)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=1, border=4)
qr.add_data(URL)
qr.make(fit=True)
matrix=qr.get_matrix()
m=len(matrix)
step=14
qsize=m*step
qx=(W-qsize)//2
qy=571
b=33
d.rounded_rectangle((qx-b,qy-b,qx+qsize+b,qy+qsize+b),radius=30,fill="white",outline="#ADD9F7",width=11)
for y,row in enumerate(matrix):
    for x,cell in enumerate(row):
        if cell:
            d.rectangle((qx+x*step,qy+y*step,qx+(x+1)*step-1,qy+(y+1)*step-1),fill="#101E37")
fy=qy+qsize+60
d.rounded_rectangle((115,fy,1085,fy+92),radius=42,fill="#FFF0F2")
center("読み取る → 最新APKをダウンロード",fy+14,42)
d.rounded_rectangle((315,fy+120,885,fy+205),radius=42,fill="#D8F5E8")
center("ずっと使える共通QR",fy+135,39,"#146A4C")
center("※ ダウンロード後にAndroidのインストール確認があります",fy+238,27,"#61718A",False)
png=outdir/"SmartScroll-QR-card.png"
jpg=outdir/"SmartScroll-QR-card.jpg"
img.save(png,optimize=True)
img.save(jpg,"JPEG",quality=94,subsampling=0,optimize=True)
print("QR URL:",URL, "modules:",m, "PNG:", png.stat().st_size,"JPG:",jpg.stat().st_size)
