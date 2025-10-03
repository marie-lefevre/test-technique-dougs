SELECT
    u.user_id,
    u.profile_id,
    u.preferred_company_id,
    u.accounting_firm_office_id,
    u.created_at,
    u.suspended_at,
    u.deleted_at,
    u.email,
    u.role,
    u.flags,
    u.is_signup_completed,
    u.date_last_refresh
FROM {{ ref('stg_users') }} AS u