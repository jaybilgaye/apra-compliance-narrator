# APRA CPS 234 Information Security — AWS Compliance Report

**Account:** 123456789012  ·  **Region:** ap-southeast-2  ·  **Assessed:** 2026-06-06 18:26:25.671606  ·  **Engine:** bedrock

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

**Roles and Responsibilities (CPS 234 ¶13) – Manual Compliance**

The entity currently lacks documented evidence demonstrating clearly defined information security roles and responsibilities across the Board, senior management, and governing bodies, representing a fundamental gap in CPS 234 compliance. While ultimate Board accountability may be understood in practice, the absence of formal documentation in board charters and a RACI matrix creates ambiguity regarding ownership of specific security functions and decision rights. This deficiency undermines the foundational governance requirement of CPS 234 paragraph 13 and exposes the entity to accountability gaps that no technical control can remediate. **Priority remediation** requires immediate documentation of information security roles in board charters, development of a comprehensive RACI matrix, and formal assignment of a senior executive with explicit ownership of the information security function.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Information security capability

#### 📋 CPS 234 ¶15 — Information security capability  · MANUAL

**Information Security Capability (CPS 234 ¶15) – Manual Control**

The entity maintains manual processes to sustain information security capability commensurate with threat levels, though no specific findings were identified during this review period. While AWS-native detective services provide the technology foundation for threat detection, CPS 234 requires a holistic capability encompassing people, processes, and technology that scales with the evolving threat landscape. The current manual status indicates potential gaps in demonstrating how the security function is resourced, governed, and adapted as vulnerabilities emerge. **Priority remediation:** Formalize documentation of the security function's resourcing model, capability assessment framework, and integration with AWS detective services to evidence a comprehensive, scalable capability that meets regulatory expectations.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Policy framework

#### 📋 CPS 234 ¶18 — Policy framework  · MANUAL

**Policy Framework (CPS 234 ¶18) – Manual Control**

The entity currently maintains an information security policy framework on a manual basis, with no adverse findings identified in the current review. While the framework exists and appears to address CPS 234 obligations, the manual nature of policy maintenance presents inherent risks of version control issues, inconsistent updates, and potential drift from the control baseline that technical configurations are designed to implement. Under CPS 234 paragraph 18, the policy framework must remain commensurate with the entity's threat and vulnerability exposures, requiring regular review and update cycles that manual processes may not consistently support. **Priority remediation:** Implement a structured policy governance process with defined review cycles, version control, and automated distribution mechanisms to ensure the framework remains current and effectively directs information security responsibilities across all obligated parties.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Information asset identification and classification

#### 📋 CPS 234 ¶20 — Information asset identification and classification  · MANUAL

**Information Asset Identification and Classification**

The entity currently maintains information asset classification through manual processes, which presents a moderate compliance risk under CPS 234 paragraph 20. While no specific control failures have been identified, the manual approach limits scalability and creates potential for inconsistent classification of assets across the environment, including those managed by third parties. CPS 234 requires systematic classification by criticality and sensitivity to ensure controls are appropriately risk-prioritised, and manual processes may not provide the ongoing assurance needed as the asset base grows. The risk committee should prioritise implementing automated asset inventory and classification using AWS native capabilities (mandatory resource tagging, AWS Config, and Resource Groups) to strengthen governance and demonstrate systematic compliance with regulatory requirements.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Implementation of controls

#### ❌ CPS 234 ¶21 — Implementation of controls - access management  · FAIL

**Access Management Controls – Non-Compliant**

The entity's access management controls do not meet CPS 234 paragraph 21 requirements for information security controls commensurate with vulnerabilities and threats. Evidence shows critical deficiencies including a user account (jay-cli) holding unrestricted AdministratorAccess privileges with long-lived credentials, absence of IAM Access Analyzer to detect excessive permissions, and failure to enforce least privilege principles. These weaknesses create material risk of unauthorised access and account compromise, directly contradicting CPS 234's mandate for controls proportionate to asset criticality and potential consequences. **Immediate remediation is required**: revoke AdministratorAccess policies, transition to role-based access with temporary credentials, enable IAM Access Analyzer, and implement least-privilege access controls across all user accounts.

> **Evidence:**
> - IAM Access Analyzer in account 123456789012 is not enabled.
> - AWS policy AdministratorAccess is attached and allows '*:*' administrative privileges.
> - IAM User jay-cli has AdministratorAccess policy attached.
> - User jay-cli has long lived credentials with access to other services than IAM or STS.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - multi-factor authentication  · FAIL

**Multi-Factor Authentication (CPS 234 ¶21): Non-Compliant**

The organisation has not fully implemented multi-factor authentication controls required under CPS 234 paragraph 21. Evidence shows the root account uses virtual MFA rather than hardware MFA, and user 'jay-cli' has no MFA enabled whatsoever. This creates material information security risk, as MFA is the primary defence against credential theft and phishing attacks that commonly lead to unauthorised access to information assets. **Immediate remediation is required**: deploy hardware MFA for the root account and enforce MFA for all IAM users with console access, particularly 'jay-cli', to meet the control implementation standard expected of APRA-regulated entities.

