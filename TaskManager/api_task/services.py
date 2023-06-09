from django.db.models import QuerySet
from rest_framework.request import Request


# Фильтр по данным GET-запроса
def filter(qs: QuerySet, request: Request) -> QuerySet:
    for attr, val in request.query_params.items():
        if hasattr(qs.model, attr):
            if val.lower() in ("none", "null"):
                val = None
            try:
                qs = qs.filter(**{attr: val})
            except Exception:
                pass
    return qs
