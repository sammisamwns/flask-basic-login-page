# JWT vs OAuth
Understanding the difference between JWT (JSON Web Token) and OAuth (Open Authorization) is key to building secure authentication systems.

## What Is JWT?
JWT (JSON Web Token) is a compact, URL-safe way to represent claims between two parties.

It is a token format used for securely transmitting information as a JSON object.

## Usage:
✅ Stateless authentication
✅ Token-based APIs
✅ Identity verification

## What Is OAuth?
OAuth is a protocol that allows applications to access user data from another service without exposing user credentials.

It is often used for third-party logins like “Sign in with Google.”

OAuth Flow (Simplified):

App requests access.

User authenticates with provider (e.g., Google).

Provider returns an access_token.

App uses token to call provider’s APIs.

## Key Differences
| Feature                    | JWT                                  | OAuth                                  |
| -------------------------- | ------------------------------------ | -------------------------------------- |
| **Type**                   | Token format                         | Authorization protocol                 |
| **Use Case**               | Authentication                       | Authorization                          |
| **Protocol?**              | ❌ Not a protocol                     | ✅ Yes                                  |
| **Carries Identity Info?** | ✅ Yes (claims, subject, expiry)      | 🔁 Depends on implementation           |
| **Stateless?**             | ✅ Yes                                | 🔁 Can be stateful or stateless        |
| **Used With?**             | OAuth, OpenID, or standalone         | Often uses JWT or opaque tokens        |
| **Security Risk**          | Susceptible to replay/XSS if misused | Needs HTTPS and proper scopes handling |

## When to Use What?
| Scenario                                    | Preferred |
| ------------------------------------------- | --------- |
| Custom login system with backend API auth   | ✅ JWT     |
| Third-party app accessing user Google Drive | ✅ OAuth   |
| Microservices needing token-based access    | ✅ JWT     |
| Delegating permission (e.g., Spotify API)   | ✅ OAuth   |

## Security Tips
Always use HTTPS when transmitting tokens.

Use short-lived JWTs and rotate them with refresh tokens.

For OAuth, use PKCE in public clients (e.g., SPAs or mobile apps).

Avoid storing tokens in localStorage — prefer HttpOnly cookies.
