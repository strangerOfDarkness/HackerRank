/*
USING MS SQL
*/

select distinct city from station
where city NOT like '[aeiou]%' AND city NOT like '%[aeiou]';