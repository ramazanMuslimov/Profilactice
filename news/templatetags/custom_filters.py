from django import template


register = template.Library()

BAD_WORLD = {
    "Эфиоп" : "Эф**п",
    "нигер" : "ни**р",
    "черный" : "че***й"
}


@register.filter()
def censor(value, code="Эфиоп"):
    postflix=BAD_WORLD[code]

    return f'{value} : {postflix}'