# Documento de Requisitos — Projeto Catálogo de Filmes

## 1. Introdução

### 1.1 Objetivo do Projeto

Desenvolver um sistema web para permitir que o usuário gerencie sua coleção pessoal de filmes de forma organizada, visual e segura.

### 1.2 Contextualização

O sistema será uma alternativa a planilhas utilizadas para registrar filmes assistidos. A aplicação permitirá armazenar informações dos filmes e suas respectivas capas, funcionando como uma estante virtual.

### 1.3 Escopo do Sistema

O sistema deverá permitir:

-   Realizar login e logout.
-   Cadastrar filmes.
-   Visualizar filmes cadastrados.
-   Editar informações dos filmes.
-   Excluir filmes.
-   Adicionar uma imagem de capa para cada filme.

----------

## 2. Descrição Geral do Sistema

### 2.1 Visão Geral

O sistema será uma aplicação web de acesso restrito. Após realizar o login, o usuário poderá acessar sua coleção de filmes e realizar operações de gerenciamento.

----------

## 3. Requisitos Funcionais

### RF01 — Autenticação

O sistema deverá permitir que o usuário realize login utilizando usuário e senha.

### RF02 — Logout

O sistema deverá permitir que o usuário encerre sua sessão.

### RF03 — Cadastro de Filme

O sistema deverá permitir o cadastro de um filme contendo:

-   Título;
-   Ano de lançamento;
-   Gênero;
-   Nota de 0 a 10;
-   Imagem da capa.

### RF04 — Visualização do Catálogo

O sistema deverá apresentar os filmes cadastrados em formato de catálogo ou galeria, exibindo suas respectivas capas e informações principais.

### RF05 — Edição de Filme

O sistema deverá permitir que o usuário altere as informações de um filme já cadastrado.

### RF06 — Exclusão de Filme

O sistema deverá permitir que o usuário exclua um filme do catálogo.

### RF07 — Upload de Capa

O sistema deverá permitir o envio de uma imagem para ser utilizada como capa do filme.

----------

## 4. Requisitos Não Funcionais

### RNF01 — Segurança

O sistema deverá proteger o acesso ao catálogo por meio de autenticação.

### RNF02 — Usabilidade

A interface deverá ser simples, intuitiva e fácil de utilizar.

### RNF03 — Responsividade

O sistema deverá funcionar adequadamente em diferentes tamanhos de tela.

### RNF04 — Desempenho

As páginas e operações principais deverão apresentar tempo de resposta adequado para uma boa experiência de uso.

### RNF05 — Manutenibilidade

O código deverá ser organizado de forma que futuras funcionalidades possam ser adicionadas com facilidade.

----------

## 5. Regras de Negócio

### RN01 — Nota do Filme

A nota atribuída a um filme deverá estar entre **0 e 10**.

### RN02 — Dados Obrigatórios

Todo filme cadastrado deverá possuir, no mínimo, título, ano de lançamento, gênero e nota.

### RN03 — Acesso Restrito

Somente usuários autenticados poderão visualizar e gerenciar o catálogo.

### RN04 — Exclusão

A exclusão de um filme deverá remover o registro do catálogo.

----------

## 10. Considerações Finais

O **Projeto Catálogo de Filmes** tem como objetivo criar uma solução simples e visual para gerenciamento de uma coleção pessoal de filmes. A primeira versão será focada nas funcionalidades essenciais de autenticação e operações de cadastro, visualização, edição e exclusão dos filmes.
