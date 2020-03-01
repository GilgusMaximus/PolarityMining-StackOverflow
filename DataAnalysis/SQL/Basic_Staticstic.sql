-- count the number of answers per user and sort by descending amount -- Values have been checked for top 10 on stack overflow -- Edit: Python also counts everything that has python within it, as i queried %python% and not %<python>%
with topanswerer (NumberofAnswers, owneruserid) as (select count(owneruserid) as NumberOfAnswers, owneruserid
                                                    from posts
                                                    where owneruserid != -1
                                                    group by owneruserid
                                                    order by NumberOfAnswers desc)

--count the number of answers of a user in the c community (0 if none) through a right outer join to keep people with 0 answers.
-- Then subract that amount from the whole amount and receive the number of answers in python as well
select topanswerer.NumberofAnswers,
       (topanswerer.NumberofAnswers - count(posts.owneruserid)) as NumberOfAnswersPython,
       count(posts.owneruserid)                                 as NumberOfAnswersC,
       topanswerer.owneruserid
from posts RIGHT OUTER JOIN topanswerer
on posts.owneruserid != -1
  and community = 0
and topanswerer.owneruserid = posts.owneruserid
group by topanswerer.owneruserid, NumberOfAnswers
order by topanswerer.NumberOfAnswers desc
fetch first 10 rows only -- find the top 10 answerer
;
-- number of posts over all
select count(owneruserid) as NumberOfAnswers, owneruserid
from posts
where owneruserid != -1
group by owneruserid
order by NumberOfAnswers desc;

-- number of posts over Python
select count(owneruserid) as NumberOfAnswers, owneruserid
from posts
where owneruserid != -1
and community = 0
group by owneruserid
order by NumberOfAnswers desc;

--avergade number of answers
with AnswerNumbers (NumberOfAnswers) as(
select count(owneruserid) as NumberOfAnswers
from posts
where owneruserid != -1
group by owneruserid
order by NumberOfAnswers desc)

select avg(AnswerNumbers.NumberOfAnswers)
from AnswerNumbers;

--mode
with AnswerNumbers (NumberOfAnswers) as(
select count(owneruserid) as NumberOfAnswers
from posts
where owneruserid != -1
group by owneruserid
order by NumberOfAnswers desc)
select mode () within group ( order by  AnswerNumbers.NumberOfAnswers) as modal_value from AnswerNumbers;

-- number of posts in c
select count(*) from posts where community = 0;
-- number of posts in python
select count(*) from posts where community = 1;