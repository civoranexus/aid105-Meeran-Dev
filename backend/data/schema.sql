CREATE TABLE schemes (
    id SERIAL PRIMARY KEY,
    scheme_id VARCHAR(20) UNIQUE NOT NULL,
    name TEXT NOT NULL,
    level VARCHAR(20),
    state VARCHAR(50),
    min_age INT,
    max_age INT,
    min_income INT,
    max_income INT,
    target_groups TEXT[],
    benefits TEXT,
    documents_required TEXT[],
    deadline DATE
);
