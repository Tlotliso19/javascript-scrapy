--dealing with the crypt_1 table
CREATE TEMP TABLE crypto_cap AS
select name, cast(yoy as float),cast(ytd as float),CAST(REPLACE(day, ',','') AS FLOAT),cast(martket_cap as bigint),
CAST(REPLACE(day, ',','') AS FLOAT) AS day,cast(weekly as float),
cast(monthly as float),cast(pecentage as float), cast(price as float),
today_date from crypto_1;  -- casting data types
 
CREATE TABLE IF NOT EXISTS crypto_cap_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    market_cap INT,
    weekly INT,
    monthly INT,
    percentage INT,
    price INT,
    today_date TEXT

);--crating tabl to hol th co crypto_1 ata



INSERT INTO  crypto_cap_coded  (name,yoy,ytd,day,market_cap,weekly,monthly,percentage, price ,today_date) --insrting into th co tabl

 WITH yesterday AS 
 ( SELECT * FROM crypto_cap
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM crypto_cap 
WHERE DATE(today_date) = CURRENT_DATE )
SELECT y.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy = y.yoy THEN 0 ELSE -1 END AS yoy_coded,
CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd = y.ytd THEN 0 ELSE -1 END AS ytd_coded,
CASE WHEN t.day>y.day THEN 1 WHEN t.day = y.day THEN 0 ELSE -1 END AS day_coded,
CASE WHEN t.martket_cap>y.martket_cap THEN 1 WHEN t.martket_cap = y.martket_cap THEN 0 ELSE -1 END AS martket_cap_coded,
CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly = y.weekly THEN 0 ELSE -1 END AS weekly_coded,
CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly = y.monthly THEN 0 ELSE -1 END AS monthly_coded,
CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage = y.pecentage THEN 0 ELSE -1 END AS pecentage_coded,
CASE WHEN t.price>y.price THEN 1 WHEN t.price = y.price THEN 0 ELSE -1 END AS price_coded,
 t.today_date

FROM  yesterday y join today t
on y.name=t.name;


-- WITH CRYPTO_2 TABL 

CREATE TEMP TABLE crypto AS SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),CAST(pecentage AS FLOAT), 
 CAST(price AS FLOAT),today_date
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
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM crypto
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            t.today_date
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
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM comodities_cast
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            t.today_date
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
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM currencies_cast
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            t.today_date
    FROM yesterday y join today t 
    ON y.name =t.name;


--dealing with stocks table
CREATE TEMP TABLE stocks_cast AS
SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),CAST(pecentage AS FLOAT), 
 CAST(price AS FLOAT),today_date
 
  FROM stocks;



