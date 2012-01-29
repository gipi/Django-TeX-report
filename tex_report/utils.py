from django.template import loader, Context

import envoy


def compile_report(template, outdir, outfilename, **kwargs):
    template = loader.get_template(template)
    c = Context(kwargs)
    tex = template.render(c)

    tex_outfilename = "%s.tex" % outfilename

    with open(tex_outfilename, "w+") as f:
        f.write(tex)
        f.close()

    r = envoy.run("pdftex -output-directory %s %s" % (outdir, tex_outfilename))

    if r.status_code != 0:
        print "ERROR"
        print r.std_out
