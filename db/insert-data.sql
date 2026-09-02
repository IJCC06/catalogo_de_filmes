INSERT INTO "usuarios" ("nome", "email", "senha")
VALUES
('Carlos', 'carlos01@gmail.com', 'carlos1234'),
('Maria', 'maria01@gmail.com', 'maria1234'),
('Gabriel', 'gabriel01@gmail.com', 'gabriel1234'),
('João', 'joao01@gmail.com', 'joao1234'),
('Luíza', 'luiza01@gmail.com', 'luiza1234');

INSERT INTO "filmes" ("id_usuario", "titulo", "ano_lancamento", "genero", "nota")
VALUES
(1, 'Indiana Jones: Caçadores da Arca Perdida', '1981-12-25', 'Aventura', 8.4),
(2, 'Lanterna Verde', '2011-08-11', 'Ficção Científica', 5.5),
(3, 'La La Land', '2017-01-13', 'Musical/Romance', 8.0),
(4, 'Violet Evergarden - O Filme', '2020-09-18', 'Fantasia/Romance', 8.3),
(5, 'Homem-Aranha: Um Novo Dia', '2026-07-29', 'Ação/Aventura', 8.0);