SELECT 
    *
FROM {{ source('bronze_service_tasks_assignment', 'collaborators') }} AS col