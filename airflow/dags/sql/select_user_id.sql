SELECT id FROM {{ params.prefix }}_users
WHERE name = 'user_{{ ts_nodash }}' AND email = 'user_{{ ts_nodash }}@example.com';
