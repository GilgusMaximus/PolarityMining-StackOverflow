--number of user accounts created by year
select count(YEAR(CreationDate)), YEAR(CreationDate) from users group by YEAR(CreationDate)