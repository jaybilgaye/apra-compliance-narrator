# APRA CPS 234 Information Security — AWS Compliance Report

**Account:** 123456789012  ·  **Region:** ap-southeast-2  ·  **Assessed:** 2026-06-06 18:26:25.671606  ·  **Engine:** template

## Executive summary

This report assesses the account against **APRA CPS 234 Information Security**. Of **10 automated controls**, **1 passed** and **9 failed** — an automated compliance score of **10%**. A further **8 controls require manual assessment** (governance/process obligations not observable from AWS APIs).

**Priority controls not met:**
- CPS 234 ¶21 — Implementation of controls - access management (4 finding(s))
- CPS 234 ¶21 — Implementation of controls - multi-factor authentication (2 finding(s))
- CPS 234 ¶21 — Implementation of controls - password policy (7 finding(s))
- CPS 234 ¶21 — Implementation of controls - prevent public exposure (1 finding(s))
- CPS 234 ¶21 — Implementation of controls - audit logging (3 finding(s))
- CPS 234 ¶21 — Implementation of controls - threat detection (3 finding(s))
- CPS 234 ¶21 — Implementation of controls - backup and availability (1 finding(s))
- CPS 234 ¶23 — Incident management - detection and alerting (4 finding(s))
- CPS 234 ¶27 — Testing control effectiveness (1 finding(s))

## Control-by-control assessment

### Roles and responsibilities

#### 📋 CPS 234 ¶13 — Roles and responsibilities  · MANUAL

**Manual assessment required.** Accountability for information security must rest with the Board; undefined ownership leaves gaps no control can close. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Document information security roles in board charters and a RACI; assign senior ownership of the security function.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Information security capability

#### 📋 CPS 234 ¶15 — Information security capability  · MANUAL

**Manual assessment required.** Capability must scale with threats; AWS-native detective services evidence the technology component but not people/process. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Maintain a resourced security function; enable AWS detective services (see cps234-21-threat-detection) as the technology component.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Policy framework

#### 📋 CPS 234 ¶18 — Policy framework  · MANUAL

**Manual assessment required.** Policies define the control intent that technical configurations implement; absent policy, controls drift without a baseline. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Establish and maintain an information security policy suite covering the obligations in CPS 234.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Information asset identification and classification

#### 📋 CPS 234 ¶20 — Information asset identification and classification  · MANUAL

**Manual assessment required.** Controls must be commensurate with asset criticality; without classification, protection cannot be risk-prioritised. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Maintain an asset inventory and classification scheme; on AWS, support it with mandatory resource tagging, AWS Config inventory and Resource Groups.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Implementation of controls

#### ❌ CPS 234 ¶21 — Implementation of controls - access management  · FAIL

**Not compliant.** 4 issue(s) detected against this control. Excessive entitlements and long-lived credentials are the most common path to account compromise; least privilege limits blast radius. An over-privileged or leaked credential can read, alter or destroy all information assets. Priority remediation: Remove AdministratorAccess and *:* policies from users; use roles and short-lived credentials; remove unused/duplicate access keys; enable IAM Access Analyzer.

> **Evidence:**
> - IAM Access Analyzer in account 123456789012 is not enabled.
> - AWS policy AdministratorAccess is attached and allows '*:*' administrative privileges.
> - IAM User jay-cli has AdministratorAccess policy attached.
> - User jay-cli has long lived credentials with access to other services than IAM or STS.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - multi-factor authentication  · FAIL

**Not compliant.** 2 issue(s) detected against this control. MFA defeats credential theft, phishing and password reuse - the dominant initial-access techniques. Single-factor access means one stolen password yields full session access. Priority remediation: Enable MFA on the root user (hardware token) and enforce MFA for all IAM users with console access.

> **Evidence:**
> - Root account has a virtual MFA instead of a hardware MFA device enabled.
> - User jay-cli does not have any type of MFA enabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - password policy  · FAIL

**Not compliant.** 7 issue(s) detected against this control. Weak password policies enable brute-force and credential-stuffing attacks against IAM users. Short or reusable passwords are guessable, enabling unauthorised access and lateral movement. Priority remediation: Set an IAM account password policy: minimum length 14, require upper/lower/number/symbol, prevent reuse of last 24, expire within 90 days.

> **Evidence:**
> - Password expiration is not set.
> - IAM password policy does not require at least one lowercase letter.
> - IAM password policy does not require minimum length of 14 characters.
> - IAM password policy does not require at least one number.
> - IAM password policy reuse prevention is less than 24 or not set.
> - IAM password policy does not require at least one symbol.
> - IAM password policy does not require at least one uppercase letter.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ✅ CPS 234 ¶21 — Implementation of controls - encryption at rest  · PASS

**Compliant.** All 1 automated check(s) for this control passed. Encryption at rest protects confidentiality if storage media, snapshots or backups are exposed or exfiltrated.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - prevent public exposure  · FAIL

**Not compliant.** 1 issue(s) detected against this control. Accidental public exposure of storage is a leading cause of large-scale data breaches. A single public bucket or snapshot can disclose sensitive information assets to the internet. Priority remediation: Enable S3 Block Public Access at account and bucket level; enable EBS snapshot public-access block; remediate any public resources.

> **Evidence:**
> - Block Public Access is not configured for the account 123456789012.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - audit logging  · FAIL

