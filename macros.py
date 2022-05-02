from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Macros',  # Application name
    'macros' : [       # List of button macros...
 # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'CD', ['Good afternoon,\nPlease see attached. Thank you.\n']),
        (0x000000, 'NBI Add', ['Good afternoon,\nPlease submit an addendum via NBI Intapp. ' \
                            + 'Please go to the Requests tab, then click the green button that says "create new request." ' \
                            + 'On the pop-up box that appears, choose "Addendum/Business Development" from the drop down. ' \
                            + 'Once completed, please submit for processing. Thank you.\n']),
        (0x000000, 'Add-P', ['Good afternoon,\nAddendum is with Conflicts Review Committee. Thank you.\n']),
         # 2nd row ----------
        (0x000000, 'Add-C1', ['Good afternoon,\nRelated party has been added to matter ###.\n']),
        (0x000000, 'Add-C2', ['Good afternoon,\nRelated parties have been added to matter ###.\n']),
        (0x000000, '25+ UP', ['*To expedite responses, individually requested Conflicts Desk searches do not include Ultimate Parent (UP) information. ' \
                            + 'Ultimate Parent searches are done at the matter approval stage and may affect the conflicts analysis. ' \
                            + 'Please contact the Conflicts Desk to request an Ultimate Parent search at the preliminary stage if needed.*\n']),
        # 3rd row ----------
        (0x000000, 'Inactive', ['This client is inactive. Please contact Master Changes to reactivate the client. ' \
                            + 'Once the client is reactivated, please reselect the client number from the Client Name/Number Lookup list. ' \
                            + 'The client should now appear as Active. ' \
                            + 'Please re-enter the information in the required fields of the profile section and submit to Conflicts for processing. Thank you.\n']),
        (0x000000, 'LAT', ['Sponsoring Attorney\n\n\n'
                            'Candidate\n\n\n'
                            'Current Employer\n\n\n'
                            'Other Client Relationships\n\n\n'
                            'Adverse Parties\n\n\n']),
       (0x000000, 'RP', ['Related party added on ']),
        # 4th row ----------
       (0x000000, 'UP', [' is its own ultimate parent. ']),
       # (0x000000, 'USA', [Keycode.COMMAND, 't', -Keycode.COMMAND, ']),
       # (0x000000, 'NBCSN', [Keycode.COMMAND, 't', -Keycode.COMMAND, ]),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
