-- CRIAR A TABELA RESTART
CREATE TABLE restart (
  student_id INT NOT NULL,
  student_name VARCHAR(255),
  restart_city VARCHAR(255),
  graduation_date DATE,
  PRIMARY KEY (student_id)
);

-- INSERIR DADOS NA TABELA RESTART
-- ALTERAR OS VALORES E REPETIR ESSA AÇÃO 10 VEZES PARA INSERIR 10 DADOS DIFERENTES
-- NÃO ESQUECER DE ALTERAR O VALOR DE STUDENT_ID
INSERT INTO restart (
  student_id,
  student_name,
  restart_city,
  graduation_date
)
VALUES (
  1,
  "Danilo Caetano",
  "São Paulo",
  2011-12-18 13:17:17
),
(
  2,
  "Danilo Caetano",
  "São Paulo",
  2011-12-18 13:17:17
),
(
  3,
  "Danilo Caetano",
  "São Paulo",
  2011-12-18 13:17:17
);

-- RETORNAR TODOS OS DADOS DA TABELA RESTART
SELECT * FROM restart;

-- CRIAR A CLOUD_PRACTITIONER
CREATE TABLE cloud_practitioner (
  student_id INT NOT NULL,
  certification_date DATE,
  PRIMARY KEY (student_id)
);

-- INSERIR DADOS NA TABELA CLOUD_PRACTITIONER
-- ALTERAR OS VALORES E REPETIR ESSA AÇÃO 5 VEZES PARA INSERIR 5 DADOS DIFERENTES
-- NÃO ESQUECER DE ALTERAR O VALOR DE STUDENT_ID
INSERT INTO cloud_practitioner (
  student_id,
  student_name,
  restart_city,
  graduation_date
)
VALUES (
  1,
  2011-12-18 13:17:17
),
(
  2,
  2011-12-18 13:17:17
)
(
  3,
  2011-12-18 13:17:17
);

-- RETORNAR TODOS OS DADOS DA TABELA CLOUD_PRACTITIONER
SELECT * FROM cloud_practitioner;

-- INNER JOIN
-- RETORNAR DADOS RELACIONADOS ENTRE AS TABELAS RESTART E CLOUD_PRACTITIONER
SELECT student_id, student_name, certification_date 
FROM restart
INNER JOIN cloud_practitioner
ON restart.student_id = cloud_practitioner.student_id;


