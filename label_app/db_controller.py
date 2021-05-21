import os
from django.templatetags.static import static

from label_app import utils


class Database:
    def __init__(self):
        self._conn = utils.get_db_connection()
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

        return self.fetchall()


class DBController(Database):

    def get_search_label_result(self, user_input, abs_static=False):

        sql_search_label = """
                                    SELECT lbl_guid, lbl_name, lbl_short_description, lbl_score_total, lbl_image_media_path
                                    FROM lbl_labels
                                    WHERE lbl_name LIKE %s
                                    """
        results = self.query(sql_search_label, params=('%%%s%%' % user_input,))
        results_list = []

        if results:
            for found_label in results:
                guid, name, short_description, score_total, image_media_path = found_label

                label_info_dict = {"guid": guid,
                                   "name": name,
                                   "short_description": short_description[:80] + '...',
                                   "score_total": score_total,
                                   "score_total_display": utils.get_total_score_display(score_total),
                                   "image_media_path": image_media_path if not abs_static else "/static/" + image_media_path,
                                   "more_info_url": f"labels/{guid}"
                                   }

                results_list.append(label_info_dict)

        return results_list
