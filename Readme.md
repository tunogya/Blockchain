# **米奇喵喵币**
**MiKi Minami Coin**

![coin](design/coin_with_font.png)

## REST API参考

    见[REST API参考](demo/Readme.md)

## Usage
1. Change the ports in [docker-compose.yml](docker-compose.yml).

    | application name | host-port | container-port |
    |------------------|-----------|----------------|
    | app              | 8000      | 8000           |
    | db               | 3306      | 3306           |
    | nginx            | 80/443    | 8000           |
        
2. Run the docker.
  
       $ docker-compose up
 
3. Stop the docker.

       $ docker-compose down

## 设计稿
    设计稿使用Sketch，文件:[MMC.sketch](design/MMC.sketch)。