# 0x02-Session_authentication

---

* Using Basic Authentication in Session Authentication with cookies

---

## Tasks

### Mandatory

| Tasks | Description | Files |
| ----- | ----- | ----- |
| <ul><li> - [ ] Task 0 </li></ul> | 0. Et moi et moi et moi! | [api/v1/app.py](api/v1/app.py), [api/v1/views/users.py](api/v1/views/users.py) |
| <ul><li> - [ ] Task 1 </li></ul> | 1. Empty session | [api/v1/auth/session_auth.py](api/v1/auth/session_auth.py), [api/v1/app.py](api/v1/app.py) |
| <ul><li> - [ ] Task 2 </li></ul> | 2. Create a session | [api/v1/auth/session_auth.py](api/v1/auth/session_auth.py) |
| <ul><li> - [ ] Task 3 </li></ul> | 3. User ID for Session ID |[api/v1/auth/session_auth.py](api/v1/auth/session_auth.py) |
| <ul><li> - [ ] Task 4 </li></ul> | 4. Session cookie | [api/v1/auth/auth.py](api/v1/auth/auth.py) |
| <ul><li> - [ ] Task 5 </li></ul> | 5. Before request | [api/v1/app.py](api/v1/app.py) |
| <ul><li> - [ ] Task 6 </li></ul> | 6. Use Session ID for identifying a User | [api/v1/auth/session_auth.py](api/v1/auth/session_auth.py) |
| <ul><li> - [ ] Task 7 </li></ul> | 7. New view for Session Authentication | [api/v1/views/session_auth.py](api/v1/views/session_auth.py), [api/v1/views/__init__.py](api/v1/views/__init__.py) |
| <ul><li> - [ ] Task 8 </li></ul> | 8. Logout | [api/v1/auth/session_auth.py](api/v1/auth/session_auth.py), [api/v1/views/session_auth.py](api/v1/views/session_auth.py) |

### Advanced

| Tasks | Description | Files |
| ----- | ----- | ----- |
| <ul><li> - [ ] Task 9 </li></ul> | 9. Expiration? | [api/v1/auth/session_exp_auth.py](api/v1/auth/session_exp_auth.py), [api/v1/app.py](api/v1/app.py) |
| <ul><li> - [ ] Task 10 </li></ul> | 10. Sessions in database | [api/v1/auth/session_db_auth.py](api/v1/auth/session_db_auth.py), [api/v1/app.py](api/v1/app.py), [models/user_session.py](models/user_session.py) |
