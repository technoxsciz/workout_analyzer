-- What is the average difficulty score for exercises in each muscle group, ordered from hardest to easiest?
SELECT
    main_muscle,
   round( avg("difficulty_1-5"),2) as avg_difficulty
from exercises
group BY
    main_muscle
ORDER BY
    avg_difficulty desc;

