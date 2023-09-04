# 0x01-Basic_authentication

---

* Learning Basic Auth, How to encode to base64 for username and password
* Using HTTPS wih headers for Authentication

---

## Tasks

### Mandatory

| Tasks | Description | Files |
| ----- | ----- | ----- |
| <ul><li> - [ ] Task 0 </li></ul> | 0. Simple-basic-API | N/A |
| <ul><li> - [ ] Task 1 </li></ul> | 1. Error handler: Unauthorized | [api/v1/app.py](api/v1/app.py), [api/v1/views/index.py](api/v1/views/index.py) |
| <ul><li> - [ ] Task 2 </li></ul> | 2. Error handler: Forbidden | [api/v1/app.py](api/v1/app.py), [api/v1/views/index.py](api/v1/views/index.py) |
| <ul><li> - [ ] Task 3 </li></ul> | 3. Auth class | [api/v1/auth](api/v1/auth), [api/v1/auth/__init__.py](api/v1/auth/__init__.py), [api/v1/auth/auth.py](api/v1/auth/auth.py) |
| <ul><li> - [ ] Task 4 </li></ul> | 4. Define which routes don't need authentication | [api/v1/auth/auth.py](api/v1/auth/auth.py) |
| <ul><li> - [ ] Task 5 </li></ul> | 5. Request validation! | [api/v1/app.py](api/v1/app.py), [api/v1/auth/auth.py](api/v1/auth/auth.py) |
| <ul><li> - [ ] Task 6 </li></ul> | 6. Basic auth | [api/v1/app.py](api/v1/app.py), [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 7 </li></ul> | 7. Basic - Base64 part | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 8 </li></ul> | 8. Basic - Base64 decode | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 9 </li></ul> | 9. Basic - User credentials | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 10 </li></ul> | 10. Basic - User object | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 11 </li></ul> | 11. Basic - Overload current_user - and BOOM! | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |

### Advanced

| Tasks | Description | Files |
| ----- | ----- | ----- |
| <ul><li> - [ ] Task 12 </li></ul> | 12. Basic - Allow password with ":" | [api/v1/auth/basic_auth.py](api/v1/auth/basic_auth.py) |
| <ul><li> - [ ] Task 13 </li></ul> | 13. Require auth with stars | [api/v1/auth/auth.py](api/v1/auth/auth.py) |

