# -*- coding: utf-8 -*-
"""
embed_qr_pptx.py — 将新生成的 qr-booking.png 替换到两个海报 PPTX 中的"现场预约"二维码

用法:
  python tools/embed_qr_pptx.py

原理: 找到 PPTX 中位置在 x≈4.45, y≈13.00 的图片（第3个QR码位置），
      用新的 qr-booking.png 替换它。
"""
import os
import sys
from pptx import Presentation
from pptx.util import Emu, Inches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
POSTER_DIR = os.path.join(BASE_DIR, 'posters')
QR_BOOKING = os.path.join(BASE_DIR, 'qr-codes', 'qr-booking.png')

# 第3个QR码卡片的位置（现场预约）
TARGET_X = 4.45
TARGET_Y = 13.00
TOLERANCE = 0.3  # 英寸


def replace_qr_in_pptx(pptx_path, qr_path):
    """替换 PPTX 中现场预约位置的二维码。"""
    p = Presentation(pptx_path)
    slide = p.slides[0]
    replaced = False

    for shape in slide.shapes:
        if shape.shape_type != 13:  # PICTURE
            continue
        try:
            left = Emu(shape.left).inches
            top = Emu(shape.top).inches
        except Exception:
            continue
        # 匹配现场预约QR码位置
        if abs(left - TARGET_X) < TOLERANCE and abs(top - TARGET_Y) < TOLERANCE:
            # 替换图片
            image_part = shape.image
            # 通过直接修改 blob 替换图片
            with open(qr_path, 'rb') as f:
                new_image_data = f.read()
            # 获取图片 part 并替换
            from pptx.opc.constants import RELATIONSHIP_TYPE as RT
            image_part._blob = new_image_data
            replaced = True
            print(f"  已替换: {os.path.basename(pptx_path)}")
            break

    if replaced:
        p.save(pptx_path)
    else:
        print(f"  ⚠️ 未找到目标位置图片: {os.path.basename(pptx_path)}")

    return replaced


def main():
    if not os.path.exists(QR_BOOKING):
        print(f"❌ QR 码文件不存在: {QR_BOOKING}")
        print("   请先运行: python tools/generate_qr.py https://你的URL")
        sys.exit(1)

    print(f"QR 码文件: {QR_BOOKING}")
    print(f"文件大小: {os.path.getsize(QR_BOOKING)} bytes")
    print()

    for fname in ['海报-展架60x160-海外留学.pptx', '海报-展架60x160-国内高考.pptx']:
        pptx_path = os.path.join(POSTER_DIR, fname)
        if os.path.exists(pptx_path):
            print(f"处理: {fname}")
            replace_qr_in_pptx(pptx_path, QR_BOOKING)
        else:
            print(f"⚠️ 文件不存在: {fname}")

    print()
    print("✅ 完成！PPTX 中的预约二维码已更新。")


if __name__ == '__main__':
    main()
