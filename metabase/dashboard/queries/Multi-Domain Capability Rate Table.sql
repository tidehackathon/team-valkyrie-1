with P as (select testcase_id
           from public.test_participants
           where participant_role = 'Provider'
           group by testcase_id
           having count(1) = 1
           intersect
           select testcase_id
           from public.test_participants
           where participant_role = 'Consumer'
           group by testcase_id
           having count(1) >= 1),
     C as (select distinct c.consumer_capability_id, p.exercise_cycle
           from (select tp.testcase_id, tp.exercise_cycle
                 from public.test_participants tp
                          join P p on p.testcase_id = tp.testcase_id
                 where tp.participant_role = 'Provider') p
                    join (select tp.testcase_id, tp.capability_id as consumer_capability_id
                          from public.test_participants tp
                                   join P p on p.testcase_id = tp.testcase_id
                          where tp.participant_role = 'Consumer') c on c.testcase_id = p.testcase_id)
select n.name                                                                           as nation
     , 100.0 * sum(case when cd.domain_count > 1 and c.exercise_cycle = 'CWIX 2021' then 1 else 0 end)
    / nullif(sum(case when c.exercise_cycle = 'CWIX 2021' then 1 else 0 end), 0)        as score_2021

     , 100.0 * sum(case when cd.domain_count > 1 and c.exercise_cycle = 'CWIX 2022' then 1 else 0 end)
    / nullif(sum(case when c.exercise_cycle = 'CWIX 2022' then 1 else 0 end), 0)        as score_2022

     , 100.0 * sum(case when cd.domain_count > 1 and c.exercise_cycle = 'CWIX 2022' then 1 else 0 end)
           / nullif(sum(case when c.exercise_cycle = 'CWIX 2022' then 1 else 0 end), 0)
    -
       100.0 * sum(case when cd.domain_count > 1 and c.exercise_cycle = 'CWIX 2021' then 1 else 0 end)
           / nullif(sum(case when c.exercise_cycle = 'CWIX 2021' then 1 else 0 end), 0) as difference
from C c
         left join (select capability_id, count(1) as domain_count
                    from public.capability_operational_domains
                    group by capability_id) cd on cd.capability_id = c.consumer_capability_id
         left join public.capabilities ca on ca.id = c.consumer_capability_id
         left join public.nations n on n.id = ca.nation_id
group by n.name
order by n.name;