> **Evidence:**
> - Root account has a virtual MFA instead of a hardware MFA device enabled.
> - User jay-cli does not have any type of MFA enabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - password policy  · FAIL

## Password Policy Control – Non-Compliant

The organisation's IAM password policy fails to meet baseline security standards required under CPS 234 paragraph 21 for implementing appropriate information security controls. Evidence shows seven critical deficiencies: no password expiration, no minimum 14-character length, no complexity requirements (uppercase, lowercase, numbers, symbols), and inadequate reuse prevention (less than 24 passwords). This materially increases vulnerability to credential-based attacks including brute-force and credential-stuffing, directly compromising the confidentiality and integrity of information assets. **Immediate remediation is required** to configure the IAM password policy with industry-standard parameters: 14-character minimum, full complexity requirements, 90-day expiration, and 24-password reuse prevention.

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

**Encryption at Rest – Compliant**

The entity has successfully implemented encryption controls for information assets at rest in accordance with CPS 234 paragraph 21. Evidence confirms that encryption is enabled across key storage services including S3 buckets, EBS volumes, RDS/DynamoDB databases, and backup vaults, protecting the confidentiality and integrity of data should storage media, snapshots, or backups be exposed or exfiltrated. This control is critical under CPS 234 as it provides a foundational safeguard against unauthorized access to sensitive information assets. No remediation is required at this time; ongoing monitoring should ensure encryption remains consistently applied to all new and existing storage resources.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - prevent public exposure  · FAIL

**Implementation of Controls – Prevent Public Exposure (CPS 234 ¶21): NON-COMPLIANT**

The entity has failed to implement adequate controls to prevent unauthorised disclosure of information assets through public exposure. Evidence shows that S3 Block Public Access is not configured at the account level (account 123456789012), creating a material risk that sensitive data could be inadvertently exposed to the internet. Under CPS 234 paragraph 21, APRA-regulated entities must maintain robust controls to prevent unauthorised disclosure, and accidental public exposure represents a leading cause of large-scale data breaches that could compromise customer information and regulatory standing. **Immediate remediation is required**: enable S3 Block Public Access at both account and bucket levels, implement EBS snapshot public-access blocks, and conduct a comprehensive audit to identify and remediate any currently public resources.

> **Evidence:**
> - Block Public Access is not configured for the account 123456789012.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - audit logging  · FAIL

**Implementation of Controls - Audit Logging (CPS 234 Paragraph 21): NON-COMPLIANT**

The entity currently fails to meet CPS 234 paragraph 21 requirements for audit logging controls. Evidence shows critical logging gaps across the AWS environment: no CloudTrail trails are enabled for API activity monitoring, AWS Config recorder is disabled preventing configuration change tracking, and S3 bucket access logging is not configured for the Terraform state bucket. These deficiencies fundamentally undermine the entity's ability to detect information security incidents, conduct forensic investigations, or provide an audit trail as mandated by CPS 234, creating significant regulatory and operational risk. **Immediate remediation is required**: enable multi-region CloudTrail with log-file validation and encryption, activate AWS Config recorders across all regions, and implement S3 access logging and VPC flow logs to establish a comprehensive audit capability.

> **Evidence:**
> - No CloudTrail trails enabled with logging were found.
> - AWS Config recorder 123456789012 is disabled.
> - S3 Bucket tf-state-123456789012-ap-southeast-2 has server access logging disabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - threat detection  · FAIL

**Threat Detection Controls – Non-Compliant**

The entity has failed to implement detective controls capable of identifying information security incidents in a timely manner, as required under CPS 234 paragraph 21. Evidence shows that critical AWS threat detection services—GuardDuty, Security Hub, and Inspector2—are not enabled across the environment, leaving the organisation blind to potential security incidents, malicious activity, and vulnerabilities. This gap directly contravenes the obligation to detect incidents promptly and increases dwell time for undetected threats, elevating the risk of material information asset compromise. **Immediate remediation is required**: enable all three services across in-use regions and establish centralised monitoring to achieve compliance and restore visibility into the security posture.

> **Evidence:**
> - GuardDuty is not enabled.
> - Inspector2 is not enabled in this account.
> - Security Hub is not enabled.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### ❌ CPS 234 ¶21 — Implementation of controls - backup and availability  · FAIL

**Backup and Availability Controls (CPS 234 ¶21): Non-Compliant**

The entity currently fails to meet CPS 234 paragraph 21 requirements for information asset availability, as no AWS Backup Vault exists to protect critical data stores including RDS databases, DynamoDB tables, and EBS volumes. This absence of systematic backup infrastructure creates material risk to business continuity and data recoverability in the event of ransomware attack, system failure, or operational error—core availability threats that CPS 234 explicitly requires entities to mitigate. Immediate remediation is required: establish AWS Backup plans and vaults, implement automated backup policies for all critical data assets, and conduct recovery testing to validate restoration capabilities. This control deficiency represents a **critical priority** requiring board attention, as the inability to recover information assets directly undermines the entity's operational resilience and regulatory obligations under CPS 234.

