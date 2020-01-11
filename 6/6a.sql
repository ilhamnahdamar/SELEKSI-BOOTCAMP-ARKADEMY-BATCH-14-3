-- MEMBUAT DATABASE --
CREATE DATABASE dbarkademy;

-- MEMBUAT TABEL DAN MENGISI DATA PADA TABEL --
CREATE TABLE tb_category (
    id VARCHAR (20) NOT NULL,
    name VARCHAR (50) NOT NULL,
    PRIMARY KEY (id) );
CREATE TABLE tb_cashier (
    id VARCHAR (20) NOT NULL,
    name VARCHAR (50) NOT NULL,
    PRIMARY KEY (id) );
/* id: 1 ,2 3
name: 'Pevita Pearce', 'Raisa Andriana', 'Ilham Ramadhan'*NAMA*
CREATE TABLE tb_product(
    id VARCHAR (20) NOT NULL,
    name VARCHAR (50) NOT NULL,
    price VARCHAR(100) NOT NULL,
    id_category VARCHAR(20) NOT NULL,
    id_cashier VARCHAR(20) NOT NULL,
    PRIMARY KEY (id),
    foreign key: id_category, id_cashier );
/* id: 1, 2, 3

-- MENGISI DATA PADA TABEL --
INSERT INTO tb_product VALUES
(1, 2),
('Latte', 'Cake', 'Comro'),
(10000, 20000, 45000);
INSERT INTO tb_cashier VALUES
(1, 2, 3),
('Pevita Pearce', 'Raisa Andriana', 'Ilham Ramadhan');
INSERT INTO tb_category VALUES
(1, 2),
('Food', 'Drink');

-- MENAMPILKAN DATA PADA TABEL --
SELECT cashier, product, category, price FROM tb_product;
