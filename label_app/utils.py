import os
import MySQLdb as db


def get_db_connection() -> db.Connection:

    db_host = os.getenv("DATABASE_HOST")
    db_user = os.getenv("DATABASE_USER")
    db_password = os.getenv("DATABASE_PASSWORD")
    db_database = os.getenv("DATABASE_NAME")
    db_port = int(os.getenv("DATABASE_PORT"))

    repo_db_connection = db.Connection(host=db_host,
                                       port=db_port,
                                       user=db_user,
                                       passwd=db_password,
                                       db=db_database,
                                       )

    return repo_db_connection
