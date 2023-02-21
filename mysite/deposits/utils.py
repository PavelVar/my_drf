from datetime import date, timedelta

from dateutil.relativedelta import relativedelta
from rest_framework.permissions import BasePermission, SAFE_METHODS


def get_end_date(start_date: date, duration: int) -> date:
    # start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    # return (date.today() + relativedelta(months=duration)).strftime("%Y-%m-%d")
    return start_date + relativedelta(months=duration)


def check_early_withdrawal_possible(created_at: date) -> bool:
    today = date.today()
    min_possible_term_to_close = timedelta(days=20)

    return today - created_at > min_possible_term_to_close


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )
