select nation_name,
       SUM(CASE WHEN operational_domain_name = 'Air' THEN score END) as "Air",
       SUM(CASE WHEN operational_domain_name = 'Land' THEN score END) as "Land",
       SUM(CASE WHEN operational_domain_name = 'Maritime' THEN score END) as "Maritime",
       SUM(CASE WHEN operational_domain_name = 'Cyberspace' THEN score END) as "Cyberspace",
       SUM(CASE WHEN operational_domain_name = 'Space' THEN score END) as "Space",
       SUM(CASE WHEN operational_domain_name = 'Other Support Services' THEN score END) as "Other Support Services"
       from (with P as (select testcase_id
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
   , C as (select distinct tp.capability_id
           from public.test_participants tp
                    join P p on p.testcase_id = tp.testcase_id
           where tp.participant_role = 'Provider')
   , NDPP as (select d.id
                   , d.name
                   , coalesce(c.ndpp_capability_count, 0) as ndpp_capability_count
              from public.operational_domains d
                       left join (select operational_domain_id, count(1) as ndpp_capability_count
                                  from public.ndpp_capabilities
                                  group by operational_domain_id) c on c.operational_domain_id = d.id)
   , CAP as (select c.capability_id
                  , c.operational_domain_id
                  , d.name as operational_domain_name
                  , ndpp.ndpp_capability_count
                  , 1      as capability_count
             from public.capability_operational_domains c
                      join public.operational_domains d on d.id = c.operational_domain_id
                      join NDPP ndpp on ndpp.id = c.operational_domain_id)
   , D as (select b.nation_id
                , n.name                                                        as nation_name
                , cap.operational_domain_id
                , cap.operational_domain_name
                , 100.0 * sum(cap.capability_count) / cap.ndpp_capability_count as index

           from public.capabilities b
                    join C c on c.capability_id = b.id
                    left join public.nations n on n.id = b.nation_id
                    join CAP cap on cap.capability_id = b.id
           group by b.nation_id
                  , n.name
                  , cap.operational_domain_id
                  , cap.operational_domain_name
                  , cap.ndpp_capability_count)
select nation_name
     , operational_domain_name
     , case when index > 100 then 100 else index end as score

from D) AS _
GROUP BY nation_name;