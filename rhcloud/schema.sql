drop table if exists entries;
create table questions (
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
