-- für fir Ranges: [0,0] = absolut neutral = 605658,  [-0.05,0) (0,0.05] = neutral = 43131, (0.05, 0.75], = psoitive = 1087681, (0.75, 1.0] = sehr positiv = 414096,
-- [-0.75, -0.05) = negativ = 445291, [-1, 0.75) = sehr negative = 62508

with a  as (
    select * from posts where compoundall < -0.75 and compoundall >= -1 order by compoundall desc, id asc
)
select * from a offset 2 fetch first 1 rows only ;


select owneruserid, count(id) as answers from posts where community = 0 and owneruserid != -1 group by owneruserid order by answers desc fetch first 5 rows only


-- neutral: [424221, 403491, 509684, 537102, 29674, 100542, 550576, 419289, 246186, 423214, 69104, 47169, 424272, 151107, 259978, 619885, 448049, 216942, 201257, 304288]
-- pos: [668327, 594469, 543111, 1022423, 396743, 561331, 327640, 1074298, 351335, 554857, 697204, 493176, 909354, 187162, 569207, 363376, 243722, 516480, 210053, 476329]
-- very pos: [281055, 211814, 32134, 99347, 138867, 21198, 329854, 259447, 53887, 379057, 6242, 300055, 72352, 68967, 119618, 408054, 371962, 128859, 129963, 274708]
-- neg: [390249, 321691, 5373, 159420, 162810, 113111, 339522, 16381, 316296, 327224, 347702, 64402, 37595, 76357, 273678, 118934, 128403, 249186, 33154, 25124]
-- very neg: [44976, 8862, 26551, 20442, 35614, 13704, 19654, 57181, 49358, 35588, 56635, 14919, 17253, 1980, 25419, 24926, 49872, 55945, 29197, 18498]


-- selects the row at the offset
select body, compoundall from posts where compoundall between -0.05 and 0.05 and compoundall != 0 order by id

select count(*) from posts where  compoundall = 0;

select body, compoundall, id from posts where compoundall between -0.05 and 0.05 and compoundall != 0 order by id offset 150639 fetch first 1 rows only;


select count(*) from posts where compundavg = 0


select count(*) from posts where compundavg != compoundall


select sum(id) from posts group by owneruserid