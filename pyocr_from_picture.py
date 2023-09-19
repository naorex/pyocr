from PIL import Image
import pyocr
import sys
import os

# 使用可能なOCRツールを導入
tools = pyocr.get_available_tools()

# 必要なOCRツールの導入有無チェック
if len(tools) == 0:
    print("OCRツール無し。Tesseract導入後に環境変数を要設定。")
    sys.exit(1)
else:
    print(tools)


# 画像を読み込み
img_list = os.listdir("./input_picture")

# OCR実行
for img_path in img_list:
    img = Image.open(f"./input_picture/{img_path}")

    # toolsの中から、1つ目のモジュール<module 'pyocr.tesseract'>を使用
    tool = tools[0]

    # OCR解析部分
    # 読み取りモードの切り替えは、tesseract_layoutを
    # --help-extraで表示される値に合わせて切り替える事で対応（標準は3）。
    # 言語はlangの項目で変更。--list-langsで変更可能な言語を表示。
    txt = tool.image_to_string(
    img,
    lang = "script/Japanese",
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    )
    
    # 空白スペースを置き換え
    txt = txt.replace(" ", "").replace(",", "").replace("式1.00", "").replace('”1.00', "").replace("|","")
    print("\n")
    print(img_path, "\n")
    print(txt, "\n")