--How do the top answerer in Python perform over time in the sentiment analysis
with AnswerNumbers (NumberOfAnswers) as (
    select count(owneruserid) as NumberOfAnswers, owneruserid
    from posts
    where owneruserid != -1
      and community = 1
    group by owneruserid
    order by NumberOfAnswers desc)

--select only the top 5 through the number of answers
select *
from posts,
     AnswerNumbers
where posts.owneruserid = AnswerNumbers.owneruserid
  and AnswerNumbers.NumberOfAnswers >= 6140
  and community = 1
order by posts.owneruserid asc, posts.creationdate asc;


with AnswerNumbers (NumberOfAnswers) as (
    select count(owneruserid) as NumberOfAnswers, owneruserid
    from posts
    where owneruserid != -1
      and community = 0
    group by owneruserid
    order by NumberOfAnswers desc)

--
select *
from posts,
     AnswerNumbers
where posts.owneruserid = AnswerNumbers.owneruserid
  and AnswerNumbers.NumberOfAnswers >= 3305
  and community = 0
order by posts.owneruserid asc, posts.creationdate asc;

--How many users answered in both category
with topanswerer (NumberofAnswers, owneruserid) as (select count(owneruserid) as NumberOfAnswers, owneruserid
                                                    from posts
                                                    where owneruserid != -1
                                                    group by owneruserid
                                                    order by NumberOfAnswers desc),

     topanswererstatistic as (select topanswerer.NumberofAnswers,
                                     (topanswerer.NumberofAnswers - count(posts.owneruserid)) as NumberOfAnswersPython,
                                     count(posts.owneruserid)                                 as NumberOfAnswersC,
                                     topanswerer.owneruserid
                              from posts
                                       RIGHT OUTER JOIN topanswerer
                                                        on posts.owneruserid != -1
                                                            and community = 0
                                                            and topanswerer.owneruserid = posts.owneruserid
                              group by topanswerer.owneruserid, NumberOfAnswers
                              order by topanswerer.NumberOfAnswers desc)

select count(topanswererstatistic.owneruserid) as BothCategoryAnswerer
from topanswererstatistic
where NumberOfAnswersPython > 0
  and NumberOfAnswersC > 0;

--How many answerers are in both categories
select count(distinct owneruserid)
from posts;


with top_user_stats as (
    select count(distinct id) as number_of_answers, owneruserid
    from posts
    where community = 0
      and owneruserid != -1
    group by owneruserid
    order by number_of_answers desc
    fetch first 5 rows only
)
select sum(cast(score as float)) / count(distinct id) as avg_score, sum(cast(commentcount as float))/count(id) as avg_comment_count, top_user_stats.owneruserid, to_char(creationdate, 'YYYY') as year
from posts,
     top_user_stats
where posts.owneruserid = top_user_stats.owneruserid
  and community = 0 and creationdate < '12-01-2019'
group by top_user_stats.owneruserid,
         year
order by top_user_stats.owneruserid asc, year asc;


with top_user_stats as (
    select count(distinct id) as number_of_answers, owneruserid
    from posts
    where community = 0
      and owneruserid != -1
    group by owneruserid
    order by number_of_answers desc
    fetch first 5 rows only
)

select count(*), posts.owneruserid,to_char(creationdate, 'YYYY') as year from top_user_stats, posts where top_user_stats.owneruserid = posts.owneruserid and community = 0
group by posts.owneruserid, year;
--select sum(top_user_stats.number_of_answers) from top_user_stats
select * , to_char(creationdate, 'YYYY') as year
from posts,
     top_user_stats
where posts.owneruserid = top_user_stats.owneruserid
  and community = 1 and creationdate < '12-01-2019'
order by year asc;

with top_user_stats as (
    select count(distinct id) as number_of_answers, owneruserid
    from posts
    where community = 0
      and owneruserid != -1
    group by owneruserid
    order by number_of_answers desc
    fetch first 5 rows only
), sc as(

select sum(compoundall)/count(id) as cmd, count(id) as ids, to_char(creationdate, 'YYYY') as year from posts, top_user_stats
where community = 0 and top_user_stats.owneruserid = posts.owneruserid
group by year)
select * from sc
select corr(cmd, ids) from sc