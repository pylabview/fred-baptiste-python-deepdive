from decimal import Decimal
from html import escape


def my_func():
    pass


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return f"{a}(<i>{hex(a)}</i>)"


def html_real(a):
    return f"{round(a, 2):.2f}"


def html_str(s):
    return html_escape(s).replace("\n", "<br/>\n")


def html_list(l):
    items = (f"<il>{htmlize(item)}</il>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def html_dic(d):
    items = (f"<il>{html_escape(k)}={htmlize(v)}<il/>" for k, v in d.items())
    return "<ul>/n" + "\n".join(items) + "\n</ul>"


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, dict):
        return html_dic(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    else:
        return html_escape(arg)


if __name__ == "__main__":
    print("Hello")
    print(
        html_str("""
                   this is
                   a multi line string
                   with special characters: 10 < 100
                  """)
    )
    print(html_int(255))
    print(htmlize(100))
    print(
        htmlize("""Python 
                  rocks!
                  """)
    )
    print(htmlize([1, 2, 3]))
    print(
        htmlize(
            [
                """Python
                   rocks! 0 < 1
                   """,
                (10, 20, 30),
                100,
            ]
        )
    )
