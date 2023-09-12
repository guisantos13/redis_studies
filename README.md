# Estudos de Banco de Dados Redis com Python

Este repositório contém exemplos e informações relacionados aos meus estudos de Redis com Python. Redis é um banco de dados em memória que é amplamente utilizado para armazenar, recuperar e gerenciar dados de maneira eficiente e rápida.

## Visão Geral

- [Estudos de Banco de Dados Redis com Python](#estudos-de-banco-de-dados-redis-com-python)
  - [Visão Geral](#visão-geral)
  - [O que é Redis?](#o-que-é-redis)
  - [Configuração](#configuração)

## O que é Redis?

O Redis é um banco de dados NoSQL em memória, conhecido por sua alta velocidade e flexibilidade. Ele é usado para várias finalidades, incluindo armazenamento em cache, filas de mensagens, análises em tempo real e muito mais. Neste repositório, estou explorando como usar o Redis em conjunto com Python.

## Configuração

Antes de começar a trabalhar com o Redis em Python, você precisará configurar o ambiente. Você pode fazer isso instalando a biblioteca Python `redis`. Use o seguinte comando para instalá-la:

```bash
pip install redis 
```
Após a instalação da lib, você deve realizar a criação de um arquivo ```.env``` contendo as variavéis que serão utilizadas para provionar o cluster do redis no arquivo ```docker-compose```.

Para realizar a criação do container utilize o comando :
```bash 
docker-compose --env-file {seu_arquivo.env}  up -d 
```


