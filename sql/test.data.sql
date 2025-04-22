INSERT INTO customer.customers (contact_person, address, city, region, postal_code, country, phone_number, email, inn, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('Ярослав Орлов', 'плещеева ул дом 15 кор 3
', 'Москва', 'Москва', '127560', 'Россия', '89252615068', 'orlov.avis20@gmail.com', '1231465789', '3617a771-a34e-4d38-821e-c3b9da5a052f'::uuid, '2025-04-22 08:57:37.000', '2025-04-22 08:57:37.000', false, NULL);


INSERT INTO employee.employees (first_name, last_name, "position", phone_number, email, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('Orlov', 'Yaroslav', 'Backend', '456789132456', 'orlov.avis@yandex.ru', 'bae7d6e3-a923-49ea-bcd9-49e01b429594'::uuid, '2025-04-22 08:52:35.000', '2025-04-22 08:52:35.000', false, NULL);

INSERT INTO supplier.suppliers (company_name, contact_person, address, city, region, postal_code, phone_number, email, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('ООО Ромашка', '1', '1', '1', '1', '1', '1', '1', 'c060e921-b907-4c39-9973-44901d34b379'::uuid, '2025-04-22 08:29:29.000', '2025-04-22 08:29:29.000', false, NULL);

INSERT INTO inventory.warehouses ("name", address, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('ООО СЛАД 1', 'Где-то там', '0a367632-c20c-4bb1-899d-262ac9454814'::uuid, '2025-04-22 08:28:38.000', '2025-04-22 08:28:38.000', false, NULL);

INSERT INTO inventory.arrivals (supplier_id, warehouse_id, arrival_date, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('c060e921-b907-4c39-9973-44901d34b379'::uuid, '0a367632-c20c-4bb1-899d-262ac9454814'::uuid, '2025-04-21', '5cc1ec9f-a995-4555-a0c2-ef38e29b22b9'::uuid, '2025-04-22 08:30:29.000', '2025-04-22 08:30:29.000', false, NULL);

INSERT INTO inventory.categories ("name", description, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('Железобетонные изделия', NULL, '4dd00769-1c1e-4ecc-8ada-3fd23559f1d1'::uuid, '2025-04-22 07:23:44.000', '2025-04-22 07:23:44.000', false, NULL);

INSERT INTO inventory.nomenclature (category_id, warehouse_id, arrival_id, "name", unit_of_measure, article_number, price, id, ts_create, ts_modify, is_deleted, "_trigger_off") VALUES('4dd00769-1c1e-4ecc-8ada-3fd23559f1d1'::uuid, '0a367632-c20c-4bb1-899d-262ac9454814'::uuid, '5cc1ec9f-a995-4555-a0c2-ef38e29b22b9'::uuid, 'test', '1', '2121', 100.00, '201639c0-2a53-4598-a77c-3fdf7d43aa9c'::uuid, '2025-04-22 09:26:49.000', '2025-04-22 09:26:49.000', false, NULL);
