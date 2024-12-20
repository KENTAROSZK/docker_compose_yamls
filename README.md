# docker-compose.yaml files

## 参考

- https://qiita.com/ymasaoka/items/ca2bb2cb19ebeafe1ccc
- https://book.impress.co.jp/books/1121101138
	- ![書籍](imgs/1121101138-520x.jpg)


## Dockerfileとdocker-compose.yamlの違い

- Dockerfile：カスタムイメージを作成するためのもの
- docker-compose：1個以上のコンテナを作成するためのもの


## コンテナのネットワーク

コンテナ間のネットワークは、`docker-compose.yaml` で自動的に作られる。

コンテナの外（例えばローカルPC）からコンテナ内部へ通信する場合は、ポートフォワーディングが必要。

- ポートフォワーディング：特定のポート番号あての通信をあらかじめ設定した別のポート番号へ転送すること。


例）
```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: flask-container
    ports:
      - "8080:80" # 「http://localhost:5000/」
```

この例の場合、外部（例えばブラウザローカルPC）からの接続（8080）のポート番号が、コンテナ上の80というポート番号へ転送されるということ


### 明示的に作ることも可能
明示的に作成した方が高度な設定が可能である。
ただ、ちょっとした検証用に利用するだけであれば、あまり使う機会はない。

```yaml
services:
  apache:
    image: httpd
    networks:
      - netweb01
    ports:
      - "8080:80"
networks:
  netweb01
```




## Tips


### コンテナを起動させたままにしたい場合

コンテナは実行されるプロセスが無いと、起動後にすぐ終了してしまう。
終了すると、コンテナの中に入ることもできない。

起動したままにするためには、以下のように`tty` という設定項目を `true` にしておけばよい。


例）

```yaml
services:
  debian:
  	image: debian:11.3
  	tty: true
```



### コンテナのログをローカルPCから確認する方法

```shell
docker compose logs コンテナ名
```

### コンテナイメージを再ビルドする場合

```shell
docker compose up --build -d
```

!!注意!!
変更が反映されない時は以下のコマンド。
イメージのビルドにはキャッシュが使われるため、明示的にキャッシュを利用しないようにするために以下のコマンドがある。

```shell
docker compose build --no-cache
```


### ローカルPCからコンテナの中に対してコマンドを実行したい時

```shell
docker compose コンテナ名 コマンド
```

例）

```shell
docker compose python-container pip list
```

