-- 👉 sqlite3 25-SQL.db
-- SQLite version 3.37.0 2021-12-09 01:34:53
-- Enter ".help" for usage hints.
--
SELECT * FROM cones WHERE Price > 5;
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25
SELECT * FROM cones WHERE Flavor LIKE '%berry%';
-- 1|strawberry|pink|3.55
-- 4|strawberry|pink|5.25
SELECT * FROM cones WHERE Flavor LIKE 'berry';
SELECT * FROM cones WHERE Flavor LIKE 'c%';
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
.headers ON
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.55
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25
-- 5|bubblegum|pink|4.75
SELECT * FROM cones WHERE Flavor LIKE '%b%';
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.55
-- 4|strawberry|pink|5.25
-- 5|bubblegum|pink|4.75
SELECT 'hello' LIKE '%ello';
-- 'hello' LIKE '%ello'
-- 1
SELECT 'cello' LIKE '%ello';
-- 'cello' LIKE '%ello'
-- 1
SELECT 'xxxxello' LIKE '%ello';
-- 'xxxxello' LIKE '%ello'
-- 1
SELECT 'xxxxello1234' LIKE '%ello';
-- 'xxxxello1234' LIKE '%ello'
-- 0
SELECT 'xxxxello1234' LIKE '%ello%';
-- 'xxxxello1234' LIKE '%ello%'
-- 1
SELECT * FROM cones WHERE Flavor LIKE '%berry' AND Price > 5;
-- Id|Flavor|Color|Price
-- 4|strawberry|pink|5.25
SELECT * FROM cones WHERE Flavor LIKE '%berry' OR Price > 5;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.55
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25

CREATE TABLE fancy_cones AS
   SELECT * FROM cones WHERE price > 4.5;

.tables
-- cones        fancy_cones  sales
SELECT * FROM fancy_cones;
-- Id|Flavor|Color|Price
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25
-- 5|bubblegum|pink|4.75
INSERT INTO cones(ID, Flavor, Color, Price) VALUES (8, 'Mint Chocolate', 'green', 3.95);
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.55
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25
-- 5|bubblegum|pink|4.75
-- 7|Vanilla|white|3.95



UPDATE cones SET Price = 10 * Price;
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|35.5
-- 2|chocolate|light brown|47.5
-- 3|chocolate|dark brown|52.5
-- 4|strawberry|pink|52.5
-- 5|bubblegum|pink|47.5
-- 7|Vanilla|white|39.5
UPDATE cones SET Price = Price / 10;
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.55
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.25
-- 5|bubblegum|pink|4.75
-- 7|Vanilla|white|3.95
UPDATE cones SET Price = Price + 0.25 WHERE Flavor IS 'strawberry';
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.8
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.5
-- 5|bubblegum|pink|4.75
-- 7|Vanilla|white|3.95
UPDATE cones SET Price = Price + 0.25 WHERE Id = 7;
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.8
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.5
-- 5|bubblegum|pink|4.75
-- 7|Vanilla|white|4.2

SELECT COUNT(*) FROM cones;
-- COUNT(*)
-- 6
SELECT * FROM cones;
-- Id|Flavor|Color|Price
-- 1|strawberry|pink|3.8
-- 2|chocolate|light brown|4.75
-- 3|chocolate|dark brown|5.25
-- 4|strawberry|pink|5.5
-- 5|bubblegum|pink|4.75
-- 7|Vanilla|white|4.2
SELECT COUNT(*) FROM cones;
-- COUNT(*)
-- 6
SELECT AVG(Price), MIN(Price), Max(Price) FROM cones;
-- AVG(Price)|MIN(Price)|Max(Price)
-- 4.70833333333333|3.8|5.5
SELECT AVG(Price), MIN(Price), Max(Price) FROM cones WHERE Flavor NOT LIKE '%berry';
-- AVG(Price)|MIN(Price)|Max(Price)
-- 4.7375|4.2|5.25
SELECT COUNT(*) as count FROM cones GROUP BY Flavor;
-- count
-- 1
-- 1
-- 2
-- 2
SELECT COUNT(*) as count, Flavor  FROM cones GROUP BY Flavor;
-- count|Flavor
-- 1|Vanilla
-- 1|bubblegum
-- 2|chocolate
-- 2|strawberry
SELECT COUNT(*) as count, Cashier FROM sales GROUP BY Cashier;
-- count|Cashier
-- 3|Baskin
-- 3|Robin
SELECT * FROM cones, sales;
-- Id|Flavor|Color|Price|Cashier|id|cone_id
-- 1|strawberry|pink|3.8|Baskin|1|2
-- 1|strawberry|pink|3.8|Baskin|3|1
-- 1|strawberry|pink|3.8|Baskin|4|2
-- 1|strawberry|pink|3.8|Robin|2|3
-- 1|strawberry|pink|3.8|Robin|5|2
-- 1|strawberry|pink|3.8|Robin|6|1
-- 2|chocolate|light brown|4.75|Baskin|1|2
-- 2|chocolate|light brown|4.75|Baskin|3|1
-- 2|chocolate|light brown|4.75|Baskin|4|2
-- 2|chocolate|light brown|4.75|Robin|2|3
-- 2|chocolate|light brown|4.75|Robin|5|2
-- 2|chocolate|light brown|4.75|Robin|6|1
-- 3|chocolate|dark brown|5.25|Baskin|1|2
-- 3|chocolate|dark brown|5.25|Baskin|3|1
-- 3|chocolate|dark brown|5.25|Baskin|4|2
-- 3|chocolate|dark brown|5.25|Robin|2|3
-- 3|chocolate|dark brown|5.25|Robin|5|2
-- 3|chocolate|dark brown|5.25|Robin|6|1
-- 4|strawberry|pink|5.5|Baskin|1|2
-- 4|strawberry|pink|5.5|Baskin|3|1
-- 4|strawberry|pink|5.5|Baskin|4|2
-- 4|strawberry|pink|5.5|Robin|2|3
-- 4|strawberry|pink|5.5|Robin|5|2
-- 4|strawberry|pink|5.5|Robin|6|1
-- 5|bubblegum|pink|4.75|Baskin|1|2
-- 5|bubblegum|pink|4.75|Baskin|3|1
-- 5|bubblegum|pink|4.75|Baskin|4|2
-- 5|bubblegum|pink|4.75|Robin|2|3
-- 5|bubblegum|pink|4.75|Robin|5|2
-- 5|bubblegum|pink|4.75|Robin|6|1
-- 7|Vanilla|white|4.2|Baskin|1|2
-- 7|Vanilla|white|4.2|Baskin|3|1
-- 7|Vanilla|white|4.2|Baskin|4|2
-- 7|Vanilla|white|4.2|Robin|2|3
-- 7|Vanilla|white|4.2|Robin|5|2
-- 7|Vanilla|white|4.2|Robin|6|1
SELECT COUNT(*) FROM cones, sales;
-- COUNT(*)
-- 36


-- SELECT Cashier, SUM(Price) as 'Total Sold' FROM sales, cones WHERE sales.cone_id = cones.id;
-- This doesn't work! We only see one result!
-- Cashier|Total Sold
-- Baskin|27.1
SELECT Cashier, SUM(Price) as 'Total Sold' FROM sales, cones WHERE sales.cone_id = cones.id GROUP BY Cashier;
-- Cashier|Total Sold
-- Baskin|13.3
-- Robin|13.8
