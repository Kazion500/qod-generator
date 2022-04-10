def create_email_template(quote):
    plain_text = 'Quote of the day: {}'.format(quote)
    html = """
    <html>
    <head></head>
    <body>
        <p>Hi There! 😁<br>
        <b>Quote of the day:</b> <br>
        {}
        </p>
    </body>
    </html>
    """.format(quote)
    return (html, plain_text,)
