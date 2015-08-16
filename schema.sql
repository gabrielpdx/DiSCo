drop table if exists entries;
create table if not exists questions (
  primarySubject text not null,
  secondarySubject text not null,
  family text not null,
  difficulty integer,
  question text not null,
  correctIndex integer,
  response1 text not null,
  response2 text not null,
  response3 text not null,
  response4 text not null
);
