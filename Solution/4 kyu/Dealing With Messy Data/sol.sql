WITH tmp1 AS (
    SELECT
        id,
        -- gi: global, case-insensitive
        LOWER(REGEXP_REPLACE(full_name, '(miss|ms|mr|mrs|dr)\.\s', '', 'gi')) AS full_name,
        credit_limit
    FROM
        prospects
),
tmp2 AS (
    SELECT
        CASE
            WHEN full_name ~ ',' THEN SPLIT_PART(full_name, ', ', 2)
            ELSE SPLIT_PART(full_name, ' ', 1)
        END AS first_name,
        CASE
            WHEN full_name ~ ',' THEN SPLIT_PART(full_name, ', ', 1)
            ELSE SPLIT_PART(full_name, ' ', 2)
        END AS last_name,
        MAX(credit_limit) AS credit_limit
    FROM
        tmp1
    GROUP BY
        1,
        2
)

SELECT
    c.first_name,
    c.last_name,
    c.credit_limit AS old_limit,
    t2.credit_limit AS new_limit
FROM
    customers c
    LEFT JOIN tmp2 t2 ON t2.first_name = LOWER(c.first_name)
    and t2.last_name = LOWER(c.last_name)
where
    c.credit_limit < t2.credit_limit
ORDER BY
    1