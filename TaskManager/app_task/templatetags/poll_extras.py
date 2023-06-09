from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Model
from app_task.services import get_perms
import re

register = template.Library()

@register.simple_tag(name="my_g", takes_context=True)
def my_g(context, get_par: str, *args, **kwargs):

    inp = get_par.replace("?", "").replace(" ", "")

    gen = iter(args)
    if "=" in inp:
        out = dict(v.split("=") for v in inp.split("&"))
    else:
        out = {}

    for v in gen:
        out[str(v)] = str(next(gen, ""))
    for k, v in kwargs.items():
        out[str(k)] = str(v)

    if out:
        return "?" + "&".join(map("=".join, out.items()))
    return ""


@register.simple_tag(takes_context=True)
def my_gd(context, get_par: str, *args):

    inp = get_par.replace("?", "").replace(" ", "")
    args = tuple(map(str, args))

    if not inp or "=" not in inp:
        return ""
    out = [v for v in inp.split("&") if not v.split("=")[0] in args]

    if out:
        return "?" + "&".join(out)
    return ""


@register.simple_tag(takes_context=True)
def my_gf(context, get_par: str, *args):

    inp = get_par.replace("?", "").replace(" ", "")
    args = tuple(map(str, args))

    if not (inp and "=" in inp):
        return ""
    out = [v for v in inp.split("&") if v.split("=")[0] in args]

    if out:
        return "?" + "&".join(out)
    return ""


@register.simple_tag(takes_context=True)
def my_hp(context, obj: Model) -> bool:
    """Права на работу с записью
    obj - объект текущей записи
    выход словарь разрешений
    """
    out = get_perms(context.dicts[1]["request"], obj)
    return out


@register.simple_tag(takes_context=True)
def my_e(context, *args):
    """Создание переменной из строки"""
    inp = "".join(map(str, args))
    for e in reversed(context.dicts):
        for k, v in e.items():
            try:
                eval(k)
            except Exception:
                locals()[k] = v
    return eval(inp)


@register.simple_tag(takes_context=True)
def my_s(context, *args):
    """Создание строки"""
    return "".join(map(str, args))


@register.filter
@stringfilter
def my_gi(value, get_par):
    """Проверка наличия параметра в GET строке"""
    return value + "=" in get_par


@register.filter
@stringfilter
def my_gg(value, get_par):
    """Получение значения парамера из GET строки"""
    out = re.search(rf"(?<={value}=).+?(?=&)", get_par + "&")
    if out:
        return out[0]
    return out


@register.filter
def my_ds(value: int, par):
    """Склонение чисел
    value - целое число
    par - строка вида "день,дня,дней"
    """
    lst = str(par).split(",") + ["", ""]

    if isinstance(value, str) and value.isdigit():
        value = int(value)
    elif not isinstance(value, int):
        value = 0
    value = abs(value)

    out = lst[2]
    if 11 <= value <= 14:
        pass
    elif value % 10 == 1:
        out = lst[0]
    elif 2 <= value % 10 <= 4:
        out = lst[1]
    return out


@register.filter
def my_ha(value, par: object):
    """Проверка наличия атрибута"""
    return hasattr(par, value)


@register.filter
def my_in_dict(value, par: dict):
    """Проверка наличия ключа в словаре"""
    return value in par


@register.filter
def my_dict_find(value, par: dict):
    """Получение значения по ключу из словаря"""
    return par.get(value, None)
