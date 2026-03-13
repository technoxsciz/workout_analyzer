-- which muscle group has the most exercises in the dataset
SELECT main_muscle, COUNT(*) as exercise_count
FROM exercises
GROUP BY main_muscle
ORDER BY exercise_count DESC;