**Not compliant.** 3 issue(s) detected against this control. Without complete, tamper-evident logs an entity cannot detect, investigate or evidence incidents. Missing or mutable logs blind incident response and break the audit trail required for investigation. Priority remediation: Enable multi-region CloudTrail with log-file validation and KMS encryption, deliver to CloudWatch Logs, enable Config recorder in all regions, VPC flow logs and S3 access logging.

> **Evidence:**
> - No CloudTrail trails enabled with logging were found.
> - AWS Config recorder 123456789012 is disabled.
> - S3 Bucket tf-state-123456789012-ap-southeast-2 has server access logging disabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - threat detection  · FAIL

**Not compliant.** 3 issue(s) detected against this control. Timely detection limits dwell time and the impact of incidents. Without detective controls, compromises persist undetected until material harm occurs. Priority remediation: Enable GuardDuty, Security Hub and Inspector v2 across all in-use regions and centralise findings.

> **Evidence:**
> - GuardDuty is not enabled.
> - Inspector2 is not enabled in this account.
> - Security Hub is not enabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - backup and availability  · FAIL

**Not compliant.** 1 issue(s) detected against this control. Recoverability protects the availability and integrity of information assets against ransomware, error and failure. Without tested backups, data loss from attack or failure may be unrecoverable. Priority remediation: Create AWS Backup plans and vaults; protect RDS, DynamoDB and EBS with backup plans; verify recovery.

> **Evidence:**
> - No Backup Vault exist.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### 📋 CPS 234 ¶22 — Implementation of controls - third-party control design  · MANUAL

**Manual assessment required.** Outsourced custody of information assets does not outsource the obligation to ensure they are protected. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Assess third-party control design via due diligence, SOC 2 / ISO 27001 reports, contractual security requirements and the AWS shared-responsibility model.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Incident management

#### ❌ CPS 234 ¶23 — Incident management - detection and alerting  · FAIL

**Not compliant.** 4 issue(s) detected against this control. Real-time alerting on high-risk events enables the timely detection CPS 234 requires. Without alerting, malicious activity is found only in retrospective log review, after impact. Priority remediation: Create CloudWatch metric filters and alarms for the listed security events on the CloudTrail log group.

> **Evidence:**
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### 📋 CPS 234 ¶24 — Incident management - response plans  · MANUAL

**Manual assessment required.** Detection without a tested response plan leaves the entity improvising during an incident. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Document response plans covering all incident stages and Board escalation; review and test at least annually (e.g. tabletop/game-day exercises).

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Testing control effectiveness

#### ❌ CPS 234 ¶27 — Testing control effectiveness  · FAIL

**Not compliant.** 1 issue(s) detected against this control. Controls degrade over time; continuous vulnerability identification evidences ongoing effectiveness testing. Untested controls and unscanned assets accumulate exploitable vulnerabilities. Priority remediation: Enable Inspector v2 and ensure EC2 instances are managed by SSM for full scan coverage; remediate findings.

> **Evidence:**
> - Inspector2 is not enabled in this account.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Internal audit

#### 📋 CPS 234 ¶32 — Internal audit  · MANUAL

**Manual assessment required.** Independent assurance validates that controls are both well-designed and operating as intended. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Include information security control effectiveness in the internal audit plan with appropriate scope, skills and independence; assess third-party assurance relied upon.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### APRA notification

#### 📋 CPS 234 ¶35 — APRA notification  · MANUAL

**Manual assessment required.** Prudential supervision depends on timely notification of material incidents and weaknesses. This obligation is not observable from AWS APIs and must be evidenced via documentation/process: Maintain a notification process with defined materiality thresholds and the 72-hour / 10-business-day timelines; AWS detective controls (cps234-23) support timely awareness.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

## Remediation roadmap
1. **¶21 Implementation of controls - access management** — Remove AdministratorAccess and *:* policies from users; use roles and short-lived credentials; remove unused/duplicate access keys; enable IAM Access Analyzer.
2. **¶21 Implementation of controls - multi-factor authentication** — Enable MFA on the root user (hardware token) and enforce MFA for all IAM users with console access.
3. **¶21 Implementation of controls - password policy** — Set an IAM account password policy: minimum length 14, require upper/lower/number/symbol, prevent reuse of last 24, expire within 90 days.
4. **¶21 Implementation of controls - prevent public exposure** — Enable S3 Block Public Access at account and bucket level; enable EBS snapshot public-access block; remediate any public resources.
5. **¶21 Implementation of controls - audit logging** — Enable multi-region CloudTrail with log-file validation and KMS encryption, deliver to CloudWatch Logs, enable Config recorder in all regions, VPC flow logs and S3 access logging.
6. **¶21 Implementation of controls - threat detection** — Enable GuardDuty, Security Hub and Inspector v2 across all in-use regions and centralise findings.
7. **¶21 Implementation of controls - backup and availability** — Create AWS Backup plans and vaults; protect RDS, DynamoDB and EBS with backup plans; verify recovery.
8. **¶23 Incident management - detection and alerting** — Create CloudWatch metric filters and alarms for the listed security events on the CloudTrail log group.
9. **¶27 Testing control effectiveness** — Enable Inspector v2 and ensure EC2 instances are managed by SSM for full scan coverage; remediate findings.

---
_Generated by apra-compliance-narrator. Automated controls reflect AWS Config / Prowler findings; manual controls require human assessment. Verify against the official APRA CPS 234 standard._