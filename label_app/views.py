from django.shortcuts import render
from label_app.db_controller import DBController
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from label_app import utils
import json

def home(request):
    return render(request, 'home.html')


@csrf_exempt
def search_label(request):

    user_searched = None
    search_results = []

    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        user_searched = post_data['label_search']

        with DBController() as db:
            search_results = db.get_search_label_result(user_searched, abs_static=request.get_host())

        return JsonResponse({"data": search_results})

    elif request.method == "GET":
        user_searched = request.GET['label_search']

        with DBController() as db:
            search_results = db.get_search_label_result(user_searched)

        return render(request, 'search_label.html', {"results_list": search_results})

    else:
        return render(request, 'home.html')


def label_details(request, guid):

    sql_select_label = """
                        SELECT lbl_guid, lbl_name, lbl_details, lbl_score_total, lbl_score_transparency, lbl_score_ecological, 
                        lbl_score_quality, lbl_image_media_path
                        FROM lbl_labels
                        WHERE lbl_guid = %s
                        """

    with DBController() as db:
        results = db.query(sql_select_label, (guid,))

    results_dict = {}

    if results:
        lbl_guid, lbl_name, lbl_details, lbl_score_total, lbl_score_transparency, lbl_score_ecological, \
        lbl_score_quality, lbl_image_media_path = results[0]

        results_dict = {"guid": lbl_guid,
                        "name": lbl_name,
                        "details": lbl_details,
                        "score_total": utils.get_total_score_display(lbl_score_total),
                        "score_transparency": utils.get_total_score_display(lbl_score_transparency),
                        "score_ecological": utils.get_total_score_display(lbl_score_ecological),
                        "score_quality": utils.get_total_score_display(lbl_score_quality),
                        "image_media_path": lbl_image_media_path}

    return render(request, 'label_details.html', {"details": results_dict})

