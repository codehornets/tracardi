from typing import Optional

from dotty_dict import Dotty
from tracardi.domain.profile import FlatProfile
from tracardi.service.utils.date import now_in_utc


def _get_interest_and_value(event: Dotty):
    interest, value = None, None
    if 'properties.interest' in event:
        interest = event['properties.interest']
        if 'properties.value' in event:
            value = float(event['properties.value'])
        else:
            value = 1.0

    return interest, value

def increase_interest(event: Dotty, profile: Optional[FlatProfile]):
    if profile:
        interest, value = _get_interest_and_value(event)
        if isinstance(interest, str):
            profile.increase_interest(interest, value)
            profile.set_field_change(f"interests.{interest}", [now_in_utc(), event.get('id', None)])
            profile.mark_for_update()

def decrease_interest(event: Dotty, profile: Optional[FlatProfile]):
    if profile:
        interest, value = _get_interest_and_value(event)
        if isinstance(interest, str):
            profile.decrease_interest(interest, value)
            profile.set_field_change(f"interests.{interest}", [now_in_utc(), event.get('id', None)])
            profile.mark_for_update()

def reset_interest(event: Dotty, profile: Optional[FlatProfile]):
    if profile:
        interest, value = _get_interest_and_value(event)
        if isinstance(interest, str):
            profile.reset_interest(interest, value)
            profile.set_field_change(f"interests.{interest}", [now_in_utc(), event.get('id', None)])
            profile.mark_for_update()