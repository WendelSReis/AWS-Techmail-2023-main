-- TRANSACTIONS

SELECT *
FROM pub1.titles
WHERE pubdate < DATE_SUB(NOW(), INTERVAL 33 MONTH);

--
START TRANSACTION;
SET SQL_SAFE_UPDATES = 0;
-- INSERINDO
INSERT INTO pub1.obsolete_titles
  SELECT * FROM pub1.titles
  WHERE pubdate < DATE_SUB(NOW(), INTERVAL 33 MONTH);
-- DELETANDO
DELETE FROM pub1.titles 
  WHERE pubdate < DATE_SUB(NOW(), INTERVAL 33 MONTH);
-- INCREMENTANDO
SET SQL_SAFE_UPDATES = 1;
-- MANDANDO AS ALTERACOES
COMMIT;