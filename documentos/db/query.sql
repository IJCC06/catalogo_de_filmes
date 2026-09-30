SELECT count(nome) AS qtde_de_usuarios FROM usuarios;
SELECT count(titulo) AS qtde_de_filmes FROM filmes;

SELECT * FROM filmes
WHERE ano_lancamento
BETWEEN '2000-01-01' AND '2021-01-01';

SELECT * FROM usuarios
WHERE email LIKE '%gabriel%';

SELECT * FROM filmes
WHERE nota >= 8.0;