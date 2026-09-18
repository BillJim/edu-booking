# -*- coding: utf-8 -*-
"""
generate_qr.py — 从 URL 生成预约表单二维码

用法:
  python tools/generate_qr.py https://你的用户名.github.io/edu-booking/
  python tools/generate_qr.py https://你的用户名.github.io/edu-booking/ --output qr-codes/qr-booking.png

不传 URL 时使用占位 URL（仅测试用）。
"""
import sys
import os
import qrcode

# 默认输出路径（相对于脚本所在目录的上级）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_OUTPUT = os.path.join(BASE_DIR, 'qr-codes', 'qr-booking.png')
PLACEHOLDER_URL = "https://example.github.io/edu-booking/"


def generate_qr(url, output_path):
    """生成 QR 码并保存为 PNG。"""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    size = os.path.getsize(output_path)
    print(f"QR 码已生成: {output_path}")
    print(f"  URL: {url}")
    print(f"  文件大小: {size} bytes")
    return output_path


def main():
    # 解析参数
    url = PLACEHOLDER_URL
    output_path = DEFAULT_OUTPUT

    args = [a for a in sys.argv[1:] if a != '--']
    for i, arg in enumerate(args):
        if arg.startswith('http://') or arg.startswith('https://'):
            url = arg
        elif arg == '--output' and i + 1 < len(args):
            output_path = args[i + 1]
        elif not arg.startswith('--') and not arg.endswith('.py'):
            # 非选项参数，当作 URL
            if '/' in arg or '.' in arg:
                url = arg

    if url == PLACEHOLDER_URL:
        print("⚠️  未提供 URL，使用占位 URL（仅测试用）")
        print("   用法: python tools/generate_qr.py https://你的用户名.github.io/edu-booking/")
        print()

    generate_qr(url, output_path)
    print()
    print("下一步:")
    print("  1. 将生成的 qr-booking.png 替换到海报中")
    print("  2. HTML 海报自动引用 qr-codes/qr-booking.png，无需额外操作")
    print("  3. PPTX 海报需重新运行嵌入脚本（如有）或手动替换图片")


if __name__ == '__main__':
    main()
