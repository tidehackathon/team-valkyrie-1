-- capabilities_id_seq sequence
create sequence if not exists capabilities_id_seq
    as integer;

-- nations_id_seq sequence
create sequence if not exists nations_id_seq
    as integer;

-- ndpp_capabilities table
create table if not exists ndpp_capabilities
(
    id               serial
        primary key,
    code             varchar(30)  not null,
    description      varchar(255) not null,
    operational_area varchar(100) not null
);

-- capability_operational_domains table
create table if not exists capability_operational_domains
(
    capability_id         integer not null,
    operational_domain_id integer not null,
    constraint capability_operational_domain_capability_id_operational_dom_key
        unique (capability_id, operational_domain_id)
);

-- capability_tasks table
create table if not exists capability_tasks
(
    capability_id integer not null,
    task_id       integer not null,
    constraint capability_tasks_capability_id_task_id_capability_id1_task__key
        unique (capability_id, task_id)
);

-- capability_warfarelevels table
create table if not exists capability_warfarelevels
(
    capability_id   integer not null,
    warfarelevel_id integer not null,
    constraint capability_warfarelevels_capability_id_warfarelevel_id_capa_key
        unique (capability_id, warfarelevel_id)
);

-- focus_areas table
create table if not exists focus_areas
(
    id                    serial
        constraint focus_areas_pk
            primary key,
    name                  varchar not null,
    is_operational_domain smallint default 0
);

-- issue_categories table
create table if not exists issue_categories
(
    id          serial
        primary key,
    name        varchar(255) not null,
    description text
);

-- nations table
create table if not exists nations
(
    id   integer default nextval('nations_id_seq'::regclass) not null
        constraint nations_fk
            primary key,
    name varchar(100)                                        not null
);

-- capabilities table
create table if not exists capabilities
(
    id        integer default nextval('capabilities_id_seq'::regclass) not null
        constraint capabilities_pk
            primary key,
    nation_id integer                                                  not null
        constraint nation_capabilities_fk
            references nations
            on delete cascade,
    name      varchar(255),
    maturity  varchar(50)
);

-- objectives table
create table if not exists objectives
(
    id             serial
        constraint objective_pk
            primary key,
    focus_area_id  integer      not null
        constraint fa_objective_fk
            references focus_areas
            on delete cascade,
    name           varchar(200) not null,
    title          varchar(255),
    exercise_cycle varchar(20)  not null
);

-- operational_domains table
create table if not exists operational_domains
(
    id   serial
        primary key,
    name varchar(100) not null
);

-- standards table
create table if not exists standards
(
    id    serial
        primary key,
    name  varchar(255) not null,
    title char(500),
    type  varchar(50)
);

-- tasks table
create table if not exists tasks
(
    id   serial
        primary key,
    name varchar(255) not null
);

-- testcases table
create table if not exists testcases
(
    id               serial
        primary key,
    tc_number        varchar(100),
    exercise_cycle   varchar(50)  not null,
    title            varchar(255) not null,
    overall_result   varchar(50),
    io_shortfall_ind boolean
);

-- test_objectives table
create table if not exists test_objectives
(
    testcase_id    integer not null
        references testcases
            on delete cascade,
    objective_id   integer not null
        references objectives
            on delete cascade,
    exercise_cycle varchar(50)
);

-- test_participants table
create table if not exists test_participants
(
    capability_id      integer     not null
        constraint capability_testcases_fk
            references capabilities
            on delete cascade,
    testcase_id        integer     not null
        constraint testcases_capability_fk
            references testcases
            on delete cascade,
    exercise_cycle     varchar(50) not null,
    participant_role   varchar(50) not null,
    participant_result varchar(50)
);

-- testcase_issue_categories table
create table if not exists testcase_issue_categories
(
    testcase_id       integer not null
        constraint testcase_issue_fk
            references testcases,
    issue_category_id integer not null
        constraint issue_testcases_fk
            references issue_categories
);

-- testcase_standards table
create table if not exists testcase_standards
(
    testcase_id integer not null
        constraint tc_standards_fk
            references testcases,
    standard_id integer not null
        constraint standards_tc_fk
            references standards
            on delete cascade
);

-- warfare_levels table
create table if not exists warfare_levels
(
    id   serial
        primary key,
    name varchar(100) not null
);
