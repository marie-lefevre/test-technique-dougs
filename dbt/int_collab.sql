SELECT 
    col.collaborator_id,
    col.user_id,
    col.first_name,
    col.last_name,
    col.full_name,
    us.email,
    DATE(col.created_at) AS created_at,
    col.suspended_at,
    col.team_id,
    tea.team_name,
    tea.team_department,
    col.skills,
    REPLACE(SUBSTR(us.flags, 2, LENGTH(us.flags)-2), "'", "") AS flags,
    col.intercom_preference,
    col.date_last_refresh
FROM {{ ref('dim_collaborators') }} AS col
LEFT JOIN {{ ref('dim_teams') }} AS tea
    ON tea.team_id = col.team_id
LEFT JOIN {{ ref('dim_users') }} AS us
    ON us.user_id = col.user_id

    
