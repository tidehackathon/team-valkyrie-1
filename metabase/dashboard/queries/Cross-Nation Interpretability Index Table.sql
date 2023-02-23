SELECT consumer_id,
       provider_id,
       score
  FROM cross_nation_interpretability_index
 WHERE operational_domain_id IS NULL;
