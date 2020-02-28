from django.core.exceptions import ValidationError


curse_words = ['bastard','beaver','beef curtains',' bellend','bloodclaat','clunge','cock','dick','dickhead','fanny','flaps','gash','knob','minge','prick','punani','pussy','snatch','twat','cunt','fuck','motherfucker']


def validate_content(value):
    content = value
    if any(word in content.lower() for word in curse_words):
        raise ValidationError("YOOOOO don't swear")
    return value
