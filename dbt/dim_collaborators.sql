SELECT 
    col.id,
    col.user_id,
    col.team_id,
    col.first_name,
    col.last_name,
    col.skills,
    col.created_at,
    col.suspended_at,
    col.productivity,
    col.intercom_preference,
    col._etl_loaded_at
FROM {{ ref('stg_collaborators') }} AS col