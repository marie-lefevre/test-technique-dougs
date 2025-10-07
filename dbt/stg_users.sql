SELECT
    u.user_id AS user_id,
    CAST(u.profile_id AS STRING) AS profile_id,
    CAST(u.preferred_company_id AS STRING) AS preferred_company_id,
    u.accounting_firm_office_id AS accounting_firm_office_id,
    u.created_at,
    u.suspended_at,
    u.deleted_at,
    u.email,
    u.role,
    u.flags,
    u.is_signup_completed,
    u.rgpd_hard_deleted_at,
    _etl_loaded_at AS date_last_refresh
FROM {{ source('bronze_monolith_global', 'users') }} AS u
    WHERE u.rgpd_hard_deleted_at IS NULL