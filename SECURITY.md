# Security Policy

## Reporting a Vulnerability

The Decision Assessment Assistant team and community take all security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

To report a security vulnerability, please email us at **hamad_almunif@icloud.com** with a detailed description of the issue, the steps to reproduce it, and any potential impact.

**Please do not report security vulnerabilities through public GitHub issues.**

## Security Measures

We are committed to ensuring the security of our platform. Here are some of the measures we take:

### Data Encryption
- **In Transit:** All data transmitted between you and our servers is encrypted using TLS 1.2 or higher.
- **At Rest:** All sensitive data stored on our servers is encrypted using AES-256.

### Authentication
- **API Keys:** All API requests must be authenticated with a valid API key.
- **JWT Tokens:** User authentication is handled via JSON Web Tokens (JWT) with a short expiration time.
- **OAuth 2.0:** We support OAuth 2.0 for third-party integrations.

### Infrastructure
- **HTTPS Enforcement:** All API and web traffic is forced to use HTTPS.
- **Regular Security Audits:** We conduct regular security audits of our infrastructure and code.
- **Dependency Scanning:** We use automated tools to scan our dependencies for known vulnerabilities.

### Best Practices for Developers
- **Keep your API keys secret:** Do not expose your API keys in client-side code or public repositories.
- **Use environment variables:** Store your API keys in environment variables on your server.
- **Rotate your keys regularly:** We recommend rotating your API keys every 90 days.
- **Use a secrets management service:** For production applications, use a service like AWS Secrets Manager or HashiCorp Vault.

## Scope

This security policy applies to the Decision Assessment Assistant API and its related services. If you believe you have found a vulnerability in any other part of our infrastructure, please let us know.

## Our Commitment

We are committed to working with the security community to resolve vulnerabilities and keep our users safe. We will:

- Acknowledge receipt of your vulnerability report within 48 hours.
- Provide you with an estimated timeline for addressing the vulnerability.
- Notify you when the vulnerability has been fixed.
- Publicly credit you for your contribution (if you wish).

Thank you for helping keep Decision Assessment Assistant secure! 🛡️
