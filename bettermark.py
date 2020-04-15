#!/usr/bin/python

import os


def main():
    os.system("export-chrome-bookmarks ./temp.html")
    head = '''<script src="https://cdn.bootcss.com/jquery/3.5.0/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
        integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<link href="https://cdn.bootcss.com/flat-ui/2.3.0/css/flat-ui.min.css" rel="stylesheet" charset="utf-8">'''
    foot = ''' <script>
        $("h1").remove();
        $("h3").last().remove();
        $("h3").attr("align", "center");
        $("a").addClass("btn btn-block btn-lg btn-primary");
        $("dl>dl>dt>dl>dt>dl").addClass("container");
    </script> '''
    with open('./temp.html', 'r') as f:
        html = f.read()
    content = head + html + foot
    with open('./index.html', 'w') as f:
        f.write(content)
    os.remove('./temp.html')


if __name__ == '__main__':
    main()
