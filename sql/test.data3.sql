
INSERT INTO inventory.categories (
        "name",
        description,
        id,
        ts_create,
        ts_modify,
        is_deleted,
        "_trigger_off"
    )
VALUES (
        'Железобетонные изделия',
        'Категория для железобетонных изделий',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Деревянные опоры ЛЭП',
        'Категория для деревянных опор линий электропередачи',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Бетон и газаблоки',
        'Категория для бетона и газаблоков',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Металлические профили',
        'Категория для металлических профилей',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Строительные материалы',
        'Категория для различных строительных материалов',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Электротехническое оборудование',
        'Категория для электротехнического оборудования',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Сантехнические материалы',
        'Категория для сантехнических материалов',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Отопительное оборудование',
        'Категория для отопительного оборудования',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Изоляционные материалы',
        'Категория для изоляционных материалов',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    ),
    (
        'Кровельные материалы',
        'Категория для кровельных материалов',
        uuid_generate_v4(),
        '2025-04-22 07:23:44.000',
        '2025-04-22 07:23:44.000',
        false,
        NULL
    );



-- Вставка товаров для Железобетонные изделия
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Железобетонные изделия'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 1',
    'Блок газобетонный 1',
    NULL,
    'шт',
    120,
    '1234567890',
    1222.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Железобетонные изделия'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 2',
    'Блок газобетонный 2',
    NULL,
    'шт',
    150,
    '1234567891',
    1300.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Железобетонные изделия'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 3',
    'Блок газобетонный 3',
    NULL,
    'шт',
    180,
    '1234567892',
    1400.00,
    uuid_generate_v4()
);

-- Вставка товаров для Деревянные опоры ЛЭП
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Деревянные опоры ЛЭП'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Опора деревянная 1',
    'Опора деревянная 1',
    NULL,
    'шт',
    100,
    '1234567893',
    500.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Деревянные опоры ЛЭП'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Опора деревянная 2',
    'Опора деревянная 2',
    NULL,
    'шт',
    120,
    '1234567894',
    550.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Деревянные опоры ЛЭП'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Опора деревянная 3',
    'Опора деревянная 3',
    NULL,
    'шт',
    150,
    '1234567895',
    600.00,
    uuid_generate_v4()
);

-- Вставка товаров для Бетон и газаблоки
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Бетон и газаблоки'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 4',
    'Блок газобетонный 4',
    NULL,
    'шт',
    100,
    '1234567896',
    1100.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Бетон и газаблоки'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 5',
    'Блок газобетонный 5',
    NULL,
    'шт',
    120,
    '1234567897',
    1200.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Бетон и газаблоки'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Блок газобетонный 6',
    'Блок газобетонный 6',
    NULL,
    'шт',
    150,
    '1234567898',
    1300.00,
    uuid_generate_v4()
);

-- Вставка товаров для Металлические профили
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Металлические профили'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Профиль металлический 1',
    'Профиль металлический 1',
    NULL,
    'шт',
    100,
    '1234567899',
    200.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Металлические профили'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Профиль металлический 2',
    'Профиль металлический 2',
    NULL,
    'шт',
    120,
    '1234567900',
    250.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Металлические профили'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Профиль металлический 3',
    'Профиль металлический 3',
    NULL,
    'шт',
    150,
    '1234567901',
    300.00,
    uuid_generate_v4()
);

-- Вставка товаров для Строительные материалы
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Строительные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кирпич 1',
    'Кирпич 1',
    NULL,
    'шт',
    100,
    '1234567902',
    10.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Строительные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кирпич 2',
    'Кирпич 2',
    NULL,
    'шт',
    120,
    '1234567903',
    12.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Строительные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кирпич 3',
    'Кирпич 3',
    NULL,
    'шт',
    150,
    '1234567904',
    14.00,
    uuid_generate_v4()
);

-- Вставка товаров для Электротехническое оборудование
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Электротехническое оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Розетка 1',
    'Розетка 1',
    NULL,
    'шт',
    100,
    '1234567905',
    50.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Электротехническое оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Розетка 2',
    'Розетка 2',
    NULL,
    'шт',
    120,
    '1234567906',
    60.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Электротехническое оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Розетка 3',
    'Розетка 3',
    NULL,
    'шт',
    150,
    '1234567907',
    70.00,
    uuid_generate_v4()
);

-- Вставка товаров для Сантехнические материалы
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Сантехнические материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кран 1',
    'Кран 1',
    NULL,
    'шт',
    100,
    '1234567908',
    200.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Сантехнические материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кран 2',
    'Кран 2',
    NULL,
    'шт',
    120,
    '1234567909',
    250.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Сантехнические материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кран 3',
    'Кран 3',
    NULL,
    'шт',
    150,
    '1234567910',
    300.00,
    uuid_generate_v4()
);

-- Вставка товаров для Отопительное оборудование
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Отопительное оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Котел 1',
    'Котел 1',
    NULL,
    'шт',
    100,
    '1234567911',
    500.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Отопительное оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Котел 2',
    'Котел 2',
    NULL,
    'шт',
    120,
    '1234567912',
    600.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Отопительное оборудование'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Котел 3',
    'Котел 3',
    NULL,
    'шт',
    150,
    '1234567913',
    700.00,
    uuid_generate_v4()
);

-- Вставка товаров для Изоляционные материалы
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Изоляционные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Теплоизоляция 1',
    'Теплоизоляция 1',
    NULL,
    'шт',
    100,
    '1234567914',
    100.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Изоляционные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Теплоизоляция 2',
    'Теплоизоляция 2',
    NULL,
    'шт',
    120,
    '1234567915',
    120.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Изоляционные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №1'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Теплоизоляция 3',
    'Теплоизоляция 3',
    NULL,
    'шт',
    150,
    '1234567916',
    140.00,
    uuid_generate_v4()
);

-- Вставка товаров для Кровельные материалы
INSERT INTO inventory.product (
    category_id,
    warehouse_id,
    arrival_id,
    "name",
    description,
    image_url,
    unit_of_measure,
    quantity,
    article_number,
    price,
    id
)
VALUES
(
    (SELECT id FROM inventory.categories WHERE name = 'Кровельные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кровля металлочерепица 1',
    'Кровля металлочерепица 1',
    NULL,
    'шт',
    100,
    '1234567917',
    200.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Кровельные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кровля металлочерепица 2',
    'Кровля металлочерепица 2',
    NULL,
    'шт',
    120,
    '1234567918',
    250.00,
    uuid_generate_v4()
),
(
    (SELECT id FROM inventory.categories WHERE name = 'Кровельные материалы'),
    (SELECT id FROM inventory.warehouses WHERE name = 'Склад №2'),
    (SELECT id FROM inventory.arrivals WHERE arrival_date = '2025-04-26'),
    'Кровля металлочерепица 3',
    'Кровля металлочерепица 3',
    NULL,
    'шт',
    150,
    '1234567919',
    300.00,
    uuid_generate_v4()
);