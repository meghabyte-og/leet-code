# Write your MySQL query statement below
#visits - transactions
select v.customer_id, count(v.customer_id)-count(t.visit_id) as count_no_trans
from Visits v left join Transactions t on v.visit_id=t.visit_id group by v. customer_id having 
count(v.customer_id)-count(t.visit_id) >0