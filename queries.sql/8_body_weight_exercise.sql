
--How many body weight only exercises exist per muscle group, ordered from most to least?

SELECT 
    main_muscle,
    count(equipment) as bodyweight_exercise_count
FROM exercises
WHERE
    equipment = 'Body Weight'
GROUP BY
    main_muscle
ORDER BY
    bodyweight_exercise_count desc;
