CREATE TABLE employees(
    e_id SERIAL PRIMARY KEY,
    full_name VARCHAR,
    EMAIL VARCHAR,
    pass VARCHAR,
    dep_id INTEGER
)
CREATE TABLE roles(
    role_id SERIAL REFERENCES  employees(e_id),
    role VARCHAR
)
CREATE TABLE requests (
    req_id SERIAL PRIMARY KEY,
    request_type VARCHAR,
    cost NUMERIC,
    amount NUMERIC,
    grade VARCHAR,
    stat VARCHAR,
    event_date DATE,
    loc VARCHAR,
    emp_id SERIAL REFERENCES employees(e_id)

)
CREATE TABLE EVENTS (
    event_type VARCHAR,
    percen NUMERIC 
)
CREATE TABLE department(
    d_id SERIAL PRIMARY KEY,
    dep_name VARCHAR,
    dep_head VARCHAR REFERENCES employees(e_id)
)
CREATE TABLE grades(
    letter VARCHAR,
    pass_fail VARCHAR
)