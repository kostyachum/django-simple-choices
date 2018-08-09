# django-simple-choices
Simple enhancemnt for choices structure to use with django models and more

# Usage

``` python
from . import choices
class Statues(choices.EnumChoices):
    FROZEN = choices.Choice('frozen', _('Frozen'))
    INVALID = choices.Choice('invalid', _('Invalid'))
    PENDING_REVIEW = choices.Choice('pending', _('Pending'))
    INCOMPLETE = choices.Choice('incomplete', _('Incomplete'))
    ACTIVE = choices.Choice('active', _('Active'))

CHOICES_PRIORITY = [
    Statues.ACTIVE,
    Statues.FROZEN,
    Statues.PENDING_REVIEW,
    Statues.INCOMPLETE,    
]
```
