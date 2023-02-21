WITH P AS (
	SELECT testcase_id
	  FROM public.test_participants
     WHERE participant_role = 'Provider'
     GROUP BY testcase_id
    HAVING count(*) = 1
	INTERSECT
	SELECT testcase_id
	  FROM public.test_participants
	 WHERE participant_role = 'Consumer'
	 GROUP BY testcase_id
	HAVING count(1) >= 1
)
SELECT
	100.0 * sum(
	    CASE
	        WHEN p.exercise_cycle = 'CWIX 2021' AND c.consumer_participant_result = 'Success' THEN 1
	        ELSE 0
	    END
	) / sum(
	    CASE
	        WHEN p.exercise_cycle = 'CWIX 2021' THEN 1
	        ELSE 0
	    END
	) AS rate2021
  FROM (
    SELECT tp.testcase_id,
           tp.exercise_cycle,
           tp.participant_result as provider_participant_result
	  FROM public.test_participants tp
	  JOIN P p ON p.testcase_id = tp.testcase_id
	  WHERE tp.participant_role = 'Provider'
) p LEFT JOIN (
    SELECT tp.testcase_id,
           tp.exercise_cycle,
           tp.participant_result as consumer_participant_result
	  FROM public.test_participants tp
	  JOIN P p ON p.testcase_id = tp.testcase_id
	 WHERE tp.participant_role = 'Consumer'
) c ON c.testcase_id = p.testcase_id;
