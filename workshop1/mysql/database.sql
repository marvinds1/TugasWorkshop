DROP DATABASE workshop1;
CREATE DATABASE IF NOT EXISTS workshop1;
USE workshop1;
CREATE TABLE IF NOT EXISTS user_accounts(
    Name varchar(32) not null,
    IdUser int not null, 
    Username varchar(16) not null,
    Email varchar(256) not null,
    Password varchar(64) not null,
    Alamat varchar(255) not null,
    NoHP varchar(16) not null,
    Birthdate DATETIME not null,
    registration_date DATETIME NOT NULL,
    PRIMARY KEY (IdUser)
);
CREATE TABLE IF NOT EXISTS product_details (
    IdProduct int not null, 
    IdUser int not null, 
    Username varchar(16) not null,
    dates DATETIME,
    photo varchar(255),
    product_name varchar (255),
    price int,
    total_buy int,
    weight int,
    description varchar(500),
    rating FLOAT(2, 1),
    PRIMARY KEY (IdProduct)
    );
 INSERT INTO user_accounts VALUES
("Rifqi Afwan", FLOOR(RAND()*(9999-1000+1))+1000, "rifqi", "rifqiafwanm@ini.com", "123123", "Mataram", "087888888888", '2001-7-04', now() );
INSERT INTO user_accounts VALUES
("Ferdi Dwi N.", FLOOR(RAND()*(9999-1000+1))+1000, "ferdi", "ferdidn@ngasal.com", "123123", "Jakarta", "087999999999", '2002-6-03', now() );
INSERT INTO user_accounts VALUES
("Nandito Fathoni", FLOOR(RAND()*(9999-1000+1))+1000, "nandito", "nanditofat@aja.com", "123123", "Mataram", "087123456789", '2001-1-12', now() );
 INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "nandito"), "nandito",now(), 
 "https://i.ibb.co/n1Kjk0n/1.jpg", "Barbel 2 Kg", 105000, 64, 4000, 
    "Speeds kembali lagi dengan produk unggulannya di bidang kesehatan. Siap menjadi alat Anda meraih kebugaran, barbel Speeds 2 Kg dilapisi dengan lapisan karet tebal yang akan mencegah barbel lepas dari genggaman Anda. Ditambah desain ergonomis sehingga nyaman digenggam, barbel Speeds 2 Kg adalah pilihan tepat bagi Anda yang ingin tampil prima. Produk tersedia sepasang.",
    4);
  INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "ferdi"), "ferdi", now(),
 "https://i.ibb.co/tJJpn26/2.jpg", "Matematika Diskrit By Rinaldi Munir Revisi Keenam",
    80000, 231, 400,
    "Buku Matematika Diskrit By Rinaldi Munir Revisi Keenam menjadi referensi bagi mahasiswa-mahasiswa yang mengenyam pendidikan di jurusan Ilmu Komputer, Sistem informasi, Teknik Informatika, Teknik Komputer atau sejenis. Buku ini juga cocok dijadikan pegangan bagi pelajar yang mengikuti Olimpiade Sains Nasional. Revisi Keenam ini ditambahi dengan bab baru tentang Graf dan penambahan materi Himpunan.",
    4.5);
 INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "rifqi"), "rifqi", now(),
  "https://i.ibb.co/q5sdqkd/3.jpg", "Purelizer Hand Sanitizer 200 ml Aloe Vera", 32000,
    250, 250,
    "Terbaru dari Purelizer sebagai pemimpin industri peralatan kesehatan, Purelizer Hand Sanitizer Aloe Vera memberikan keamanan pada keluarga Anda dengan formula terbaru yang antilengket, membersihkan 99,9% kuman, serta memberikan aroma aloe vera yang menyegarkan. Dengan  kemasan yang mudah digenggam serta dibawa ke mana saja, berikan perlindungan terbaik bagi keluarga Anda.",
    4);
 INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "ferdi"), "ferdi", now(),
  "https://i.ibb.co/9hXQM4T/4.jpg", "Stella Tempat Minum Dengan Pengukur Suhu", 50000, 50, 400,
    "Dapatkan tempat minum yang dapat menyimpan minuman Anda, baik hangat maupun dingin, secara tahan lama. Dengan seal antitumpah, Anda tidak perlu takut membawanya ke dalam aktivitas Anda yang aktif. Dilengkapi pengukur suhu, sekarang Anda dapat buktikan sendiri kualitas tempat minum penahan panas milik Stella! Cukup cas selama 30 menit, pengukur suhu tahan 24 jam!",
    5);
    
INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "rifqi"), "rifqi", now(),
 "https://i.ibb.co/qrLvJD3/5.jpg", "Medina Duo Simple Set Blue", 72000, 233, 600,
    "Produk terbaru dari Medina! Untuk si kecil yang aktif, Medina Duo Simple Set Blue dapat memberikan anak Anda perasaan menyenangkan dalam memakan bekalnya. Dibuat dengan bahan yang aman dan telah teruji, Medina Duo Simple Set tersedia dalam kotak dan tumbler yang siap menemani hari anak Anda.",
    4.4);

INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "ferdi"), "ferdi", now(),
 "https://i.ibb.co/6yvBqc0/6.jpg", "IKEA Vardera Cangkir Teh", 49900, 100, 200, 
    "Ikea Vardera memberikan Anda kesan minimalis dipadukan dengan kualitas bahan khas IKEA yang aman, kuat, dan mewah. Dapatkan IKEA Vardera Anda untuk pengalaman khas keluarga kerajaan.",
    5);

INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "nandito"), "nandito", now(),
 "https://i.ibb.co/18hZmLg/7.jpg", "Harmonica Suzuki Folk Master", 100000, 300, 150,
    "Harmonica dari penyedia alat musik berkualitas yang telah terpecaya ratusan tahun. Nada dalam C. Untuk pemula yang siap menjelajahi dunia Oskar Lee dan Blues.",
    4.5);

INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "rifqi"), "rifqi", now(),
  "https://i.ibb.co/PzsGf8z/8.jpg", "Zebra Kokoro Pulpen - Black", 14000, 1000, 100, 
    "Zebra hadir kembali dengan varian pulpen yang nyaman, ergonomis, dan berkualitas. Dengan teknologi Jepang, katakan tidak pada tinta yang tidak kunjung kering. Formula baru tinta dari departemen riset Zebra mencegah tinta Anda dari mengotori lengan dan merusak kertas kesayangan Anda.",
    4.8);
    
INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "nandito"), "nandito", now(),
 "https://i.ibb.co/HXtwLbY/9.jpg", "Oxford Learner's Pocket Dictionary", 55000, 200, 300,
    "Kamus Oxford terlengkap yang muat pada kantung jeans favorit Anda.",
    4);
    
INSERT INTO product_details VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "ferdi"), "ferdi", now(),
 "https://i.ibb.co/mSTHW7w/10.jpg", "Torch Sling Bag Kashiba – Dark Grey", 115000, 230, 200,
    "Varian baru dari Torch. Bagi Anda seorang petualang, pekerja yang aktif, maupun seorang traveller, miliki produk dari Torch dengan bahan nylon yang antiair dan kuat. Torch, dapat Anda percaya.",
    4.5);

#update
CREATE TABLE IF NOT EXISTS cart(
    IdCart int not null, 
    IdUser int not null,
    PRIMARY KEY (IdCart)
);
CREATE TABLE IF NOT EXISTS detail_cart(
    IdDetailCart int not null,
    IdCart int not null, 
    IdProduct int not null,
    amount int not null,
    PRIMARY KEY (IdDetailCart)
);
INSERT INTO cart VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "rifqi"));
INSERT INTO cart VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "ferdi"));
INSERT INTO cart VALUES
(FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE Username = "nandito"));
ALTER TABLE product_details
ADD latitude FLOAT;
ADD longitude FLOAT;
