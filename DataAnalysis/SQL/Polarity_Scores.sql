-- Average compound value in Python subcommunity from the avg value
select avg(compundavg)
from posts
where community = 1;

-- Average compound value in Python subcommunity from the avg value
select avg(compundavg)
from posts
where community = 0;
-- Average compound value in Python subcommunity from the all value
select avg(compoundall)
from posts
where community = 1;
-- Average compound value in Python subcommunity from the all value
select avg(compoundall)
from posts
where community = 0;

--what are the 10 most negative answers in the the communities for avg compound
select *
from posts
where community = 1
order by compundavg asc
fetch first 10 rows only;
--what are the 10 most negative answers in the communities for all compound
select *
from posts
where community = 0
order by compoundall asc
fetch first 10 rows only;
--What are the 10 most positive answers in the communities for all compound
select *
from posts
where community = 0
order by compoundall desc
fetch first 10 rows only;
--What are the 10 most positive answers in the communities for average compound
select *
from posts
where community = 1
order by compundavg desc
fetch first 10 rows only;




-- how many negative answers are there according to vader compound thresh holds
--select * from posts where compoundall >= 0.05 and compoundall < 0.3;

select count(*) from posts where compoundall >= 0.05 and community = 0 and lasteditdate is not null;



--average of polarity average over months in the communities from compound all
with all_months as (select distinct to_char(creationdate, 'YYYY-MM') as year_moth from posts)
select avg(compoundall), a.year_moth
from all_months a, posts
where a.year_moth = to_char(creationdate, 'YYYY-MM') and
      community = 1
group by a.year_moth
order by a.year_moth asc;
--average of polarity average over months in the communities from compound avg
with all_months as (select distinct to_char(creationdate, 'YYYY-MM') as year_moth from posts)
select avg(compundavg), a.year_moth
from all_months a, posts
where a.year_moth = to_char(creationdate, 'YYYY-MM') and
      community = 0
group by a.year_moth
order by a.year_moth asc;

-- average comment count for answers that are very positive
select avg(commentcount) from posts where compundavg > 0.9 and community = 1;

select avg(commentcount) from posts where compoundall > 0.9 and community = 0;

-- average comment count for answers that are very negative
select avg(commentcount) from posts where compundavg < -0.9 and community = 0;

select avg(commentcount) from posts where compoundall < -0.9 and community = 1;


--variance in the different communities
select variance(compoundall) from posts where community = 0;
select variance(compoundall) from posts where community = 1;

-- standard deviation in the communities
select stddev(compoundall) from posts where community = 0;
select stddev(compoundall) from posts where community = 1;

-- number of answers with > 0.05 compound
select count(*) from posts where compoundall > 0.05 and community = 0;
select count(*) from posts where compoundall > 0.05 and community = 1;

-- prozentual
select count(*)/620355.0 from posts where compoundall > 0.05 and community = 0;
select count(*)/2038010.0 from posts where compoundall > 0.05 and community = 1;

-- correlation of compound values and comment count in the whole dataset
select corr(compoundall, commentcount) from posts;
select corr(compundavg, commentcount) from posts;

--corelation of compound and editing
with edited as (
    select count(lasteditoruserid) as counter, compoundall, compundavg from posts where lasteditoruserid != -1 or lasteditoruserid is not null group by compoundall, compundavg
)
select corr(edited.compoundall, edited.counter) from edited;

--average over all
select stddev(compundavg) from posts where community = 0;


--what are the best edit questions
select body, commentcount, score, id, community, compoundall from posts where lasteditdate is null and community = 0 order by compoundall desc;
--fetch first 10 rows only

select count(*), avg(score) as votingscore,  avg(commentcount) as commentcount from posts where compoundall < -0.95