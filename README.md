# Flask で画像のアップロードを行う

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

- 画像の単体アップロード

  ```
  $ python upload_file.py
  ```

  http://localhost:8000 にアクセス
  アップロードした画像は`./upload`に格納される
  アップロードされたら画像ページにリダイレクトされる

- 画像の複数アップロード
  ```
  $ python upload_files.py
  ```
  http://localhost:8000 にアクセス
  アップロードした画像は`./uploads`に格納される
