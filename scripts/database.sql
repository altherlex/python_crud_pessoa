-- criacao de database
create database python_crud_pessoas;

-- colocando database em uso
use python_crud_pessoas;

-- criacao de tabelas
create table pessoas (

    id int not null auto_increment,
    nome varchar (100) not null,
    cpf char (11),
    primary key (id)

);

create table contatos (

    id int not null auto_increment,
    id_pessoas int not null,
    telefone char (11),
    email varchar (150),
    primary key (id),
    foreign key (id_pessoas) references pessoas (id)

);

-- inserindo dados para teste
insert into pessoas (nome, cpf) values ("Luciano Neves", "12345678900");
insert into contatos (id_pessoas, telefone, email) values (1, "11123456789", "luciano@email.com");

-- consulta de tabelas
select * from pessoas;

select * from contatos;

select
    p.nome,
    p.cpf,
    c.telefone,
    c.email
from
    pessoas as p
inner join contatos as c on c.id_pessoas = p.id;

-- alterar informacoes
set SQL_SAFE_UPDATES=0;
update python_crud_pessoas.pessoas set nome = "Parangaricutirimirruaro do Chapolin" where cpf = "66666666666";
update python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id set c.telefone= "11666666666" where cpf = "66666666666";
update python_crud_pessoas.contatos set id_pessoas = 8 where id = 5;

-- deletar informacoes
SET foreign_key_checks = 0;
delete from python_crud_pessoas.pessoas where cpf = "66666666666";
delete c from python_crud_pessoas.pessoas as p inner join python_crud_pessoas.contatos as c on c.id_pessoas = p.id where cpf = "66666666666";