import cv2
import numpy as np
import os
from PIL import Image
import random

def apply_affine_transform(image_path, rotation_angle, output_path, transformation):
    # 画像を読み込む
    img = cv2.imread(image_path)

    # 画像のサイズを取得
    rows, cols = img.shape[:2]

    # アフィン変換のための変換行列を作成
    M = cv2.getRotationMatrix2D((cols/2, rows/2), rotation_angle, 1)

    # アフィン変換を適用
    dst = cv2.warpAffine(img, M, (cols, rows))

    # ランダムに選択した変換を適用
    if transformation == 1:
        # 色彩変化
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
        dst[:,:,0] = (dst[:,:,0] + random.randint(0, 180)) % 180
        dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)
    elif transformation == 2:
        # スケール変化
        scale = 1 + random.uniform(-0.1, 0.1)
        dst = cv2.resize(dst, None, fx=scale, fy=scale)
    elif transformation == 3:
        # 透明度の変化（アルファブレンディング）
        alpha = random.uniform(0.5, 1.0)
        dst = cv2.addWeighted(dst, alpha, img, 1 - alpha, 0)
    elif transformation == 4:
        # 形状変化（シア変換）
        M = np.float32([[1, random.uniform(-0.1, 0.1), 0],
                        [random.uniform(-0.1, 0.1), 1, 0]])
        dst = cv2.warpAffine(dst, M, (cols, rows))

    # 変換した画像を保存
    cv2.imwrite(output_path, dst)

def create_rotating_gif(image_path, gif_path, num_frames):
    # 一時的な画像ファイルのパスを保存するリスト
    temp_images = []

    try:
        for i in range(num_frames * 2):  # 正回転と逆回転
            # 回転角度を計算（360度をフレーム数で分割）
            angle = i * (360 / num_frames) if i < num_frames else 360 - (i - num_frames) * (360 / num_frames)

            # 出力画像のパスを作成
            output_path = f"temp_{i}.jpg"
            temp_images.append(output_path)

            # ランダムに変換を選択
            transformation = random.choice([1, 2, 3, 4])

            # アフィン変換を適用
            apply_affine_transform(image_path, angle, output_path, transformation)

        # 一時的な画像を読み込み、GIFを作成
        images = [Image.open(image_path) for image_path in temp_images]
        images[0].save(gif_path, save_all=True, append_images=images[1:], loop=0)
    finally:
        # 一時的な画像を削除
        for image_path in temp_images:
            os.remove(image_path)

# 関数を呼び出して画像にアフィン変換を適用し、GIFを作成
create_rotating_gif("data/one.jpg", "data/rotating.gif", 30)
