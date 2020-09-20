# Blockchain 指南

使用Django开发的区块链项目。

## REST API参考
见[Readme.md](demo/Readme.md)

## Usage
1. Change the ports in [docker-compose](docker-compose.yml) file.

    | application name | out-port | in-port |
    |------------------|----------|---------|
    | app              | 8000     | 8000    |
    | db               | 3306     | 3306    |
    | nginx            | 80/443   | 8000    |
        
2. Run the docker.
        
       $ docker-compose up
 
3. Stop the docker.

       $ docker-compose down

