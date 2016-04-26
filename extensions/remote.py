import requests
import repos
from sphinx.directives import code
from sphinx.util import parselinenos
from docutils.parsers.rst import Directive, directives
class RemoteCodeBlock(code.CodeBlock):
    has_content = False
    required_arguments = 3
    optional_arguments = 0 
    option_spec = {
	'lines': directives.unchanged_required,
        'name':directives.unchanged_required,
        'caption':directives.unchanged_required
	}
    def run(self):

        document = self.state.document
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

	url = repos.repositories[self.arguments[1]]+"/"+self.arguments[2]

	session=requests.Session()
	session.headers.update({"Cache-Control": "no-cache, no-store, must-revalidate"})
        r = session.get(url)
        

	
	if r.status_code != 200:
            raise Exception("Failed to retrieve "+url)

        lines = r.text.split("\n")

	linespec = self.options.get('lines')
  		
        if linespec:
            try:
                linelist = parselinenos(linespec, len(lines))
            except ValueError as err:
                return [document.reporter.warning(str(err), line=self.lineno)]
	    lines = [lines[i] for i in linelist if i < len(lines)]
	    
            if not lines:
                return [document.reporter.warning(
                    'Line spec %r: no lines pulled from include file %r' %
                    (linespec, filename), line=self.lineno)]
	
	lines=self.custom_trim(lines)
	self.content=lines
        

        return super(RemoteCodeBlock, self).run()
    
    def custom_trim(self,lines):
	
	minwsnum=100
	for line in lines:
		wsnum=len(line) - len(line.lstrip()
		)
		if minwsnum>wsnum and len(line.lstrip())>0:
	        	minwsnum=wsnum
	lines=[line[minwsnum:] for line in lines]	
	
        return lines


def setup(app):
    app.add_directive('remote-code-block', RemoteCodeBlock)
    return {'parallel_read_safe': True}