CREATE TABLE IF NOT EXISTS stocks_coded (
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

INSERT INTO stocks_coded (name,yoy,ytd,day,weekly,monthly,percentage,price,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM stocks_cast
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM stocks_cast
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
            CASE WHEN t.pecentage>y.pecentage THEN 1 WHEN t.pecentage=y.pecentage THEN 0 ELSE -1 END AS pecentage,
            CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            t.today_date
    FROM yesterday y join today t 
    ON y.name =t.name;


--dealing with bonds table
CREATE TEMP TABLE bonds_cast AS
SELECT name,CAST(yoy AS FLOAT),CAST(ytd AS FLOAT),
 CAST(REPLACE(day, ',','') AS FLOAT) AS day,
 CAST(weekly AS FLOAT),CAST(monthly AS FLOAT),
 CAST(yeild AS FLOAT),today_date
 
  FROM bonds;



CREATE TABLE IF NOT EXISTS bonds_coded (
    name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    weekly INT,
    monthly INT,
   
    yeild INT,
    today_date TEXT

);

INSERT INTO bonds_coded (name,yoy,ytd,day,weekly,monthly,yeild,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM bonds_cast
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM bonds_cast
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
           
            CASE WHEN t.yeild>y.yeild THEN 1 WHEN t.yeild=y.yeild THEN 0 ELSE -1 END AS yeild,
            t.today_date
    FROM yesterday y join today t 
    ON y.name =t.name;


--dealing with commoditiesPrices table 
CREATE TEMP TABLE commoditiesPrices AS 
  SELECT name, CAST (REPLACE(yoy , '%' , ' ') AS float) AS yoy, 
   CAST (REPLACE(ytd, '%' , ' ') AS float) AS ytd,  
    CAST (REPLACE(day , '%' , ' ') AS float) AS day,
    CAST (REPLACE(weekly, '%' , ' ') AS float)  AS weekly,
    CAST (REPLACE(monthly , '%' , ' ') AS float) AS monthly,
   CAST (REPLACE(percentage , '%' , ' ') AS float) AS percentage,
  CAST(price AS float) AS price,
  DATE(today_date) AS today_date from commoditiesprices;
 
CREATE TABLE IF NOT EXISTS commodities_Prices_coded (
      name TEXT,
    yoy INT,
    ytd INT,
    day INT,
    weekly INT,
    monthly INT,
    percentage INT,
    today_date TEXT
);

INSERT INTO commodities_Prices_coded (name,yoy,ytd,day,weekly,monthly,percentage,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM commoditiesPrices
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM commoditiesPrices
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.name,CASE WHEN t.yoy>y.yoy THEN 1 WHEN t.yoy=y.yoy THEN 0 ELSE -1 END AS yoy,
            CASE WHEN t.ytd>y.ytd THEN 1 WHEN t.ytd=y.ytd THEN 0 ELSE -1 END AS ytd,
            CASE WHEN t.day>y.day THEN 1 WHEN t.day=y.day THEN 0 ELSE -1 END AS day,
            CASE WHEN t.weekly>y.weekly THEN 1 WHEN t.weekly=y.weekly THEN 0 ELSE -1 END AS weekly,
            CASE WHEN t.monthly>y.monthly THEN 1 WHEN t.monthly=y.monthly THEN 0 ELSE -1 END AS monthly,
           
            CASE WHEN t.percentage>y.percentage THEN 1 WHEN t.percentage=y.percentage THEN 0 ELSE -1 END AS percentage,
            t.today_date
    FROM yesterday y join today t 
    ON y.name =t.name;

-- dealing with yahoo_futures table

CREATE TEMP TABLE yahoo_futures_cast AS    SELECT symbol,name,market_time,
    CAST(REPLACE(volume, ',', '') AS INT) AS volume,
      CAST(REPLACE(change, ',', '') AS float) AS change,
    CAST(REPLACE(change_pecent, '%', '') AS float) AS change_pecent,
    CAST(REPLACE(open_interest,',','') AS float) AS open_interest,
    CAST(REPLACE(price,',','') AS float) AS price,
    DATE(today_date) AS today_date
    FROM yahoofutures LIMIT 10;
CREATE TABLE IF NOT EXISTS yahoo_futures_coded(
  symbol TEXT,
      name TEXT,
  market_time TEXT,
    change INT,
    change_pecent INT,
    open_interest INT,
    price INT,
    today_date TEXT
);

INSERT INTO yahoo_futures_coded (symbol,name,market_time,change,change_pecent,open_interest,price,today_date)--insting th co ata

 WITH yesterday AS 
 ( SELECT * FROM yahoo_futures_cast
WHERE DATE(today_date) = CURRENT_DATE - INTERVAL '1 day'),
today AS 
( SELECT * FROM yahoo_futures_cast
WHERE DATE(today_date) = CURRENT_DATE )
SELECT t.symbol,t.name,t.market_time,
          CASE WHEN t.change>y.change THEN 1 WHEN t.change=y.change THEN 0 ELSE -1 END AS change,
          CASE WHEN t.change_pecent>y.change_pecent THEN 1 WHEN t.change_pecent=y.change_pecent THEN 0 ELSE -1 END AS change_pecent,
          CASE WHEN t.open_interest>y.open_interest THEN 1 WHEN t.open_interest=y.open_interest THEN 0 ELSE -1 END AS open_interest,
          CASE WHEN t.price>y.price THEN 1 WHEN t.price=y.price THEN 0 ELSE -1 END AS price,
            t.today_date
    FROM yesterday y join today t 
    ON y.name =t.name;