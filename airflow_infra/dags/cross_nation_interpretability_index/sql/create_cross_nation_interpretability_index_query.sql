CREATE TABLE IF NOT EXISTS cross_nation_interpretability_index
(
    consumer_id           INTEGER NOT NULL REFERENCES nations (id),
    provider_id           INTEGER NOT NULL REFERENCES nations (id),
    operational_domain_id INTEGER REFERENCES operational_domains (id),
    score                 FLOAT   NOT NULL
);
