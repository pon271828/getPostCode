# 使い方

`docker-compose up --build`

を実行すると、コンテナが作成される その後、

`docker-compose run app python3 getPostCode.py (郵便番号)`

(郵便番号は半角)を実行すると、

`http://zipcloud.ibsnet.co.jp/api/search`

にリクエストを行い、入力した郵便番号に応じた地域名が、標準出力とresponse.txtに出力される

このアプリでは、[郵便番号検索API - zipcloud](http://zipcloud.ibsnet.co.jp/doc/api)を利用しています。
