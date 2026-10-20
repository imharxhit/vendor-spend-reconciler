#!/usr/bin/env python3
"""Automated Vendor Invoice vs. Contracted Rate-Card Reconciliation Engine."""
import json
from typing import List, Dict


def audit_invoice_batch(invoices: List[Dict[str, object]]) -> Dict[str, object]:
    discrepancies = []
    total_billed = 0.0
    total_leakage = 0.0
    for inv in invoices:
        total_billed += float(inv["billed_amount_inr"])
        contract_rate = float(inv["contracted_unit_rate_inr"])
        billed_rate = float(inv["billed_unit_rate_inr"])
        qty = float(inv["quantity"])
        if billed_rate > contract_rate * 1.015:
            overcharge = (billed_rate - contract_rate) * qty
            total_leakage += overcharge
            discrepancies.append({
                "invoice_number": inv["invoice_number"],
                "vendor_id": inv["vendor_id"],
                "violation_type": "RATE_CARD_OVERCHARGE",
                "overcharge_inr": round(overcharge, 2),
            })
    return {
        "invoices_audited": len(invoices),
        "total_billed_inr": round(total_billed, 2),
        "total_leakage_identified_inr": round(total_leakage, 2),
        "discrepancies": discrepancies,
    }


if __name__ == "__main__":
    sample = [{
        "vendor_id": "VND-104",
        "invoice_number": "INV-2026-881",
        "quantity": 120,
        "contracted_unit_rate_inr": 1450.0,
        "billed_unit_rate_inr": 1620.0,
        "billed_amount_inr": 194400.0,
    }]
    print(json.dumps(audit_invoice_batch(sample), indent=2))
