from setuptools import setup, find_packages
import sys


paste_deploy = "PasteDeploy"
if sys.version_info[1] < 5:
    paste_deploy += "<1.5.0"


version = '4.0.dev'

tests_require = ['zope.testing', 'zc.buildout', 'Cheetah', 'PasteScript']

setup(
    name='ZopeSkel',
    version=version,
    description="Templates and code generator for quickstarting Plone.",
    long_description=open('README.txt').read() + "\n" +
                     open('HISTORY.txt').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    license='MIT',
    keywords='web zope command-line skeleton project',
    author='Daniel Nouri',
    author_email='daniel.nouri@gmail.com',
    maintainer='Cris Ewing',
    maintainer_email="cris@crisewing.com",
    url='http://svn.plone.org/svn/collective/ZopeSkel/trunk',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        paste_deploy,
        "PasteScript>=1.7.2",
        "Cheetah>1.0,<=2.2.1",
    ],
    tests_require=tests_require,
    extras_require=dict(
        test=tests_require
    ),
    test_suite='zopeskel.tests.test_all.test_suite',
    entry_points="""
    [paste.paster_create_template]
    basic_namespace = zopeskel.basic_namespace:BasicNamespace
    nested_namespace = zopeskel.nested_namespace:NestedNamespace
    basic_zope = zopeskel.basic_zope:BasicZope
    plone = zopeskel.plone:Plone
    plone_app = zopeskel.plone_app:PloneApp
    plone_buildout = zopeskel.plone_buildout:PloneBuildout
    plone_portlet = zopeskel.plone_portlet:PlonePortlet
    plone_hosting = zopeskel.hosting:StandardHosting
    recipe = zopeskel.recipe:Recipe
    plone_pas = zopeskel.plone_pas:PlonePas

    [paste.paster_command]
    addcontent = zopeskel.localcommands:ZopeSkelLocalCommand

    [zopeskel.zopeskel_sub_template]
    portlet = zopeskel.localcommands.plone:Portlet
    view = zopeskel.localcommands.plone:View
    zcmlmeta = zopeskel.localcommands.plone:ZCMLMetaDirective
    i18nlocale = zopeskel.localcommands.plone:I18nLocale

    form = zopeskel.localcommands.plone:Form
    formfield = zopeskel.localcommands.plone:FormField
    browserlayer = zopeskel.localcommands.plone:BrowserLayer

    extraction_plugin = zopeskel.localcommands.plone_pas:ExtractionPlugin
    authentication_plugin = zopeskel.localcommands.plone_pas:AuthenticationPlugin
    challenge_plugin = zopeskel.localcommands.plone_pas:ChallengePlugin
    credentials_reset_plugin = zopeskel.localcommands.plone_pas:CredentialsResetPlugin
    user_adder_plugin = zopeskel.localcommands.plone_pas:UserAdderPlugin
    role_assigner_plugin = zopeskel.localcommands.plone_pas:RoleAssignerPlugin
    user_factory_plugin = zopeskel.localcommands.plone_pas:UserFactoryPlugin
    anonymous_user_factory_plugin = zopeskel.localcommands.plone_pas:AnonymousUserFactoryPlugin
    properties_plugin = zopeskel.localcommands.plone_pas:PropertiesPlugin
    groups_plugin = zopeskel.localcommands.plone_pas:GroupsPlugin
    roles_plugin = zopeskel.localcommands.plone_pas:RolesPlugin
    update_plugin = zopeskel.localcommands.plone_pas:UpdatePlugin
    validation_plugin = zopeskel.localcommands.plone_pas:ValidationPlugin
    user_enumeration_plugin = zopeskel.localcommands.plone_pas:UserEnumerationPlugin
    group_enumeration_plugin = zopeskel.localcommands.plone_pas:GroupEnumerationPlugin
    role_enumeration_plugin = zopeskel.localcommands.plone_pas:RoleEnumerationPlugin

    [console_scripts]
    zopeskel = zopeskel.zopeskel_script:run
    """,
)
