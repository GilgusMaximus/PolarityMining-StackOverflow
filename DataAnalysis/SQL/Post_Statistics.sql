--minimal number of votes for c
select min(score) as worstscore, max(Score) as bestscore, min(score)*-1+max(score) as totalrangeofscores from posts;
--how many votes and comments do positive answers have on average in the c community (based on compound all)
select avg(score), avg(commentcount) from posts where community = 1;
--
select score from posts where score <= -5 order by score;

--number of edited answers
select count(*) from posts where community = 1 and  lasteditdate is not null;

--number of posts which were edited and have a positive compound value according to vader threshholds
select count(*) from posts where community = 1 and lasteditdate is not null and compoundall >= 0.05;
select count(*) from posts where community = 0 and lasteditdate is not null and compundavg >= 0.05;


select avg(compundavg) from posts where lasteditdate is not null and community = 1;

select avg(compoundall) from posts where lasteditdate is null and community = 0;


select (227921.0)/count(*)from posts where community = 0;

select avg(score), avg(commentcount) from posts where community = 0 and lasteditdate is null;

select stddev(score), stddev(commentcount), min(score), max(score), min(commentcount), max(commentcount) from posts where community = 0 and lasteditdate is null;


select avg(commentcount) from posts where community = 0;

select avg(score) from posts;

select mode () within group ( order by posts.commentcount) as modal_value from posts where community = 1;
select mode () within group ( order by  posts.commentcount) as modal_value from posts where lasteditdate is not null and community = 0;

--1378831
select count(*)from posts where commentcount != 0;

