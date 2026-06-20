# Write your MySQL query statement below
select b.id 
from Weather a join Weather b on b.recordDate = DATE_ADD(a.recordDate, INTERVAL 1 DAY) 
where a.temperature < b.temperature

