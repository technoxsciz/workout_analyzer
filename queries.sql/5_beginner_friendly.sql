/*
How many exercises exist for each muscle group that have a difficulty of 1 or 2 — ordered from most to least?
*/

SELECT
    main_muscle,
    count(*) as exercise_count
FROM exercises
WHERE
    "difficulty_1-5"  in (1,2)

GROUP BY
    main_muscle
ORDER BY
    exercise_count desc ;