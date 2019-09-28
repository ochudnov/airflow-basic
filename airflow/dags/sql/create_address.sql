INSERT INTO {{ params.prefix }}_addresses(user_id, country, city, zip_code, address)
VALUES({{ task_instance.xcom_pull(task_ids='get_user_id', key='return_value')[0][0] }},
	'UK', 'London', 'NW1 6XE', '221B Baker Street');
