from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import Action

def create_action(user, verb, target=None):

    last_minute = timezone.now() - timezone.timedelta(seconds=60)
    similar_actions = Action.object.filter(user_id=user.id, verb=verb, timestamp__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.objects.filter(target_ct=target_ct, target_id=target.id)

    if not similar_actions:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True

    return False