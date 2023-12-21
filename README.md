# Rotating GIF Creator

このプログラムは、指定した画像を回転させてGIFを作成します。また、各フレームでランダムに選択した変換（色彩変化、スケール変化、透明度の変化、形状変化）を適用します。

## 使い方

1. まず、`create_rotating_gif`関数を呼び出します。この関数は、元の画像のパス、出力GIFのパス、およびGIFに含めるフレーム数を引数に取ります。

    ```python
    create_rotating_gif("data/one.jpg", "data/rotating.gif", 30)
    ```

2. この関数を呼び出すと、元の画像が少しずつ回転しながら変換され、それぞれの結果が一時的な画像として保存されます。

3. 最後に、これらの一時的な画像が組み合わせられてGIFが作成されます。

## 必要なパッケージ

このプログラムを実行するには、以下のPythonパッケージが必要です：

- OpenCV
- NumPy
- Pillow

これらのパッケージは、`requirements.txt`ファイルを使用してインストールできます：

```bash
pip install -r requirements.txt
