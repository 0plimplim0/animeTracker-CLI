create table if not exists animes(
    id integer primary key,
    title text not null,
    episodes integer,
    current_episode integer default 0,
    status text not null check (status in ('plan_to_watch', 'watching', 'completed', 'dropped')) default 'plan_to_watch',
    notes text,
    started_at text,
    finished_at text
);