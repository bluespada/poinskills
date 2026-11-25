---
name: {{FEATURE_NAME}}
description: {{one-line summary of what this PRD covers}}
status: draft
tasks: []
authored:
  - {{author}}
createdAt: {{YYYY-MM-DDTHH:MM:SSZ}}
updatedAt: {{YYYY-MM-DDTHH:MM:SSZ}}
---

# PRD: {{FEATURE_NAME}}

**Spec ID**: `{{NNN}}-{{feature-slug}}`
**Verification method**: Test | Inspection | Analysis (document default; per requirement where it differs)
**Change rule**: a change to any requirement here must propagate into the task files listed under `tasks`.

---

## 1. Executive Summary

{{One or two sentences: what this is and what it is for. No technology.}}

## 2. Problem Statement

### Current State

{{What exists today, or what is absent.}}

### Desired State

{{What should be true once this is delivered, in observable terms.}}

### Business Impact

{{Benefits: A, B, C. Risks if not delivered: X, Y, Z.}}

## 3. Functional Requirements

- **FR-001**: The system MUST {{specific capability}}.
  Priority: {{High}} | Status: {{Draft}} | Verification: {{Test}}
- **FR-002**: The system MUST {{specific capability}}.
  Priority: {{Medium}} | Status: {{Draft}} | Verification: {{Test}}

## 4. Non-Functional Requirements

- **NFR-001**: {{Measurable constraint with a target and a measurement window.}}

## 5. Service Level Objectives

Include only when this runs as a service.

- Availability: {{99.95% measured over a 30-day rolling window}}
- Latency: {{p95 duration under 100ms}}
- Error rate: {{under 0.1% of requests}}

## 6. Cost Constraints

Include only when the project spends money at runtime.

### Budget

{{One-time setup: amount. Recurring: amount with tolerance.}}

### Cost Optimization

{{Levers worth taking: scheduling, retention, tiering.}}

## 7. Compliance Requirements

Include only when a framework applies. Name each one.

- Frameworks: {{SOC 2 Type II, HIPAA, PCI-DSS, GDPR, internal standard}}
- Data residency: {{where data may live}}
- Retention: {{duration and deletion rule}}

## 8. Success Criteria

### Functional Validation

- [ ] {{Observable behavior that must hold}}

### Security Validation

- [ ] {{No high or critical findings in security scans, where applicable}}

### Performance Validation

- [ ] {{Load or latency target met, where applicable}}

### Operational Validation

- [ ] {{Monitoring, alerting, backup or recovery verified, where applicable}}

## 9. Assumptions

- {{Assumption that, if false, invalidates part of this PRD}}

## 10. Out of Scope

- {{Explicitly excluded item}}

## 11. Dependencies

- {{External system, team, or decision this depends on}}

## 12. Open Questions

- `[NEEDS CLARIFICATION: the specific question]`