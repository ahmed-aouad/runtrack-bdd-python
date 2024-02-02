 CREATE TABLE etage (
    ->   id INT AUTO_INCREMENT PRIMARY KEY ,
    ->   nom VARCHAR(255) ,
    ->   numero int ,
    ->   superficie int
    ->   );


 CREATE TABLE salle (
    ->   id INT AUTO_INCREMENT PRIMARY KEY ,
    ->   nom VARCHAR(255) ,
    -> id_etage int ,
    -> capacite int
    ->   );
