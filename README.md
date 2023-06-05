# Projeto Docker

### Descrição do projeto
<p align="justify">
Desenvolvi e implantei uma API REST utilizando FastAPI em Python, adotando uma abordagem moderna e eficiente. Para garantir a portabilidade e a facilidade de implantação, utilizei o Docker para criar uma imagem personalizada.

Criei um Dockerfile contendo as configurações necessárias para construir a imagem Docker, que engloba os recursos básicos para o projeto funcionar adequadamente. Essa imagem torna o ambiente de desenvolvimento isolado e independente do sistema operacional, facilitando a colaboração e a implantação consistente.

Para simplificar ainda mais o processo de implantação e gerenciamento dos contêineres, utilizei o Docker Compose. Com ele, defini um ambiente composto por dois contêineres interconectados. O primeiro contêiner executa um banco de dados MongoDB, enquanto o segundo contêiner roda a API FastAPI.

Esses contêineres se comunicam perfeitamente por meio da rede interna do Docker Compose, permitindo que a API interaja com o banco de dados MongoDB de forma eficiente e confiável. Além disso, para garantir a persistência dos dados, configurei um volume Docker, que preserva os dados do MongoDB mesmo em caso de reinicialização ou falhas do contêiner.

Essa abordagem de desenvolvimento e implantação, baseada em contêineres Docker, traz inúmeros benefícios, como a portabilidade do ambiente de desenvolvimento, a escalabilidade fácil e a garantia da integridade dos dados. Com essa solução, pude criar uma API robusta, de alto desempenho e pronta para ser implantada em diferentes ambientes de maneira consistente.
</p>

### Ferramenta e Linguagem
<img src="https://img.shields.io/static/v1?label=python&message=Linguagem &color=grenn&style=for-the-badge&logo=PYTHON"/>
<img src="https://img.shields.io/static/v1?label=fastapi&message=Framework &color=grenn&style=for-the-badge&logo=FASTAPI"/>
<img src="https://img.shields.io/static/v1?label=docker&message=ferramenta &color=grenn&style=for-the-badge&logo=DOCKER"/>

### Como Rodar a Aplicação :arrow_forward:

<p align="justify">Instale o Docker</p>

```
https://docs.docker.com/engine/install/ubuntu/
```
<p align="justify">Rodando aplicação</p>

```
docker-compose build
docker-compose up -d
A Api está em http://localhost:8000/docs
```
