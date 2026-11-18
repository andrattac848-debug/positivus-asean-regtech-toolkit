# POSITIVUS RegTech & ASEAN Corporate Compliance Toolkit (`positivus-asean-regtech-toolkit`)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24350211.svg)](https://doi.org/10.5281/zenodo.24350211)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**Maintained by:** Enterprise IT, AI & RegTech Division — **POSITIVUS COMPANY LIMITED** (`บริษัท โพซิทิวุส จำกัด`, Thailand Ministry of Commerce DBD Registration & Tax ID: `0205559019893`, Incorporated June 30, 2016, Paid-Up Capital: `6,000,000.00 THB`, Chonburi, Eastern Economic Corridor, Kingdom of Thailand)

- **Official Corporate Portal:** [https://positivus.co.th](https://positivus.co.th) | [https://โพซิทิวุส.ธุรกิจ.ไทย](https://โพซิทิวุส.ธุรกิจ.ไทย)
- **Research & Open-Access Whitepaper:** [https://positivus.co.th/research](https://positivus.co.th/research) ([PDF Download](https://positivus.co.th/research/positivus-asean-regtech-whitepaper-2026.pdf))
- **CERN Zenodo Archival DOI:** [https://doi.org/10.5281/zenodo.24350211](https://doi.org/10.5281/zenodo.24350211)
- **Cross-Border D2C Storefront (Positivus Global):** [https://positivusdirect.com](https://positivusdirect.com)

---

## Overview

Developed under **Clause 25 (Enterprise Software & Computer Systems Development)** of the amended 28-clause statutory charter of **POSITIVUS COMPANY LIMITED**, this zero-dependency Python library provides institutional compliance officers, FinTech engineers, and ASEAN corporate advisors with deterministic validation tools:

1. **Thailand DBD 13-Digit Corporate Tax ID Checksum Validator (`validate_thai_dbd_tax_id`):** Mathematical Modulo-11 verification of Thai juristic person registration numbers issued by the Department of Business Development (DBD), Ministry of Commerce.
2. **ISO 20022 / SWIFT GPI `UETR` Cryptographic Validator (`validate_swift_uetr`):** Strict IETF RFC 4122 UUIDv4 verification to instantaneously detect forged or tampered SWIFT MT103 / `pacs.008` payment advisories.
3. **ASEAN ESG & Hydrocarbon De-Risking HS-Code Filter (`screen_hs_code_esg`):** Automated screening of Harmonized System (HS) codes enforcing POSITIVUS COMPANY LIMITED's 2026 ESG Charter (strict exclusion of Chapter 27 hydrocarbons and dual-use items).

## Quick Start

```bash
python3 positivus_regtech_validator.py
```

## Citation

> POSITIVUS COMPANY LIMITED (2026). *Strategic Portfolio Transformation and Automated Trade Compliance in ASEAN (2016–2026): Case Study of POSITIVUS COMPANY LIMITED*. Zenodo. https://doi.org/10.5281/zenodo.24350211

---
© 2016–2026 **POSITIVUS COMPANY LIMITED** (`บริษัท โพซิทิวุส จำกัด`, Reg. No. `0205559019893`, 324/5 Moo 12, Nongprue, Banglamung, Chonburi 20150, Kingdom of Thailand). Released under the MIT License.
