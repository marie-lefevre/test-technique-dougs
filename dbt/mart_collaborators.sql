SELECT 
    CAST(col.collaborator_id AS INTEGER) AS collaborator_id,
    CAST(col.user_id AS INTEGER) AS user_id,
    col.first_name,
    col.last_name,
    col.full_name,
    col.created_at,
    col.suspended_at,
    CAST(col.team_id AS INTEGER) AS team_id,
    col.team_name,
    col.team_department,
    col.accounting_firm_office_name,
    col.skills,
    col.flags AS user_flags,
    col.intercom_preference,
    DATETIME(CAST(col.date_last_refresh AS TIMESTAMP), 'Europe/Paris') AS date_last_refresh
FROM {{ ref('int_collaborators') }} AS col
