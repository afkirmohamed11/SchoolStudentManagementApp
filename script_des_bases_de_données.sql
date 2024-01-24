

#-- Création de la Base_de_données " projet " -----------
drop database if exists projet;
create database projet;

#-- Création de la table ETUDIANT------------
use projet;
create table ETUDIANT(
id integer primary key auto_increment,
mot_de_passe varchar(50),
nom varchar(50),
prenom varchar(50),
filière varchar(50),
email varchar(50),
téléphone varchar(50),
cne varchar(50),
cin varchar(50),
date_de_naissance date,
image longblob

);
-- Création de la table adresse------------------
use projet;
create table ADRESS (
 id_Etud int,
 num int, 
 rue varchar(30),
 ville varchar(30),
 constraint fk_addr foreign key (id_Etud) references Etudiant(id)
);

#----------------------- Création de la table emploidutemps----------------
use projet;
create table emploidutemps(
link varchar(300),
filier varchar(50)
);


   #--insertion des données dans la table emploidutemps---------------------
insert into emploidutemps values('https://drive.google.com/file/d/1Nz6Mu8ZliD2G_Hn4mM5zV0aJuBbOOar5/view?usp=sharing','ID1');
insert into emploidutemps values('https://drive.google.com/file/d/1_Le_y2BODEpDWBmvG7RMLjjju4tHiaLX/view?usp=sharing','ID2');
insert into emploidutemps values('https://drive.google.com/file/d/1vH6M0Hvmf2nYQzCpvWFC8MfZet1D-j3R/view?usp=sharing','GI1');
insert into emploidutemps values('https://drive.google.com/file/d/1dNIVbYuUU36nLypcZW15TNUiJ362SgeC/view?usp=sharing','GI2');
-- Création de la table MODULES-------------------

use projet;
create table MODULES (
filière varchar(50) references Etudiant (filière),
module varchar(150),
link varchar(500),
professeur varchar(50)
);

        #--- insertion des valeurs---------------
#-----------------ID1--------------------
insert into Modules values('ID1','Analyse numérique matricielle et Statistique Inférentielle','https://drive.google.com/file/d/12t0fPVAbIEe6IImQ3D1XlX-6FtUtb5Mv/view?usp=share_link','F.EL MOURADI');
insert into Modules values('ID1','Architecture des ordinateurs et systèmes d’exploitation','https://drive.google.com/file/d/1dyoJqRC2ZpRd29T3ygkMzylH26BdARHo/view?usp=share_link','M.EL CHERRADI/S.EL HAMDDOUI');
insert into Modules values('ID1','Statistique en grande dimension',null,'M.ADDAM');
insert into Modules values('ID1','Programmation Python / Les bases du Web','https://drive.google.com/file/d/1IdvixzGbxEj-0kg8erNDbvGRTTQWHWs0/view?usp=share_link','A.BENGAG');
insert into Modules values('ID1','Programmation Orientée Objet Java',null,'T.BOUDAA');
insert into Modules values('ID1','Entreprenariat I','https://drive.google.com/file/d/1dyoJqRC2ZpRd29T3ygkMzylH26BdARHo/view?usp=share_link','S.KOULALI');
insert into Modules values('ID1','Administration et Optimisation des Bases de Données','https://drive.google.com/file/d/1RaiUVkSEWXF1_jLkEzSj6AcQry5tsbic/view?usp=share_link','Y.EL MOURABIT');
insert into Modules values('ID1','Data Mining','https://drive.google.com/file/d/1KBnfDVc4SGaKANnZMvfssVah2nVi6p9u/view?usp=share_link','A.BOUFFASIL');
insert into Modules values('ID1','Théorie des langages et compilation','https://drive.google.com/file/d/1T4Da0KGx5B5tfUwPZ0TszI1YYVQQpTME/view?usp=share_link','A.KHAMJAN');
insert into Modules values('ID1','Systèmes d’Information et Bases de Données','https://drive.google.com/file/d/1_D4l9b6GsjIPTG6NBPfoisyACm6YD-Dg/view?usp=share_link','A.EL HADDADI');
insert into Modules values('ID1','Structure de données et Algorithmique avancée','https://drive.google.com/file/d/1l6klhLDuHY9H6QIi0LxuLeGEzV_jgczU/view?usp=share_link' ,'A.AL HADDADI');
insert into Modules values('ID1','Analyse numérique matricielle et Statistique Inférentielle','https://drive.google.com/file/d/1LYof6BYyn5PlBdryyCmOsRif65mW0Ans/view?usp=share_link','M.ADDAM');
insert into Modules values('ID1','Communication Professionnelle et Soft Skills -I-','https://drive.google.com/file/d/16ON7T1QPF4TJNtcKFN9UmmUk60scITJZ/view?usp=share_link','A.BOUAZZA');

