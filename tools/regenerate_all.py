# -*- coding: utf-8 -*-
"""
regenerate_all.py — 一键重新生成预约二维码并嵌入 PPTX

用法:
  python tools/regenerate_all.py https://你的用户名.github.io/edu-booking/

流程:
  1. 用 URL 生成新的 qr-codes/qr-booking.png
  2. 将新二维码替换到两个海报 PPTX 中
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# 导入同目录下的两个脚本
sys.path.insert(0, SCRIPT_DIR)
from generate_qr import generate_qr
from embed_qr_pptx import replace_qr_in_pptx

QR_BOOKING = os.path.join(BASE_DIR, 'qr-codes', 'qr-booking.png')
POSTER_DIR = os.path.join(BASE_DIR, 'posters')


def main():
    if len(sys.argv) < 2:
        print("用法: python tools/regenerate_all.py https://你的用户名.github.io/edu-booking/")
        print()
        print("示例:")
        print("  python tools/regenerate_all.py https://wanglaoshi.github.io/edu-booking/")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith('http://') and not url.startswith('https://'):
        print(f"❌ URL 必须以 http:// 或 https:// 开头: {url}")
        sys.exit(1)

    print("=" * 50)
    print("一键重新生成预约二维码")
    print("=" * 50)
    print(f"URL: {url}")
    print()

    # Step 1: 生成 QR 码
    print("[1/2] 生成二维码...")
    generate_qr(url, QR_BOOKING)
    print()

    # Step 2: 嵌入 PPTX
    print("[2/2] 替换 PPTX 中的二维码...")
    for fname in ['海报-展架60x160-海外留学.pptx', '海报-展架60x160-国内高考.pptx']:
        pptx_path = os.path.join(POSTER_DIR, fname)
        if os.path.exists(pptx_path):
            print(f"  处理: {fname}")
            replace_qr_in_pptx(pptx_path, QR_BOOKING)
        else:
            print(f"  ⚠️ 文件不存在: {fname}")

    print()
    print("✅ 全部完成！")
    print("  - HTML 海报自动引用 qr-codes/qr-booking.png，无需额外操作")
    print("  - PPTX 海报中的预约二维码已替换")
    print()
    print("下一步:")
    print("  1. 用手机扫描海报上的预约二维码，确认能打开表单页面")
    print("  2. 首次提交需在邮箱中点确认链接激活 Formsubmit.co")


if __name__ == '__main__':
    main()
