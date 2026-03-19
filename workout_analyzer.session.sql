/*"How many exercises are Push, Pull, or Push & Pull across the entire dataset?"
*/
SELECT 
    force,
    count(*) as push_pull_count
FROM exercises

GROUP BY
    force
