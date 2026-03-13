--For each muscle group, how many exercises are Compound and how many are Isolated?

select 
    main_muscle,
    mechanics,
    count(*) as mechanics_count
from  exercises

group by
    main_muscle,
    mechanics

order by
    mechanics_count desc;
