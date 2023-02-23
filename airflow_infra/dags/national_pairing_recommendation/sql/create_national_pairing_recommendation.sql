CREATE TABLE IF NOT EXISTS national_pairing_recommendation
(
    consumer_id           INTEGER NOT NULL REFERENCES nations (id),
    provider_id           INTEGER NOT NULL REFERENCES nations (id),
    operational_domain_id INTEGER REFERENCES operational_domains (id),
    score                 FLOAT   NOT NULL
);
