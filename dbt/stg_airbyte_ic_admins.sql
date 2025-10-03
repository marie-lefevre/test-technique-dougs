SELECT
    CAST(sbaia.id AS STRING) AS ic_admin_id,
    sbaia.name AS name,
    sbaia.type AS type,
    sbaia.email AS email,
    sbaia.job_title AS job_title,
    sbaia.has_inbox_seat AS has_inbox_seat,
    sbaia.away_mode_enabled AS away_mode_enabled,
    sbaia.away_mode_reassign AS away_mode_reassign,
    MAX(sbaia._airbyte_extracted_at) OVER () AS date_last_refresh
FROM {{ source('bronze_airbyte_intercom', 'admins') }} AS sbaia
ORDER BY 1