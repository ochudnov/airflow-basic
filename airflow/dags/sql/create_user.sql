INSERT INTO {{ params.prefix }}_users(name, email)
VALUES('user_{{ ts_nodash }}', 'user_{{ ts_nodash }}@example.com');
