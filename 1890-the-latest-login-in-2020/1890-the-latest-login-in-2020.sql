# Write your MySQL query statement below
select user_id, last_stamp from
(select user_id, time_stamp last_stamp, row_number() over(partition by user_id order by time_stamp desc) r from Logins 
where year(time_stamp) = 2020) t
where r=1