--dealing with the crypt_1 table
CREATE TEMP TABLE crypto_cap AS
select name, cast(yoy as float),cast(ytd as float),cast(day as float),cast(martket_cap as bigint),
cast(monthly as float),cast(pecentage as float), cast(price as float),cast(weekly as float),
today_date from crypto_1;  -- casting data types
 
CREATE TABLE IF NOT EXISTS crypto_cap_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day_volume INT,
    market_cap INT,
    weekly INT,
    monthly INT,
    percentage INT,
    price INT,
    today_date TEXT

);--crating tabl to hol th co crypto_1 ata



INSERT INTO  crypto_cap_coded  (name,yoy,ytd,day_volume,market_cap,weekly,monthly,percentage, price ,today_date) --insrting into th co tabl

 WITH yesterday AS 
 ( SELECT * FROM crypto_cap
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM crypto_cap 
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE )
SELECT y.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy = y.yoy THEN 0 ELSE -1 END AS yoy_coded,
CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd = y.ytd THEN 0 ELSE -1 END AS ytd_coded,
CASE WHEN t.day>y.day THEN 1 WHEN t.day = y.day THEN 0 ELSE -1 END AS day_coded,
CASE WHEN t.martket_cap>y.martket_cap THEN 1 WHEN t.martket_cap = y.martket_cap THEN 0 ELSE -1 END AS martket_cap_coded,
CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly = y.weekly THEN 0 ELSE -1 END AS weekly_coded,
CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly = y.monthly THEN 0 ELSE -1 END AS monthly_coded,
CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage = y.pecentage THEN 0 ELSE -1 END AS pecentage_coded,
CASE WHEN t.price>y.price THEN 1 WHEN t.price = y.price THEN 0 ELSE -1 END AS price_coded,
 today_date

FROM  yesterday y join today t
on y.name=t.name;


-- WITH CRYPTO_2 TABL 

CREATE TEMP TABLE crypto AS SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),CAST(pecentage AS FLOAT), 
 CAST(price AS FLOAT)
  FROM crypto_2 ; --casting ata typs


CREATE TABLE IF NOT EXISTS crypto_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    weekly INT,
    monthly INT,
    percentage INT,
    price INT,
    today_date TEXT

);--crating tabl to hol co crypto_2 ata 


INSERT INTO crypto_coded (name,yoy,ytd,day,weekly,monthly,percentage,price,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM crypto
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM crypto
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            today_date
    FROM yesterday y join today t 
    ON y.name =t.name;


--dealing with comodities table
CREATE TEMP TABLE comodities_cast AS
SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),CAST(pecentage AS FLOAT), 
 CAST(price AS FLOAT),today_date
 
  FROM comodities;

CREATE TABLE IF NOT EXISTS comodities_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    weekly INT,
    monthly INT,
    percentage INT,
    price INT,
    today_date TEXT

);

INSERT INTO comodities_coded (name,yoy,ytd,day,weekly,monthly,percentage,price,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM comodities_cast
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM comodities_cast
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            today_date
    FROM yesterday y join today t 
    ON y.name =t.name;

---dealing with currencies data table 
CREATE TEMP TABLE currencies_cast AS
SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),CAST(pecentage AS FLOAT), 
 CAST(price AS FLOAT),today_date
 
  FROM currencies;

CREATE TABLE IF NOT EXISTS currencies_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    weekly INT,
    monthly INT,
    percentage INT,
    price INT,
    today_date TEXT

);

INSERT INTO currencies_coded (name,yoy,ytd,day,weekly,monthly,percentage,price,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM currencies_cast
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM currencies_cast
WHERE TO_DATE(today_date,'YYYY-MM-DD') = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            today_date
    FROM yesterday y join today t 
    ON y.name =t.name;