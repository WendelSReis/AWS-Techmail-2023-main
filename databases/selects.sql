-- SELECTS

-- LAB 151
-- RETORNAR TODOS OS DADOS DAS COLUNAS ESPECIFICAS
SELECT partnum, bktitle, slprice, pubdate FROM pub1.titles;

-- RETORNAR DADOS ENTRE INTERVALOS DE DATAS
-- RETORNAR DADOS QUE NÃO CONTENHAM AS STRINGS: repair, play e build
SELECT partnum, bktitle, slprice, pubdate FROM pub1.titles
WHERE 
(pubdate BETWEEN "2012-01-01" AND "2017-12-30")
AND 
(lower(bktitle) NOT LIKE "%repair%" AND lower(bktitle) NOT LIKE "%play%" 
AND lower(bktitle) NOT LIKE "%build%");

-- SOMAR VALORES DE VENDAS
SELECT SUM(qty)FROM pub1.sales
WHERE partnum == "40125";

-- LAB 153
SELECT name FROM pub1.loyalty;

--
SELECT substring_index(name, " ", -1) AS segundoNome, name 
FROM pub1.loyalty
LIMIT 10;

--
SELECT substring_index(name, " ", -1) AS 'last_name', points, email
FROM pub1.loyalty
WHERE pub1.loyalty.email LIKE '%.gov' OR pub1.loyalty.email LIKE '%.org'
ORDER BY last_name ASC, points DESC;

--
SELECT DISTINCT(substring(bktitle, 1, 15)) AS 'titles'
FROM pub1.titles
WHERE length(trim(bktitle)) > 12
ORDER BY titles ASC;

-- LAB 155

-- RANK
SELECT * FROM pub1.sales;

--
SELECT sldate, partnum, qty, custnum 
FROM pub1.sales;

--
SELECT sldate, partnum, qty, custnum,
RANK() OVER (PARTITION BY MONTHNAME(sldate) ORDER BY qty DESC) AS 'quantity_rank'
FROM pub1.sales
ORDER BY quantity_rank;

--
SELECT * FROM pub1.titles;

--
SELECT partnum, bktitle, slprice
FROM pub1.titles;

--
SELECT partnum, bktitle, slprice
FROM pub1.titles
WHERE TRIM(bktitle) -- REMOVER ESPACOS EM BRANCO
LIKE "% % %";

-- 
SELECT partnum, bktitle, slprice
FROM pub1.titles
WHERE bktitle
LIKE "% % %"
ORDER BY slprice DESC 
LIMIT 20;

-- LAB 157
-- FIRST
SELECT
  slspers.repid AS rep,
  CONCAT(trim(lname), ", ", trim(fname)) AS fullname,
  SUM(sales.qty) AS quantity
  FROM pub1.sales -- RODAR PRA GERAR ERRO
  -- RELACIONAMENTO A ESQUERDA
  LEFT JOIN pub1.slspers ON (pub1.sales.repid = pub1.slspers.repid)
  -- RELACIONAMENTO A DIREITA
  RIGHT JOIN pub1.slspers ON (pub1.slspers.repid = pub1.sales.repid)
  GROUP BY slspers.repid
  ORDER BY quantity DESC;

-- LAB 159

DROP TABLE IF EXISTS pub1.inventory;
