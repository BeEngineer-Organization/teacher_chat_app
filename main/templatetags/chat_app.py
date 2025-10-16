from datetime import timedelta

from django import template
from django.utils import timezone

register = template.Library()


@register.filter
@register.simple_tag
def elapsed_time(dt):
    if not dt:
        return None

    delta = timezone.now() - dt

    zero = timedelta()
    one_day = timedelta(days=1)
    two_days = timedelta(days=2)

    # 未来の時刻はエラーにする
    if delta < zero:
        raise ValueError("未来の時刻です。")
    elif delta < one_day:  # 経過時間が 1 日未満のとき
        return "今日"
    elif delta < two_days:  # 経過時間が 1 日以上 2 日未満のとき
        return "昨日"
    else:
        return dt.strftime("%m/%d")  # 「月/日」の形で返す