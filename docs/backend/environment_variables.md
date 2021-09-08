# environment variables

Currently, the backend expects the following environment variables to be present
at all times. If even one of ones listed below will not be available during the
start of the application then flask will fail.

This list should be updated regularly but in case it wasn't try checking
out the code in `backend/config.py`. All env vars should be defined there 
and nowhere else in code. They do NOT have default values!
See `.envrc.example` for real config details.

- `STRIP_STAGE_PATH` - used only on lambdas, needed for our AWS Gateway use case.

- `FLASK_ENV` - set to `development`, `staging` or `production`. Determines
the config used when booting the app.

- `SECRET_KEY` - used for sessions, see https://stackoverflow.com/a/22463969. 
  Must be set to random value.
  
- `BASE_URL` - used for reverse URLs and routing. Must be set to domain name
  of the application or `localhost`.
  
- `DB_HOST` - DNS name or IP address of the database.
- `DB_PORT` - port number for the database.
- `DB_NAME` - name of the database with tables created for the application.
- `DB_USER` - name of the user which app should use for database authentication.
- `DB_PASSWORD` - password for database authentication.
  
- `MAIL_SUPPRESS_SEND` - block or allow mail sending. Set to `TRUE` or `FALSE`.
- `MAIL_USERNAME` - username used for SMTP login.
- `MAIL_PASSWORD` - password used for SMTP login.
- `MAIL_SERVER` - DNS name or IP address of SMTP host which should receive mail.
- `MAIL_PORT` - port for SMTP server receiving connection.


### Few notes on `MAIL_*` variables

You have to define them (meaning `os.environ['MAIL_SERVER']` won't throw 
`KeyError`), but you can set them to be empty strings.

`MAIL_SUPPRESS_SEND` can be useful if you want to disable mail sending entirely.
A good example for it would be CI pipeline or local tests where you always want 
to stop the outgoing mail. It's also useful to quickly change this variable's
value to FALSE on production if for some reason you want to stop sending
emails without breaking the flow or sending HTTP errors to the clients.

The configuration flow is as follows:

1. If `MAIL_SUPPRESS_SEND` is `TRUE` - end here. No mail will be sent.
2. Else check if `MAIL_USERNAME` and `MAIL_PASSWORD` are non-empty
3. If yes then use whatever is in `MAIL_*`.
4. Else try fetching temporary credentials from ethereal.
5. If that works - use em
6. Else inform the user that we failed to find credentials and block mail.
