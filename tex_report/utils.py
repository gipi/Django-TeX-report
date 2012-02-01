from django.template import loader, Context

from . import settings

import envoy


def compile_report(template, outdir, outfilename_scheme, **kwargs):
    """Creates a pdf using the given template.

    The temporary ``.tex`` files are stored where the ``TEX_REPORT_TMP_PATH``
    settings variable point to.
    """
    template = loader.get_template(template)
    c = Context(kwargs)
    tex = template.render(c)

    tex_outfilename = "%s/%s.tex" % (settings.TEX_REPORT_TMP_PATH, outfilename_scheme)

    with open(tex_outfilename, "w+") as f:
        f.write(tex)
        f.close()

    r = envoy.run("pdftex -output-directory %s %s" % (outdir, tex_outfilename))

    if r.status_code != 0:
        print "ERROR"
        print r.std_out
