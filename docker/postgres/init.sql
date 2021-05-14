
-- More on roles: https://www.postgresqltutorial.com/postgresql-roles/
-- Below statement creates a role named "postgres" and has password "postgres"
-- When you login using "postgres" role, you get max privileges because "SUPERUSER" is granted to "postgres"
CREATE ROLE postgres LOGIN SUPERUSER PASSWORD 'postgres';
CREATE DATABASE pluralsight;
GRANT ALL PRIVILEGES ON DATABASE pluralsight to airflow;

