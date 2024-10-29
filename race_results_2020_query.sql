SELECT 
    races.race_year,
    races.race_name,
    races.race_date,
    races.circuit_location,
    drivers.driver_name,
    drivers.driver_number,
    drivers.driver_nationality,
    constructors.team,
    results.grid,
    results.fastest_lap,
    results.race_time,
    results.points
FROM 
    results
JOIN 
    races ON results.race_id = races.race_id
JOIN 
    drivers ON results.driver_id = drivers.driver_id
JOIN 
    constructors ON results.constructor_id = constructors.constructor_id
WHERE 
    races.race_year = 2020
ORDER BY 
    results.points DESC;
