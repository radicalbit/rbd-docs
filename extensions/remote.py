import requests
import repos
from sphinx.directives import code


class RemoteCodeBlock(code.CodeBlock):
    has_content = False
    required_arguments = 3
    
    def run(self):
	url = repos.repositories[self.arguments[1]]+"/"+self.arguments[2]
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception("Failed to retrieve "+url)

        self.content = [r.text]

        return super(RemoteCodeBlock, self).run()


def setup(app):
    app.add_directive('remote-code-block', RemoteCodeBlock)
    return {'parallel_read_safe': True}

