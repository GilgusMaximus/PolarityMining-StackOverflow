--display the number of answers for each year in the C community
select date_part('year', creationdate) as year, count(date_part('year', creationdate)) as number_of_answers
from posts
where community = 0
group by date_part('year', creationdate);
--display the number of answers for each month in the C community in the cleaned version of the files (so some more answers were removed)
select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers
from posts
where community = 0 and creationdate < '2019-12-01'
group by to_char(creationdate, 'YYYY-MM');
--display the number of answers for each month in the Python community in the cleaned version of the files (so some more answers were removed)
select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers
from posts
where community = 1 and creationdate < '2019-12-01'
group by to_char(creationdate, 'YYYY-MM');


select count(*) from posts where community = 1 and creationdate between '2016-12-01' and '2017-01-01';

select * from posts where id < 1000 and lasteditdate is null