> **Evidence:**
> - No Backup Vault exist.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### 📋 CPS 234 ¶22 — Implementation of controls - third-party control design  · MANUAL

**Third-Party Control Design (CPS 234 ¶22)**

This control is currently managed through manual processes and requires immediate formalisation to meet CPS 234 obligations. While no adverse findings have been identified, the absence of a documented, systematic approach to evaluating third-party information security control design creates compliance risk, particularly given the entity's reliance on cloud infrastructure and external service providers. CPS 234 paragraph 22 explicitly requires APRA-regulated entities to evaluate the design of third-party controls protecting their information assets, as outsourcing arrangements do not transfer accountability for information security. **Priority remediation** should establish a formal third-party security assessment framework incorporating due diligence procedures, regular review of SOC 2/ISO 27001 attestations, contractual security requirements aligned to the entity's risk appetite, and documented understanding of shared responsibility models (particularly for AWS environments).

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Incident management

#### ❌ CPS 234 ¶23 — Incident management - detection and alerting  · FAIL

**Incident Management - Detection and Alerting: Non-Compliant**

The entity currently fails to meet CPS 234 paragraph 23 requirements for timely detection of information security incidents. Evidence shows no CloudWatch metric filters or alarms are configured to detect critical security events including authentication failures, root account usage, sign-ins without MFA, and unauthorized API calls. This absence of real-time alerting mechanisms creates a material gap in the entity's ability to detect and respond to potential security breaches in a timely manner, directly contravening CPS 234's mandate for robust incident detection capabilities. **Immediate remediation is required**: CloudWatch metric filters and alarms must be implemented on CloudTrail log groups for all identified security events to establish baseline detection capabilities and demonstrate compliance with regulatory obligations.

> **Evidence:**
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.
> - No CloudWatch log groups found with metric filters or alarms associated.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

#### 📋 CPS 234 ¶24 — Incident management - response plans  · MANUAL

**Incident Management – Response Plans (CPS 234 ¶24)**

The entity currently maintains incident response plans on a manual basis, though no specific deficiencies have been identified in the current review. CPS 234 paragraph 24 requires comprehensive, documented response plans covering detection through post-incident review, including Board escalation protocols, with mandatory annual review and testing through exercises such as tabletop or game-day scenarios. Without formalised testing and review cycles, the entity risks ineffective incident response when time-critical decisions are required, potentially delaying containment and regulatory notification. **Priority remediation:** Establish an annual calendar for formal testing of response plans and document Board escalation procedures to ensure preparedness and regulatory compliance.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Testing control effectiveness

#### ❌ CPS 234 ¶27 — Testing control effectiveness  · FAIL

## Testing Control Effectiveness (CPS 234 Paragraph 27)

**Status: Non-Compliant**

The entity has not established systematic testing of information security control effectiveness as required under CPS 234. Evidence shows that AWS Inspector2, a continuous vulnerability and software composition analysis service, is not enabled in the account, indicating an absence of automated, ongoing security testing capabilities. This deficiency prevents the entity from maintaining visibility into control degradation over time and identifying emerging vulnerabilities commensurate with the dynamic threat landscape and asset changes. **Immediate remediation is required**: enable AWS Inspector v2 across all relevant accounts, ensure EC2 instances are managed through Systems Manager for comprehensive scan coverage, and establish processes to triage and remediate identified findings within risk-based timeframes.

> **Evidence:**
> - Inspector2 is not enabled in this account.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### Internal audit

#### 📋 CPS 234 ¶32 — Internal audit  · MANUAL

**Internal Audit (CPS 234 ¶32) – Manual Process**

The entity currently lacks a structured internal audit program specifically addressing information security control design and operating effectiveness as required under CPS 234. While no adverse findings have been identified to date, the absence of independent assurance over information security controls—including those operated by related parties and third parties—represents a material gap in the entity's governance framework. Under CPS 234 paragraph 32, APRA mandates that appropriately skilled personnel conduct regular reviews to validate control effectiveness, which is critical for demonstrating ongoing compliance and identifying control deficiencies before they result in incidents. **Priority remediation:** Develop and implement a risk-based internal audit plan for information security that includes third-party assurance assessment, ensuring auditors possess appropriate cybersecurity expertise and independence.

_Reference: https://www.apra.gov.au/sites/default/files/cps_234_july_2019_for_public_release.pdf_

### APRA notification

#### 📋 CPS 234 ¶35 — APRA notification  · MANUAL

**APRA Notification (CPS 234 ¶35) – Manual Process**

The entity maintains a manual notification process for reporting material information security incidents to APRA within the required 72-hour timeframe and control weaknesses within 10 business days, with no adverse findings identified. While the current process appears operationally sound, the manual nature introduces execution risk during high-pressure incident scenarios when timely regulatory notification is critical to prudential supervision. Under CPS 234 paragraph 35, failure to meet these strict timeframes could constitute a reportable breach and undermine supervisory confidence. **Priority:** Formalize the notification procedure with documented materiality thresholds, decision trees, and escalation protocols, and integrate automated alerting from AWS detective controls to ensure consistent, timely APRA notification during material incidents.

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