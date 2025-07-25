from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ValidationError


def calculate_repayment_score(payment_status):
    mapping = {
        'on_time': 1.0,
        'minor_delay': 0.5,
        'major_delay': 0.0,
    }
    return mapping.get(payment_status, 0.0)


def calculate_credit_score(user, livestock_number, monthly_income, max_income, repayment_status,
                           w1=0.4, w2=0.4, w3=0.2):

    if user.type != 'farmer':
        raise PermissionDenied("Credit score calculation only available for farmers.")

    if not (1 <= livestock_number <= 30):
        raise ValidationError("Livestock number must be between 1 and 30 inclusive.")

    if monthly_income < 0:
        raise ValidationError("Monthly income must be non-negative.")

    if max_income <= 0:
        raise ValidationError("Maximum income must be positive.")

    repayment_score = calculate_repayment_score(repayment_status)
    livestock_score = livestock_number / 30
    income_score = monthly_income / max_income

    weighted_sum = w1 * livestock_score + w2 * income_score + w3 * repayment_score
    normalized_0_100 = weighted_sum * 100
    credit_score_100_850 = 100 + normalized_0_100 * 7.5

    return min(credit_score_100_850, 850)


def determine_max_loan_amount(credit_score_value):
    low_threshold = 325
    mid_threshold = 575

    if credit_score_value < low_threshold:
        return 2000
    elif low_threshold <= credit_score_value <= mid_threshold:
        proportion = (credit_score_value - low_threshold) / (mid_threshold - low_threshold)
        loan_amount = 2000 + proportion * (100000 - 2000)
        return int(loan_amount)
    else:
        return 150000
