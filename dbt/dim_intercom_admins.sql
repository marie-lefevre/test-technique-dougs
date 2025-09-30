SELECT
    saia.ic_admin_id,
    saia.name,
    saia.type,
    saia.email,
    saia.job_title,
    saia.has_inbox_seat,
    saia.away_mode_enabled,
    saia.away_mode_reassign,
    saia.date_last_refresh
FROM {{ ref('stg_airbyte_intercom_admins') }} saia