-- ======================================================
-- 실습용 DB : DoItsql
--       TB : doit_tb
-- ======================================================
CREATE DATABASE IF NOT EXISTS doitsql;

USE doitsql;

CREATE TABLE IF NOT EXISTS doit_tb
(
    col_1 int PRIMARY KEY AUTO_INCREMENT,      
    col_2 VARCHAR(50),      
    col_3 int     
    
);

CREATE TABLE IF NOT EXISTS data_tb
(
    col_2 VARCHAR(50),      
    col_3 int,      
    col_4 char(2)     
    
);

-- DB내에 TB 확인
SHOW TABLES;


-- TB 구조 확인
DESC doit_tb;

-- 데이터 추가 
INSERT INTO data_tb VALUES 
("test", 1, "A"),("ENGLISH", 2, "B"),("MATH", 3, "C"),
("ABC", 4, "D"),("DEF", 5, "E"),("GHI", 6, "F"),
("JKL", 7, "G"),("MNO", 8, "H"),("PQR", 9, "I");

-- INSERT INTO doit_tb VALUES 
-- (1, "test", 10);


-- AUTO_INCREMENT 자동 증가
INSERT INTO doit_tb (col_2, col_3)
VALUES ("OK", 100);

INSERT INTO doit_tb (col_2, col_3)
VALUES ("OK", 100), 
       ("YES", 90),
       ("GOOD", 40);

-- AE 컬럼도 값 지정
INSERT INTO doit_tb VALUES 
(8, "test", 10);

# ======================================================
# SELECT -> INSERT 
# DATA_TB -> doit_tb로 데이터 추가
# ======================================================
INSERT INTO doit_tb(col_2, col_3)
SELECT col_2, col_3 FROM data_tb;

# ======================================================
# SELECT 결과 -> CREATE
# DATA_TB -> doit_tb로 데이터 추가
# ======================================================
CREATE Table CopyTB AS (SELECT * FROM data_tb);



# 전체 데이터 조회
select * from doit_tb;

# AE 설정값 변경
SET @@AUTO_INCREMENT_increment = 5;



# 현재 마지막 AE값 확인
SELECT LAST_INSERT_ID() '마지막 AE 번호';