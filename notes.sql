update read me
what is the project about
how I made it
where I got the data
modules, languages used, what I am extracting, loading, etc
use notes from code

go into postgres and look at tables
try to ask some questions (queries to engage data)


National Parks grouped by state

SELECT pl.state, pi.parkname 
From parkinfo as pi
JOIN parklocation as pl
    ON pi.parkcode = pl.parkcode
ORDER BY pl.state;

Top 40 National Parks by size (Arces)

SELECT pl.state, pi.parkname, pi.acres 
From parkinfo as pi
JOIN parklocation as pl
    ON pi.parkcode = pl.parkcode
ORDER BY pi.acres DESC
limit 40

Total acres by state

SELECT SUM(pi.acres), pl.state 
From parkinfo as pi
JOIN parklocation as pl
    ON pi.parkcode = pl.parkcode
GROUP BY pl.state