#---------------ID2---------------
insert into Modules values('ID2','Intelligence Artificielle II – Deep Learning',null,'M.EL MAROUANI');
insert into Modules values('ID2','Entreprenariat II','https://drive.google.com/file/d/1JN9jVbh6U5W2pECBVqFQGXn3v52UEIss/view?usp=share_link','S.KOULALI');
insert into Modules values('ID2','Data Warehouse et Data Lake',null,'A.EL HADDADI');
insert into Modules values('ID2','Big Data Avancées',null,'A.EL HADDADI');
insert into Modules values('ID2','Applications Web avancées avec Java et Spring','https://drive.google.com/file/d/1n8DGRfwlaFVVBSf38m6ewVsoCn5AklT8/view?usp=share_link','T.BOUDAA');
insert into Modules values('ID2','NLP',null,'T.BOUDAA');
insert into Modules values('ID2','Modélisation Stochastique / Techniques Mathématiques d’Optimisation',null,'M.ADDAM');
insert into Modules values('ID2','Intelligence Artificielle I – Machine Learning',null,'A.EL HADDADI');
insert into Modules values('ID2','Fondements du Big Data',null,'A.EL HADDADI');
insert into Modules values('ID2','Communication Professionnelle et Soft Skills -II-',null,'A.BOUAZZA');
insert into Modules values('ID2','Bases de données avancées',null,'Y. EL MOURABIT');
insert into Modules values('ID2','Architecture Logicielle et UML',null,'T.BOUDAA');

#----GI1------#
insert into Modules values('GI1','Web1 : Technologies de Web et PHP5',null,'E.W.DADI');
insert into Modules values('GI1','Théorie des langages et compilation',null,'O.ZEALOUK');
insert into Modules values('GI1','Programmation Orientée Objet C++',null,'R.RAGRAGUI');
insert into Modules values('GI1','Entreprenariat 1 & Atelier Start up',null,'S.KOULALI');
insert into Modules values('GI1','Architecture Logicielle et UML',null,'F.RAFII ZAKANI');
insert into Modules values('GI1','Algorithmique Avancée et complexité','https://drive.google.com/file/d/1w4BKdqS5aBBj-tgGPHeI5SQhMvxMfe2m/view?usp=share_link','E.W.DADI');
insert into Modules values('GI1','Systèmes d’Information et Bases de Données Relationnelles',null,'Y.EL MOURABIT');
insert into Modules values('GI1','Réseaux informatiques',null,'F.RAFII ZAKANI');
insert into Modules values('GI1','Langues et Communication Professionnelles 1',null,'A.BOUAZZA');
insert into Modules values('GI1','Recherche opérationnelle et théorie des graphes',null,'E.W.DADI');
insert into Modules values('GI1','Langage C avancé et structures de données',null,'A.RAGRAGUI');
insert into Modules values('GI1','Comptabilité générale ',null,'E.W.DADI');


#---------------GI2-------------------
insert into Modules values('GI2','Machine Learning',null,'A.BOUFASSIL');
insert into Modules values('GI2','Gestion de projet et Génie logiciel',null,'A.RAGRAGUI');
insert into Modules values('GI2','Frameworks Java EE avancés et .Net',null,'T.BOUDAA/S.OUALD CHAIB');
insert into Modules values('GI2','Web 2 : Applications Web modernes',null,'F.RAFII ZAKANI');
insert into Modules values('GI2','Entreprenariat 2','https://drive.google.com/file/d/1JN9jVbh6U5W2pECBVqFQGXn3v52UEIss/view?usp=share_link','ALI BENAISSA');
insert into Modules values('GI2','Crypto-systèmes et sécurité Informatique',null,'N.KANNOUF');
insert into Modules values('GI2','Python pour les sciences de données',null,'E.W.DADI');
insert into Modules values('GI2','Programmation Java Avancée',null,'T.BOUDAA');
insert into Modules values('GI2','Linux et programmation système',null,'M.CHERADDI');
insert into Modules values('GI2','Langues et Communication Professionnelle 2 & Soft Skils',null,'A.BOUAZZA');
insert into Modules values('GI2','sécurité informatique',null,'A.BENGAG');
insert into Modules values('GI2','Administration des Bases de données Avancées',null,'A.AKHLAL');

#-- Création de la table MODULES-------------------

use projet;
create table deliberation (
filière varchar(50) references Etudiant (filière),
link varchar(500)
);


        #--- insertion des valeurs---------------

insert into deliberation values('ID1','https://drive.google.com/file/d/1-HvPbzPQaRRwSDNQ9tVbMxUv4b_04nyA/view?usp=share_link');
insert into deliberation values('ID2','https://drive.google.com/file/d/1FWXRnfAh7SFkBgotOEAiG6nmC7S_gNlI/view?usp=share_link');
insert into deliberation values('GI1','https://drive.google.com/file/d/15-isLBx2JGl40H1PWkXoVWwrZpjeAcXz/view?usp=share_link');
insert into deliberation values('GI2','https://drive.google.com/file/d/159DB-ZBEQpxzEKpFTFhQW-kDsB0pj7cc/view?usp=share_link');

create table BentouhamiAfkirAkkouh(
        test varchar(10)
);