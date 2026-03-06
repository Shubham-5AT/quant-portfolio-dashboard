
CREATE DATABASE IF NOT EXISTS economic_data;

USE economic_data;


CREATE TABLE economy (
    country VARCHAR(100),
    year INT,
    GDP BIGINT,
    Population BIGINT,
    Life_Expectancy FLOAT,
    Unemployment_Rate FLOAT,
    CO2_Emissions_metric_tons_per_capita FLOAT,
    Access_to_Electricity FLOAT
);