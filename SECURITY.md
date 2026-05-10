# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly through GitHub Security Advisories.

**Do not open a public issue for security vulnerabilities.**

### How to Report

1. Go to the [Security Advisories](../../security/advisories) page for this repository.
2. Click **"New draft security advisory"**.
3. Fill in the details of the vulnerability, including:
   - A description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- We will acknowledge receipt of your report within 48 hours.
- We will provide an initial assessment within 5 business days.
- We will work with you to understand and resolve the issue before any public disclosure.
- We will credit you in the advisory (unless you prefer to remain anonymous).

### Scope

This policy applies to the flame-detections repository and its detection rule content. For vulnerabilities in the FLAME Exchange taxonomy or infrastructure, please report to the [flame-fraud](https://github.com/elchacal801/flame-fraud) repository.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | Yes       |

## Security Best Practices

- Detection rules in this repository should never contain secrets, API keys, or credentials.
- Native queries should not include environment-specific connection strings or endpoints.
- Review all contributions for inadvertent disclosure of sensitive information.
