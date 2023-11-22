from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def as_percentage_of(part, whole):
    try:
        return "%d%%" % (float(part) / whole * 100)
    except (ValueError, ZeroDivisionError):
        return ""
