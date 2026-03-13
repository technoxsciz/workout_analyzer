/* 
How many exercises can be performed with each type of equipment, ordered from most to least?
*/

SELECT 
    equipment,
    count(*) as exercise_count
FROM exercises

GROUP BY
    equipment

ORDER BY
    exercise_count desc;