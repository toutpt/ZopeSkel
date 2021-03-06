"""
Local templates that are generically useful for every plone related project.
"""
from zopeskel.vars import var
from zopeskel.localcommands import ZopeSkelLocalTemplate


class PloneSubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    parent_templates = ['plone']

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(PloneSubTemplate, self).pre(command, output_dir, vars)
        dotted_name = [vars['namespace_package']]
        if 'namespace_package2' in vars and vars['namespace_package2']:
            dotted_name.append(vars['namespace_package2'])
        dotted_name.append(vars['package'])
        vars['dotted_name'] = ".".join(dotted_name)


class Portlet(PloneSubTemplate):
    """
    A plone 3 portlet skeleton
    """
    _template_dir = 'templates/plone/portlet'
    summary = "A Plone 3 portlet"

    vars = [
        var('portlet_name', 'Portlet name (human readable)',
            default="Example portlet"),
        var('portlet_type_name', 'Portlet type name (id)',
            default="ExamplePortlet"),
        var('description', 'Portlet description', default=""),
    ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(Portlet, self).pre(command, output_dir, vars)
        vars['portlet_filename'] = vars['portlet_type_name'].lower()
        vars['dotted_name'] = "%s.portlets" % vars['package_dotted_name']


class View(PloneSubTemplate):
    """
    A browser view skeleton
    """
    _template_dir = 'templates/plone/view'
    summary = "A browser view skeleton"

    vars = [
        var('view_name', 'Browser view name', default="Example"),
    ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(View, self).pre(command, output_dir, vars)
        vars['view_filename'] = vars['view_name'].lower().replace(' ', '')
        vars['view_classname'] = vars['view_name'].replace(' ', '')


class ZCMLMetaDirective(PloneSubTemplate):
    """
    A zcml meta directive skeleton
    """
    _template_dir = 'templates/plone/zcmlmeta'
    summary = "A ZCML meta directive skeleton"

    vars = [
        var('directive_name', 'The directive name', default="mydirective"),
        var('directive_namespace', 'The directive namespace',
            default="mynamespace"),
    ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(ZCMLMetaDirective, self).pre(command, output_dir, vars)
        vars['directive_class_name'] = vars['directive_name'].title()


class I18nLocale(PloneSubTemplate):
    """
    A skeleton for an i18n language
    """
    _template_dir = 'templates/plone/i18nlocales'
    summary = "An i18n locale directory structure"

    vars = [var('language_code', 'The iso-code of the language')]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(I18nLocale, self).pre(command, output_dir, vars)
        # There is no default for language_code, because that makes no sense
        # To accomodate testing, we introduce a default here.

        language_iso_code = vars['language_code'].lower().strip()
        iso = language_iso_code and language_iso_code or 'nl'
        vars['language_iso_code'] = iso


class Form(PloneSubTemplate):
    """
    A form skeleton
    """
    _template_dir = 'templates/plone/form'
    summary = "A form skeleton"

    vars = [
        var('form_name', 'Form class name', default="ExampleForm"),
        var('form_label', "Form Title", default='Example Form'),
        var('form_description', "Form Description", default=''),
        var('form_actions', 'Comma separated list of form actions',
            default="Submit"),
        var('form_invariants', 'Comma separated list of invariants',
            default=""),
    ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        splitCSV = lambda in_str: [x.strip() for x in in_str.split(",")]
        vars['form_filename'] = vars['form_name'].lower()
        vars['form_actions'] = splitCSV(vars['form_actions'])
        vars['form_invariants'] = splitCSV(vars['form_invariants'].strip())


class Z3cForm(PloneSubTemplate):
    """
    A zc3 form skeleton
    """
    _template_dir = 'templates/plone/form'
    summary = "A form skeleton"

    vars = [var('form_name', 'Form name', default="Example")]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(Z3cForm, self).pre(command, output_dir, vars)
        vars['form_filename'] = vars['form_name'].lower()


class FormField(PloneSubTemplate):
    """
    A template to add a form field to a form. Essentially this
    adds a field to Zope 3 schema.
    """
    _template_dir = 'templates/plone/formfield'
    summary = "Schema field for a form"

    _supported_fields = [
        ("Bool", "Field containin a truth value."),
        ("Text", "Field containing unicode text."),
        ("TextLine", "Field containing a single line of unicode text."),
        ("Datetime", "Field containing a DateTime."),
        ("Date", "Field containing a date."),
        ("Choice", "Obect from a source or vocabulary."),
        ("Password", "Field containing a unicode string without newlines.")
    ]
    _field_description = "\n".join(
        [" " * 25 + x[0].lower() + " : " + x[1] for x in _supported_fields]
    )

    vars = [
        var('form_filename',
            "Name of the file containing the form in browser.",
            default="exampleform"),
        var('field_name',
            "Name of the field (this should be a unique identifier).",
            default='examplefield'),
        var('field_type', "Type of field. Use one of the following \n\n %s\n" %
            _field_description,
            default='textline'),
        var('field_title', '', default='A short summary or label'),
        var('field_description',
            'A description of the field (to be displayed as a hint)',
            default=''),
        var('field_required',
            'Tells whether a field requires its value to exist (True/False)',
            default=False),
        var('field_readonly',
            "If true, the field's value cannot be changed (True/False)",
            default=False),
        var('field_default',
            'The field default value may be None or a legal field value',
            default='None'),
        var('field_missing_value',
            'If a field has no assigned value, set it to this value',
            default=''),
        var('field_constraint',
            'Specify the name of a function to use for validation',
            default=''),
    ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        super(FormField, self).pre(command, output_dir, vars)
        # XXX this should be handled by _map_boolean in base.py
        # but this template does not inherit from BaseTemplate
        for var in FormField.vars:
            if var.name in vars and (type(vars[var.name]) == str) and \
                    var.default in [True, False, None]:
                lowered = vars[var.name].lower().strip()
                if lowered in ['t', 'y', 'true']:
                    vars[var.name] = True
                elif lowered in ['f', 'n', 'false']:
                    vars[var.name] = False
                elif lowered == 'none':
                    vars[var.name] = None

        # make the field type case insensitive, if the field type
        # is not in the list of enumerated types
        # simple use the provided one
        vars['field_type'] = dict(
            [(x[0].lower(), x) for x in self._supported_fields]
        ).get(vars['field_type'].lower(), (vars['field_type'],))[0]


class BrowserLayer(PloneSubTemplate):
    """
    A browserlayer skeleton
    """
    _template_dir = 'templates/plone/browserlayer'
    summary = "A Plone browserlayer"


class Dexterity(PloneSubTemplate):
    """A dexterity template"""
    _template_dir = 'templates/plone/dexterity'
    summary = "A dexterity template"

    vars = [var('typeid', 'Content type ID', default="example"),
            var('type_schema', 'Type schema name', default="ExampleSchema"),
            var('type_title', 'Type title', default="Example"),
            var('type_desc', 'Type description', default="Description")]

    def pre(self, command, output_dir, vars):
        super(Dexterity, self).pre(command, output_dir, vars)
        vars['permission_id'] = "%s.Add%s" % (vars['dotted_name'],
                                               vars['typeid'].capitalize())
        vars['permission_title'] = "%s: Add %s" % (vars['dotted_name'],
                                                       vars['type_title'])
        vars['permission_var'] = "Add%s" % vars['typeid'].capitalize()
