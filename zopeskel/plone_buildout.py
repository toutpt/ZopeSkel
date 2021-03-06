import copy

from zopeskel import abstract_buildout


class PloneBuildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/plone_buildout'
    summary = "A buildout for Plone developer installation"
    help = """
This template creates a Plone 4 buildout for development purposes.
It uses Zope in debug mode and sets a default password.
"""

    pre_run_msg = """
*** NOTE: This template is for developers.

If you just want to install Plone, the preferred way to get a buildout-based
setup for Plone is to use the standard installer for your operating system
(the Windows installer, the Mac installer, or the Unified Installer for
Linux/Unix/BSD). These give you a best-practice, widely-used setup with an
isolated Python and a well-documented buildout.
"""

    post_run_msg = """
Generation finished.

Now run bootstrap and buildout:

python bootstrap.by

bin/buildout

See ZopeSkel add-on page for more details:

http://plone.org/products/zopeskel

"""

    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(abstract_buildout.AbstractBuildout.vars)

    vars = vars[1:]

    vars.extend([abstract_buildout.VAR_PLONEVER, ])

    # Set default Plone 4 version
    vars[0].default = "4.1"

    def pre(self, command, output_dir, vars):

        # For easy mode (don't ask stupid questions)
        vars['expert_mode'] = 'easy'
        vars['eggifiedzope'] = True
        vars['zope2_install'] = True
        vars['zope2_version'] = "2.12.3"
        super(PloneBuildout, self).pre(command, output_dir, vars)
