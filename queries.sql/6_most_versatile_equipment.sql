/*
Which equipment type allows you to train the most different muscle groups?
*/

select 
    equipment,
    COUNT(Distinct main_muscle) as muscle_group_count
FROM exercises

GROUP BY
    equipment
ORDER BY
    muscle_group_count DESC;
