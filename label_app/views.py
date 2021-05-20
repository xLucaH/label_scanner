from django.shortcuts import render
from label_app.db_controller import DBController
from django.urls import reverse

from label_app import utils

def home(request):
    return render(request, 'home.html')


def search_label(request):

    if request.method == "POST":
        user_searched = request.POST['label_search']

        sql_search_label = """
                            SELECT lbl_guid, lbl_name, lbl_short_description, lbl_score_total, lbl_image_media_path
                            FROM lbl_labels
                            WHERE lbl_name LIKE %s
                            """

        with DBController() as db:
            results = db.query(sql_search_label, params=('%%%s%%' % user_searched,))

        if results:

            results_list = []
            for found_label in results:
                guid, name, short_description, score_total, image_media_path = found_label

                label_info_dict = {"guid": guid,
                                   "name": name,
                                   "short_description": short_description[:80] + '...',
                                   "score_total": score_total,
                                   "score_total_display": utils.get_total_score_display(score_total),
                                   "image_media_path": image_media_path,
                                   "more_info_url": f"labels/{guid}"
                                   }

                results_list.append(label_info_dict)

        return render(request, 'search_label.html', {"results_list": results_list})
    else:
        return render(request, 'search_label.html')


def label_details(request, guid):
    return render(request, 'label_details.html')

