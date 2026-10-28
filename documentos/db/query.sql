-- Active: 1788283797601@@127.0.0.1@5432@catalogo_filmes
SELECT count(nome) AS qtde_de_usuarios FROM usuarios;
SELECT count(titulo) AS qtde_de_filmes FROM filmes;

SELECT * FROM filmes;

SELECT * FROM usuarios
WHERE email LIKE '%gabriel%';

SELECT * FROM filmes
WHERE nota >= 8.0;