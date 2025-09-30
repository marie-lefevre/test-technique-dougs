SELECT 
    team.team_id,
    team.team_name,
    team.user_id,
    team.team_department,
    team.date_last_refresh
FROM {{ ref('stg_teams') }} AS team