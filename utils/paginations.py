from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def page(query, quanity=None, page=None):
    paginator = Paginator(query, quanity)

    try:
        users = paginator.page(page)

    except PageNotAnInteger:
        output = {'page': "page not found"}
        obj = {"query": output, 'page_detail': ""}
        return obj

    except EmptyPage:
        paginator = Paginator(query, 1)
        users = paginator.page(1)
        page_detail = {
            'total_data_count': paginator.count, 'data_qty': paginator.per_page,
            "current_page": 1, "total_of_pages": paginator.num_pages,
        }

        obj = {"query": users.object_list, 'page_detail': page_detail}
        return obj

    page_detail = {
        'total_data_count': paginator.count, 'data_qty': paginator.per_page,
        "current_page": int(page), "total_of_pages": paginator.num_pages,
    }

    obj = {"query": users.object_list, 'page_detail': page_detail}
    return obj