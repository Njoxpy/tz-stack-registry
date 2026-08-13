# Interview Questions — Ekilie Cloud

## Technical Screening

### Junior

- Explain the difference between a goroutine and an OS thread. Why does Go's concurrency model matter for a service that handles many simultaneous deploys?
- In React, what's the difference between state and props, and when would a component re-render unnecessarily?

### Mid

- Walk through how you'd design a zero-downtime deploy for a Go service behind a load balancer. What has to happen in what order?
- In React Native, how do you handle a feature that behaves differently on iOS vs Android without duplicating your component logic?

### Senior

- You're given a Go service with a memory leak that only shows up under sustained load. How do you find it, and how do you prevent it from happening again?
- How would you evaluate whether a performance-critical piece of infrastructure (say, a build artifact processor) should be written in Go or in Zig? What's the actual trade-off, not just "Zig is faster"?

## Coding Challenge

### Junior

- **Prompt:** Implement a function that takes a list of GitHub webhook events (as JSON) and returns only the push events to the `main` branch, in the order received.
- **Constraints:** 45 minutes, Go or JavaScript, submit as a single file with a short README.
- **What they evaluate:** Correctness on edge cases (empty list, malformed JSON), readability, whether they handle errors instead of ignoring them.

### Mid

- **Prompt:** Build a minimal CI/CD webhook receiver in Go that accepts a GitHub push event, validates the signature, and triggers a mock "deploy" function idempotently (a retry of the same event shouldn't trigger a second deploy).
- **Constraints:** 2-hour take-home, Go required, must include tests.
- **What they evaluate:** Idempotency handling, signature validation correctness, test coverage, whether they think about retries and duplicate delivery.

### Senior

- **Prompt:** Design and implement a rolling deploy coordinator: given N instances of a service, roll out a new version with health checks between each instance, and automatically roll back on failure.
- **Constraints:** Take-home, up to 4 hours, Go, must run locally with a provided mock health-check server.
- **What they evaluate:** Failure-mode thinking (partial rollout failure, health check flakiness), state management, whether rollback logic is actually safe under concurrent triggers.

## System Design

### Mid

- **Prompt:** Design the deploy pipeline for a platform where a `git push` to a connected GitHub repo triggers a build and a zero-downtime release, for services written in any of Go, Node.js, Django, Rails, or Laravel.
- **Focus areas:** transactional integrity of the deploy state, idempotency of webhook-triggered builds, basic observability (how do you know a deploy failed and why).

### Senior

- **Prompt:** Design multi-tenant cloud infrastructure that gives users full root access to their own containers/VMs while maintaining isolation, fair resource allocation, and the ability to scale to thousands of concurrent student/indie-dev workloads with unpredictable traffic.
- **Focus areas:** tenant isolation and blast-radius containment, noisy-neighbor mitigation, cost-efficient scaling for low-revenue-per-user workloads, observability across tenants without violating isolation.

## Source of Questions

- <https://www.linkedin.com/company/ekilie/>
- <https://www.ekilie.cloud/>
