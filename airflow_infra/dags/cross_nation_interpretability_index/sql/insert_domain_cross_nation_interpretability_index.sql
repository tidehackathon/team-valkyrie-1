INSERT INTO cross_nation_interpretability_index
    (with P as (select testcase_id
                from public.test_participants
                where participant_role = 'Provider'
                group by testcase_id
                having count(1) = 1
                intersect
                select testcase_id
                from public.test_participants
                where participant_role = 'Consumer'
                group by testcase_id
                having count(1) >= 1)
     select pn.id              as provider_id
          , cn.id              as consumer_id
          , cod.id             as operation_domain_id

          , 100.0 * sum(case when c.consumer_participant_result = 'Success' then 1 else 0 end)
         / nullif(count(*), 0) as score

     from (select tp.capability_id      as provider_capability_id,
                  tp.testcase_id,
                  tp.exercise_cycle,
                  tp.participant_result as provider_participant_result
           from public.test_participants tp
                    join P p on p.testcase_id = tp.testcase_id
           where tp.participant_role = 'Provider') p
              join (select tp.capability_id      as consumer_capability_id,
                           tp.testcase_id,
                           tp.exercise_cycle,
                           tp.participant_result as consumer_participant_result
                    from public.test_participants tp
                             join P p on p.testcase_id = tp.testcase_id
                    where tp.participant_role = 'Consumer') c on c.testcase_id = p.testcase_id
              join public.capabilities cp on cp.id = p.provider_capability_id
              join public.nations pn on pn.id = cp.nation_id
              join public.capabilities cc on cc.id = c.consumer_capability_id
              join public.nations cn on cn.id = cc.nation_id

              left join public.capability_operational_domains ccod on ccod.capability_id = c.consumer_capability_id
              left join public.operational_domains cod on cod.id = ccod.operational_domain_id
     group by pn.id, cn.id, cod.id);

