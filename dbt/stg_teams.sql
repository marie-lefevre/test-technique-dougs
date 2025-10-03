SELECT 
    CAST(team.id AS STRING) AS team_id,
    team.name AS team_name,
    CAST(team.user_id AS STRING) AS user_id,
    team.department AS team_department,
    _etl_loaded_at AS date_last_refresh
FROM {{ source('bronze_service_tasks_assignment', 'teams') }} AS team