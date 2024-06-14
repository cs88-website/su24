.read data.sql
-- Homework 11

-- Comment out the unfinished questions while you
-- are working so AS to avoid errors in the tests.

-- Q2
CREATE TABLE pricing as
  SELECT name, unitPrice FROM tracks;

--Q3
CREATE TABLE long as
  SELECT name FROM tracks WHERE milliseconds > 480000;
  
--Q4
CREATE TABLE smallest as
  SELECT name, milliseconds FROM tracks ORDER BY bytes ASC LIMIT 1;

--Q5
CREATE TABLE long_album as
  SELECT title FROM albums AS a, tracks AS t WHERE a.albumId = t.albumId AND milliseconds > 480000;

--Q6
CREATE TABLE track_count as
  SELECT albumId, count(*) FROM tracks GROUP BY albumId;

--Q7
CREATE TABLE album_count as
  SELECT name, count(*) FROM artists, albums WHERE artists.artistId = albums.artistId GROUP BY name;

--Q8
CREATE TABLE busiest_artists as
  SELECT artists.name, count(*)
  FROM artists, albums, tracks
  WHERE artists.artistId = albums.artistId AND albums.albumId = tracks.albumId
  GROUP BY artists.name;
