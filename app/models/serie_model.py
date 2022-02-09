from . import DataBaseConnector
from psycopg2 import sql

class Serie(DataBaseConnector):

    serie_keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

    def __init__(self, *agr, **kwargs):
        self.serie = kwargs["serie"],
        self.seasons = kwargs["seasons"],
        self.released_date = kwargs["released_date"],
        self.genre = kwargs["genre"],
        self.imdb_rating = kwargs["imdb_rating"]


    def create_serie(self):

        self.create_table()

        self.get_conn_cur()

        query = """
            INSERT INTO
                ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s) 
            RETURNing *   
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        inserted_serie = self.cur.fetchone()

        self.commit_and_cloese()
        
        return inserted_serie


    @classmethod
    def create_table(cls):
        cls.get_conn_cur()

        query = """
            CREATE TABLE IF NOT EXISTS ka_series(
                id              BIGSERIAL       PRIMARY KEY,
                serie           VARCHAR(100)    NOT NULL UNIQUE,
                seasons         INTEGER         NOT NULL,
                released_date   DATE            NOT NULL,
                genre           VARCHAR(50)     NOT NULL,
                imdb_rating     FLOAT           NOT NULL
            )
        """

        cls.cur.execute(query)

        cls.commit_and_cloese()


    @classmethod
    def read_series(cls):

        cls.create_table()
        
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        series = cls.cur.fetchall()
        
        cls.commit_and_cloese()

        return series


    @classmethod
    def get_specific_serie(cls, id):

        cls.create_table()

        cls.get_conn_cur()

        query = sql.SQL(
            """
                SELECT 
                    *
                FROM
                    ka_series
                WHERE
                    id={id}         
            """
        ).format(
            id = sql.Literal(id)
        )

        cls.cur.execute(query)

        serie = cls.cur.fetchone()

        cls.commit_and_cloese()

        return serie
            

    @staticmethod
    def serealiaze_serie(data, keys=serie_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))

        if type(data) is list:
            return [dict(zip(keys, serie)) for serie in data]    