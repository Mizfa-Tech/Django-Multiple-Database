from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Imdb(DjangoCassandraModel):
    imdb_id = columns.Text(max_length=10, primary_key=True, required=True)
    title = columns.Text()
    release_date = columns.DateTime()
    cover_url = columns.Text()
    genres = columns.List(value_type=columns.Text)
    description = columns.Text()
    director = columns.List(value_type=columns.Text)
    writers = columns.List(value_type=columns.Text)
    country_of_origin = columns.Text()
    language = columns.List(value_type=columns.Text)
    run_time = columns.Text()
    rate = columns.Text()
    rete_population = columns.Text()
    casts = columns.Map(key_type=columns.Text, value_type=columns.Text)
    stars = columns.List(value_type=columns.Text)

    def __str__(self):
        return self.imdb_id
