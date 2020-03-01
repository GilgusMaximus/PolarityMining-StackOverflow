--Die ersten 100k Posts die Antworten sind und deren Frage den Tag java hat
SELECT * FROM Posts
    where Id < 100000 AND
    PostTypeId = 2 and --fragen
    ParentId in (
        select Id from Posts
            where Tags like '%java%'
    )

-- Posts deren Tags c oder c programming enthält und der Antworten count größer 1 ist
SELECT * FROM Posts
    where tags like '%<c>%' or
    tags like '%c programming%' and 
    answercount > 0 

-- Aus den ersten 1000 Posts diejenigen die zwischen dem 1.1.2008 und dem 31.12.2008 gepostet wurden
select * from posts
    where creationdate between '2008-01-01' and '2008-12-31' and
    id < 1000
    order by creationdate asc

-- antworten  die in 2008 getätigt wurden und auf fragen mit Tag c oder C programming gemacht wurden, sortiert bei aufsteigendem datu,
select * from posts
    where creationdate between '2010-01-01' and '2011-01-01' 
    and PostTypeId = 2
    and ParentId in (
        SELECT id FROM Posts
            where tags like '%<c>%' or
            tags like '%c programming%' and 
            answercount > 0 
    )
    ORDER BY creationdate asc

-- antworten  die in 2012 (erste 6 Monate) getätigt wurden und auf fragen mit Tag c oder C programming gemacht wurden, sortiert bei aufsteigendem datu,
    select * from posts
    where creationdate between '2012-01-01' and '2012-07-01' 
    and PostTypeId = 2
    and ParentId in (
        SELECT id FROM Posts
            where tags like '%<c>%' or
            tags like '%c programming%' and 
            answercount > 0 
    )
    ORDER BY creationdate asc

    --alle Python posts in den ersten 10000 posts die mindestens eine antwort haben
    SELECT * FROM Posts
    where id < 10000 and tags like '%python%' and 
    answercount > 0 

    -- Python da es 1 Million posts wengier sind -> schnelelre verarbeitung
    select * from posts
    where creationdate between '2011-04-01' and '2011-07-01' 
    and PostTypeId = 2
    and ParentId in (
        SELECT id FROM Posts
            where tags like '%python%' and 
            answercount > 0 
    )
    ORDER BY creationdate asc

    select * from posts
    where creationdate between '2012-09-01' and '2013-01-01' 
    and PostTypeId = 2
    and ParentId in (
        SELECT id FROM Posts
            where tags like '%python%' and 
            answercount > 0 
    )
    ORDER BY creationdate asc
	
	
	
	
	-- Number of questions that were asked within the first week of registration in python monthly
	
	SELECT count(Posts.id),  CAST(
      cast(DATEPART(YYYY, Posts.CreationDate) as varchar) + '-' + 
      cast(DATEPART(MM, Posts.CreationDate) as varchar) + '-01'
    as date) as Month FROM Posts, Users
  where tags like '%python%' and posttypeid = 1 and users.creationdate > posts.creationdate-7
  group by CAST(
      cast(DATEPART(YYYY, Posts.CreationDate) as varchar) + '-' + 
      cast(DATEPART(MM, Posts.CreationDate) as varchar) + '-01'
    as date)
  order by Month