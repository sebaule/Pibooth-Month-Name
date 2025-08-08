# Pibooth-Month-Name
===========
Pibooth plugin to have in the footer 2 the  date of the day (ie: August 8 2025 or 8 Août 2025)
The default options of pibooth are only numbers (ie: 8 8 2025)
This plugin replace the month number by the month letters
more beautiful no ? 

You just have to restart pibooth every day in order to have the date up-to-date.

Installation
-------------

You have to copy the file `pibooth_month_name.py` in the directory of your plugins.

Configuration
-------------

In your configuration file `.config/pibooth/pibooth.cfg` you have to configure all parameters below : 

Declaration of this plugin : 

    [GENERAL]
        
    # Path to custom plugin(s) not installed with pip (list of quoted paths accepted)
    plugins = /<Full Path>/pibooth_month_name.py
note:: Edit the configuration by running the command ``pibooth --config`` or editing the `.config/pibooth/pibooth.cfg` file.

or 

    [GENERAL]
        
    # Path to custom plugin(s) not installed with pip (list of quoted paths accepted)
    plugins = ('/<Full Path>/pibooth_ftp.py', '/<Full Path>/pibooth_month_name.py')
note:: Edit the configuration by running the command ``pibooth --config`` or editing the `.config/pibooth/pibooth.cfg` file.

Here the new configuration options available in the `pibooth` configuration.
**The keys and their default values are automatically added to your configuration after first** `pibooth`_ **restart.**

    
    [PLUGIN_MONTH_NAME]
    
    # Liste des mois séparés par des virgules, en anglais ou dans la langue que tu souhaites
    #months = janvier,février,mars,avril,mai,juin,juillet,août,septembre,octobre,novembre,décembre
    months = january,february,march,april,may,june,july,august,september,october,november,december
    
    # Format de date à appliquer dans footer_text2 ; variables disponibles : {day}, {month}, {year}
    #date_format_footer_text2 = {day} {month} {year}
    date_format_footer_text2 = {month} {day} {year}
note:: Edit the configuration by running the command ``pibooth --config`` or editing the `.config/pibooth/pibooth.cfg` file.


important, the default parameter have to be empty :

    [PICTURE]
    
    # Secondary text displayed
    #footer_text2 = "{date.day} {date.month} {date.year}"
    footer_text2 =
note:: Edit the configuration by running the command ``pibooth --config`` or editing the `.config/pibooth/pibooth.cfg` file.



