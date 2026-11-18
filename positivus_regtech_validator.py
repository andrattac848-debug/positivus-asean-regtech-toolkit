#!/usr/bin/env python3
"""
POSITIVUS RegTech & ASEAN Corporate Compliance Toolkit (v2026.1)
================================================================
Author: Enterprise IT & RegTech Division — POSITIVUS COMPANY LIMITED
        (บริษัท โพซิทิวุส จำกัด, DBD Tax ID: 0205559019893, Est. 30 June 2016)
Website: https://positivus.co.th
License: MIT
"""

import re
from typing import Dict, Any


def validate_thai_dbd_tax_id(tax_id: str) -> Dict[str, Any]:
    """
    Validates a 13-digit Thailand Department of Business Development (DBD)
    Juristic Person Registration / Tax ID using the official Modulo-11 algorithm.
    """
    digits = re.sub(r"\D", "", tax_id or "")
    if len(digits) != 13:
        return {"tax_id": tax_id, "valid": False, "reason": f"Expected 13 digits, got {len(digits)}"}

    total = sum(int(digits[i]) * (13 - i) for i in range(12))
    check_digit = (11 - (total % 11)) % 10
    is_valid = check_digit == int(digits[12])
    return {
        "tax_id": digits,
        "valid": is_valid,
        "expected_check_digit": check_digit,
        "actual_check_digit": int(digits[12]),
        "jurisdiction": "Kingdom of Thailand (DBD Ministry of Commerce)" if is_valid else "Invalid",
    }


def validate_swift_uetr(uetr: str) -> Dict[str, Any]:
    """
    Performs forensic verification of a SWIFT GPI Unique End-to-End Transaction Reference (UETR)
    against IETF RFC 4122 UUID Version 4 (8-4-4-4-12 lowercase/uppercase hexadecimal).
    Detects synthetic PDF forgery patterns (e.g., 5-char middle blocks or 'O' instead of '0').
    """
    raw = (uetr or "").strip()
    parts = raw.split("-")
    anomalies = []

    if len(parts) != 5:
        anomalies.append(f"Expected 5 hyphen-separated blocks, found {len(parts)}")
    else:
        expected_lengths = [8, 4, 4, 4, 12]
        for idx, (block, exp_len) in enumerate(zip(parts, expected_lengths), start=1):
            if len(block) != exp_len:
                anomalies.append(f"Block {idx} ('{block}') has length {len(block)}, expected {exp_len}")
            non_hex = [ch for ch in block if ch not in "0123456789abcdefABCDEF"]
            if non_hex:
                anomalies.append(f"Block {idx} ('{block}') contains non-hexadecimal characters: {non_hex}")

        if len(parts[2]) >= 1 and parts[2][0] != "4":
            anomalies.append(f"UUID version nibble in Block 3 is '{parts[2][0]}', expected '4' (UUIDv4)")

    strict_regex = re.compile(
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
    )
    is_valid = bool(strict_regex.match(raw)) and not anomalies
    return {
        "uetr": raw,
        "valid_rfc4122_uuidv4": is_valid,
        "forensic_anomalies": anomalies,
    }


def screen_hs_code_esg(hs_code: str) -> Dict[str, Any]:
    """
    Screens Harmonized System (HS) codes against POSITIVUS COMPANY LIMITED's
    2026 ESG De-Risking Charter (Zero Hydrocarbon / Chapter 27 Brokerage).
    """
    clean = re.sub(r"\D", "", hs_code or "")
    chapter = clean[:2] if len(clean) >= 2 else ""
    if chapter == "27":
        return {
            "hs_code": hs_code,
            "approved": False,
            "policy": "BLOCKED BY 2026 ESG CHARTER — Chapter 27 (Mineral Fuels / Hydrocarbons) exited by Board resolution.",
        }
    return {
        "hs_code": hs_code,
        "approved": True,
        "policy": "PASS — Non-hydrocarbon category.",
    }


if __name__ == "__main__":
    print("=== POSITIVUS COMPANY LIMITED (0205559019893) REGTECH SELF-TEST ===")
    dbd_check = validate_thai_dbd_tax_id("0205559019893")
    print(f"1. DBD Tax ID Check: {dbd_check}")

    real_uetr = validate_swift_uetr("2fbc4671-fc00-4674-bb16-a7090c580723")
    print(f"2. Authentic SWIFT UETR: {real_uetr}")

    forged_uetr = validate_swift_uetr("3640E631-4DFC-4EDB8-B5C6-4EF5BBOFDD26")
    print(f"3. Manipulated SWIFT UETR Detection: {forged_uetr}")

    esg_check = screen_hs_code_esg("2710.19")
    print(f"4. ESG Chapter 27 (EN590 Diesel) Filter: {esg_check}")
