class HTMLstring:

    def __init__(self, head: str = "", body: str = ""):
        self.head = head
        self.body = body

    def __str__(self):
        string = f"""<html>
    <head>
        {self.head}
    </head>
    <body>
        {self.body}
    </body>
</html>"""
        return string

    def add_text(self, text: str, header: int = 0):
        if header != 0:
            text = f"<h{header}> {text} </h{header}>"
        else:
            text = f"<p> {text} </p>"
        text += "\n"
        self.body += text

    def add_image(self, filepath: str, alt: str, start=False, end=False):
        text = f'<img src="{filepath}" alt="{alt}">'
        if start:
            text = "<p> " + text
        if end:
            text = text + "<p>"
        self.body += text

    def save(self, filepath):
        file = open(filepath, 'w')
        file.write(str(self))
        file.close()
