"""Deliberately imperfect baseline. NOT a payment authorization system."""
from typing import Mapping, Any


def propose(case: Mapping[str, Any]) -> str:
    """Propose approve/review/deny for a synthetic refund request.

    BUG FOR THE EXERCISE: fraud_flag is not considered.
    All real execution requires independent server-side authorization.
    """
    amount = case['amount']
    if amount <= 0:
        return 'deny'
    if not case['has_receipt'] or amount > 100:
        return 'review'
    return 'approve'
