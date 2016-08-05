from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def getpagerecords(object_list,page_no):
    paginator = Paginator(object_list,settings.PAGE_SIZE)
    try:
        records = paginator.page(page_no)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return records