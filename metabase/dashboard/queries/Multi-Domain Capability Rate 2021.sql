WITH P AS (
    SELECT testcase_id
	  FROM public.test_participants
	 WHERE participant_role = 'Provider'
	 GROUP BY testcase_id
	HAVING count(1) = 1
	INTERSECT
	SELECT testcase_id
	  FROM public.test_participants
	 WHERE participant_role = 'Consumer'
	 GROUP BY testcase_id
	HAVING count(1) >= 1
),
    C AS (
    SELECT DISTINCT c.consumer_capability_id,
                    p.exercise_cycle
      FROM (
        SELECT tp.testcase_id,
               tp.exercise_cycle
          FROM public.test_participants tp
          JOIN P p ON p.testcase_id = tp.testcase_id
     WHERE tp.participant_role = 'Provider'
    ) p JOIN (
        SELECT tp.testcase_id,
               tp.capability_id as consumer_capability_id
          FROM public.test_participants tp
          JOIN P p ON p.testcase_id = tp.testcase_id
         WHERE tp.participant_role = 'Consumer'
    ) c ON c.testcase_id = p.testcase_id
)
SELECT
	100.0 * sum(
	    CASE
	        WHEN cd.domain_count > 1 AND c.exercise_cycle = 'CWIX 2021' THEN 1
	        ELSE 0
	    END
	) / sum(
	    CASE
	        WHEN c.exercise_cycle = 'CWIX 2021' THEN 1
	        ELSE 0
	    END
	) AS rate21
  FROM C c
  LEFT JOIN (
    SELECT capability_id,
           count(1) AS domain_count
	  FROM public.capability_operational_domains
	 GROUP BY capability_id
) cd ON cd.capability_id = c.consumer_capability_id;
