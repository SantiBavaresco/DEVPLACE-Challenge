CREATE DATABASE Educacion

go
use Educacion
go

/* Creando tabla Carrera, Universidad y Estudiante  */

Create table Carrera(
Id char(8) primary key,
Nombre varchar(20) not null
Total_materias int not null
);

Create table Universidad(
Id char(8) primary key,
Nombre varchar(20) not null,
Provincia varchar(20) not null,
Localidad varchar(50)
);

/* Creando tabla Estudiantes con campos para llaves foraneas */

Create table Estudiante(
Id char(8) primary key,
Nombre varchar(20) not null,
Apellido varchar(20) not null,
Telefono char(15),
E-mail varchar(50)
IdCarrera char(8) not null,
IdUniversidad char(8) not null,
Materias_aprobadas int,
Promedio int,
CONSTRAINT fk_Carrera FOREIGN KEY (IdCarrera) REFERENCES Carrera (Id),
CONSTRAINT fk_Universidad FOREIGN KEY (IdUniversidad) REFERENCES Universidad (Id)
);

/* EJ 4 */
SELECT * FROM Estudiantes WHERE (Promedio > 7) AND (Materias_Aprobadas > 12)
