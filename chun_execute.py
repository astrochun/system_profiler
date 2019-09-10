"""
chun_execute
====

Simple code to execute @fillipp system_profiler() and extract what I need.

Original code here:

https://github.com/filipp/system_profiler

"""

import system_profiler

from astropy.table import Table

def main(outfile):

    '''
    Provide explanation for function here.

    Parameters
    ----------
    outfile: str
     Output filename to write astropy ASCII table

    Returns
    -------

    Notes
    -----
    Created by Chun Ly, 9 September 2019
    '''

    # Get all applications in /Applications
    apps_dict = system_profiler.find('Applications', 'path', '/Applications')

    n_apps = len(apps_dict)

    name    = [''] * n_apps
    path    = [''] * n_apps
    version = [''] * n_apps
    moddate = [''] * n_apps
    
    for ii in range(n_apps):
        t_app       = apps_dict[ii]
        name[ii]    = t_app['_name']
        try:
            version[ii] = t_app['version']
        except KeyError:
            version[ii] = 'N/A'
        moddate[ii] = t_app['lastModified'].strftime('%m-%d-%y')
        path[ii]    = t_app['path']

    tab0 = Table([name, version, moddate, path],
                 names=('Name','version','ModifiedDate','path'))
    tab0.sort('Name')

    tab0.write(outfile, format='ascii.fixed_width_two_line', overwrite=True)
#enddef

