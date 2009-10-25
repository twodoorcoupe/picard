# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2007 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# Install gettext "noop" function in case const.py gets imported directly.
import __builtin__
__builtin__.__dict__['N_'] = lambda a: a

# Host for PUID submissions
PUID_SUBMIT_HOST = "musicbrainz.org"
PUID_SUBMIT_PORT = 80

# Submission limits
MAX_RATINGS_PER_REQUEST = 20

# Amazon associate and developer ids
AMAZON_STORE_ASSOCIATE_IDS = {
    u'amazon.ca': u'musicbrainz01-20',
    u'amazon.co.jp': u'musicbrainz-22',
    u'amazon.co.uk': u'musicbrainz0c-21',
    u'amazon.com': u'musicbrainz0d-20',
    u'amazon.de': u'musicbrainz00-21',
    u'amazon.fr': u'musicbrainz0e-21',
}

# MusicDNS client ID
MUSICDNS_KEY = "0736ac2cd889ef77f26f6b5e3fb8a09c"

# Release formats
RELEASE_FORMATS = {
    u'CD': N_('CD'),
    u'DVD': N_('DVD'),
    u'SACD': N_('SACD'),
    u'LaserDisc': N_('LaserDisc'),
    u'MiniDisc': N_('MiniDisc'),
    u'Vinyl': N_('Vinyl'),
    u'Cassette': N_('Cassette'),
    u'Cartridge': N_('Cartridge (4/8-tracks)'),
    u'ReelToReel': N_('Reel-to-Reel'),
    u'DAT': N_('DAT'),
    u'Digital': N_('Digital Media'),
    u'WaxCylinder': N_('Wax Cylinder'),
    u'PianoRoll': N_('Piano Roll'),
    u'DCC': N_('Digital Compact Cassette'),
    u'Other': N_('Other'),
}

# Release countries
RELEASE_COUNTRIES = {
    u'BD': N_('Bangladesh'),
    u'BE': N_('Belgium'),
    u'BF': N_('Burkina Faso'),
    u'BG': N_('Bulgaria'),
    u'BB': N_('Barbados'),
    u'WF': N_('Wallis and Futuna Islands'),
    u'BM': N_('Bermuda'),
    u'BN': N_('Brunei Darussalam'),
    u'BO': N_('Bolivia'),
    u'BH': N_('Bahrain'),
    u'BI': N_('Burundi'),
    u'BJ': N_('Benin'),
    u'BT': N_('Bhutan'),
    u'JM': N_('Jamaica'),
    u'BV': N_('Bouvet Island'),
    u'BW': N_('Botswana'),
    u'WS': N_('Samoa'),
    u'BR': N_('Brazil'),
    u'BS': N_('Bahamas'),
    u'BY': N_('Belarus'),
    u'BZ': N_('Belize'),
    u'RU': N_('Russian Federation'),
    u'RW': N_('Rwanda'),
    u'RE': N_('Reunion'),
    u'TM': N_('Turkmenistan'),
    u'TJ': N_('Tajikistan'),
    u'RO': N_('Romania'),
    u'TK': N_('Tokelau'),
    u'GW': N_('Guinea-Bissa'),
    u'GU': N_('Guam'),
    u'GT': N_('Guatemala'),
    u'GR': N_('Greece'),
    u'GQ': N_('Equatorial Guinea'),
    u'GP': N_('Guadeloupe'),
    u'JP': N_('Japan'),
    u'GY': N_('Guyana'),
    u'GF': N_('French Guiana'),
    u'GE': N_('Georgia'),
    u'GD': N_('Grenada'),
    u'GB': N_('United Kingdom'),
    u'GA': N_('Gabon'),
    u'SV': N_('El Salvador'),
    u'GN': N_('Guinea'),
    u'GM': N_('Gambia'),
    u'GL': N_('Greenland'),
    u'GI': N_('Gibraltar'),
    u'GH': N_('Ghana'),
    u'OM': N_('Oman'),
    u'TN': N_('Tunisia'),
    u'JO': N_('Jordan'),
    u'HT': N_('Haiti'),
    u'HU': N_('Hungary'),
    u'HK': N_('Hong Kong'),
    u'HN': N_('Honduras'),
    u'HM': N_('Heard and Mc Donald Islands'),
    u'VE': N_('Venezuela'),
    u'PR': N_('Puerto Rico'),
    u'PW': N_('Palau'),
    u'PT': N_('Portugal'),
    u'SJ': N_('Svalbard and Jan Mayen Islands'),
    u'PY': N_('Paraguay'),
    u'IQ': N_('Iraq'),
    u'PA': N_('Panama'),
    u'PF': N_('French Polynesia'),
    u'PG': N_('Papua New Guinea'),
    u'PE': N_('Peru'),
    u'PK': N_('Pakistan'),
    u'PH': N_('Philippines'),
    u'PN': N_('Pitcairn'),
    u'PL': N_('Poland'),
    u'PM': N_('St. Pierre and Miquelon'),
    u'ZM': N_('Zambia'),
    u'EH': N_('Western Sahara'),
    u'EE': N_('Estonia'),
    u'EG': N_('Egypt'),
    u'ZA': N_('South Africa'),
    u'EC': N_('Ecuador'),
    u'IT': N_('Italy'),
    u'VN': N_('Viet Nam'),
    u'SB': N_('Solomon Islands'),
    u'ET': N_('Ethiopia'),
    u'SO': N_('Somalia'),
    u'ZW': N_('Zimbabwe'),
    u'SA': N_('Saudi Arabia'),
    u'ES': N_('Spain'),
    u'ER': N_('Eritrea'),
    u'MD': N_('Moldova, Republic of'),
    u'MG': N_('Madagascar'),
    u'MA': N_('Morocco'),
    u'MC': N_('Monaco'),
    u'UZ': N_('Uzbekistan'),
    u'MM': N_('Myanmar'),
    u'ML': N_('Mali'),
    u'MO': N_('Macau'),
    u'MN': N_('Mongolia'),
    u'MH': N_('Marshall Islands'),
    u'MK': N_('Macedonia, The Former Yugoslav Republic of'),
    u'MU': N_('Mauritius'),
    u'MT': N_('Malta'),
    u'MW': N_('Malawi'),
    u'MV': N_('Maldives'),
    u'MQ': N_('Martinique'),
    u'MP': N_('Northern Mariana Islands'),
    u'MS': N_('Montserrat'),
    u'MR': N_('Mauritania'),
    u'UG': N_('Uganda'),
    u'MY': N_('Malaysia'),
    u'MX': N_('Mexico'),
    u'IL': N_('Israel'),
    u'FR': N_('France'),
    u'IO': N_('British Indian Ocean Territory'),
    u'SH': N_('St. Helena'),
    u'FI': N_('Finland'),
    u'FJ': N_('Fiji'),
    u'FK': N_('Falkland Islands (Malvinas)'),
    u'FM': N_('Micronesia, Federated States of'),
    u'FO': N_('Faroe Islands'),
    u'NI': N_('Nicaragua'),
    u'NL': N_('Netherlands'),
    u'NO': N_('Norway'),
    u'NA': N_('Namibia'),
    u'VU': N_('Vanuatu'),
    u'NC': N_('New Caledonia'),
    u'NE': N_('Niger'),
    u'NF': N_('Norfolk Island'),
    u'NG': N_('Nigeria'),
    u'NZ': N_('New Zealand'),
    u'ZR': N_('Zaire'),
    u'NP': N_('Nepal'),
    u'NR': N_('Nauru'),
    u'NU': N_('Niue'),
    u'CK': N_('Cook Islands'),
    u'CI': N_('Cote d\'Ivoire'),
    u'CH': N_('Switzerland'),
    u'CO': N_('Colombia'),
    u'CN': N_('China'),
    u'CM': N_('Cameroon'),
    u'CL': N_('Chile'),
    u'CC': N_('Cocos (Keeling) Islands'),
    u'CA': N_('Canada'),
    u'CG': N_('Congo'),
    u'CF': N_('Central African Republic'),
    u'CZ': N_('Czech Republic'),
    u'CY': N_('Cyprus'),
    u'CX': N_('Christmas Island'),
    u'CR': N_('Costa Rica'),
    u'CV': N_('Cape Verde'),
    u'CU': N_('Cuba'),
    u'SZ': N_('Swaziland'),
    u'SY': N_('Syrian Arab Republic'),
    u'KG': N_('Kyrgyzstan'),
    u'KE': N_('Kenya'),
    u'SR': N_('Suriname'),
    u'KI': N_('Kiribati'),
    u'KH': N_('Cambodia'),
    u'KN': N_('Saint Kitts and Nevis'),
    u'KM': N_('Comoros'),
    u'ST': N_('Sao Tome and Principe'),
    u'SI': N_('Slovenia'),
    u'KW': N_('Kuwait'),
    u'SN': N_('Senegal'),
    u'SM': N_('San Marino'),
    u'SL': N_('Sierra Leone'),
    u'SC': N_('Seychelles'),
    u'KZ': N_('Kazakhstan'),
    u'KY': N_('Cayman Islands'),
    u'SG': N_('Singapore'),
    u'SE': N_('Sweden'),
    u'SD': N_('Sudan'),
    u'DO': N_('Dominican Republic'),
    u'DM': N_('Dominica'),
    u'DJ': N_('Djibouti'),
    u'DK': N_('Denmark'),
    u'VG': N_('Virgin Islands (British)'),
    u'DE': N_('Germany'),
    u'YE': N_('Yemen'),
    u'DZ': N_('Algeria'),
    u'US': N_('United States'),
    u'UY': N_('Uruguay'),
    u'YT': N_('Mayotte'),
    u'UM': N_('United States Minor Outlying Islands'),
    u'LB': N_('Lebanon'),
    u'LC': N_('Saint Lucia'),
    u'LA': N_('Lao People\'s Democratic Republic'),
    u'TV': N_('Tuvalu'),
    u'TW': N_('Taiwan'),
    u'TT': N_('Trinidad and Tobago'),
    u'TR': N_('Turkey'),
    u'LK': N_('Sri Lanka'),
    u'LI': N_('Liechtenstein'),
    u'LV': N_('Latvia'),
    u'TO': N_('Tonga'),
    u'LT': N_('Lithuania'),
    u'LU': N_('Luxembourg'),
    u'LR': N_('Liberia'),
    u'LS': N_('Lesotho'),
    u'TH': N_('Thailand'),
    u'TF': N_('French Southern Territories'),
    u'TG': N_('Togo'),
    u'TD': N_('Chad'),
    u'TC': N_('Turks and Caicos Islands'),
    u'LY': N_('Libyan Arab Jamahiriya'),
    u'VA': N_('Vatican City State (Holy See)'),
    u'VC': N_('Saint Vincent and The Grenadines'),
    u'AE': N_('United Arab Emirates'),
    u'AD': N_('Andorra'),
    u'AG': N_('Antigua and Barbuda'),
    u'AF': N_('Afghanistan'),
    u'AI': N_('Anguilla'),
    u'VI': N_('Virgin Islands (U.S.)'),
    u'IS': N_('Iceland'),
    u'IR': N_('Iran (Islamic Republic of)'),
    u'AM': N_('Armenia'),
    u'AL': N_('Albania'),
    u'AO': N_('Angola'),
    u'AN': N_('Netherlands Antilles'),
    u'AQ': N_('Antarctica'),
    u'AS': N_('American Samoa'),
    u'AR': N_('Argentina'),
    u'AU': N_('Australia'),
    u'AT': N_('Austria'),
    u'AW': N_('Aruba'),
    u'IN': N_('India'),
    u'TZ': N_('Tanzania, United Republic of'),
    u'AZ': N_('Azerbaijan'),
    u'IE': N_('Ireland'),
    u'ID': N_('Indonesia'),
    u'UA': N_('Ukraine'),
    u'QA': N_('Qatar'),
    u'MZ': N_('Mozambique'),
    u'BA': N_('Bosnia and Herzegovina'),
    u'CD': N_('Congo, The Democratic Republic of the'),
    u'CS': N_('Serbia and Montenegro (historical, 2003-2006)'),
    u'RS': N_('Serbia'),
    u'ME': N_('Montenegro'),
    u'HR': N_('Croatia'),
    u'KP': N_('Korea (North), Democratic People\'s Republic of'),
    u'KR': N_('Korea (South), Republic of'),
    u'SK': N_('Slovakia'),
    u'SU': N_('Soviet Union (historical, 1922-1991)'),
    u'TL': N_('East Timor'),
    u'XC': N_('Czechoslovakia (historical, 1918-1992)'),
    u'XE': N_('Europe'),
    u'XG': N_('East Germany (historical, 1949-1990)'),
    u'XU': N_('[Unknown Country]'),
    u'XW': N_('[Worldwide]'),
    u'YU': N_('Yugoslavia (historical, 1918-1992)'),
}

# List of available user interface languages
UI_LANGUAGES = [
    (u'af', u'Afrikaans', N_(u'Afrikaans')),
    (u'ar', u'العربية', N_(u'Arabic')),
    (u'bg', u'Български', N_(u'Bulgarian')),
    (u'ca', u'Català', N_(u'Catalan')),
    (u'cs', u'Čeština', N_(u'Czech')),
    (u'cy', u'Cymraeg', N_(u'Welsh')),
    (u'da', u'Dansk', N_(u'Danish')),
    (u'de', u'Deutsch', N_(u'German')),
    (u'en', u'English', N_(u'English')),
    (u'en_CA', u'English (Canada)', N_(u'English (Canada)')),
    (u'en_GB', u'English (UK)', N_(u'English (UK)')),
    (u'es', u'Español', N_(u'Spanish')),
    (u'et', u'Eesti keel', N_(u'Estonian')),
    (u'fa', u'فارسی', N_(u'Persian')),
    (u'fi', u'Suomi', N_(u'Finnish')),
    (u'fr', u'Français', N_(u'French')),
    (u'fy', u'Frysk', N_(u'Frisian')),
    (u'gl', u'Galego', N_(u'Galician')),
    (u'he', u'עברית', N_(u'Hebrew')),
    (u'hi', u'हिन्दी', N_(u'Hindi')),
    (u'hu', u'Magyar', N_(u'Hungarian')),
    (u'is', u'Íslenska', N_(u'Islandic')),
    (u'it', u'Italiano', N_(u'Italian')),
    (u'kn', u'ಕನ್ನಡ ', N_(u'Kannada')),
    (u'ko', u'한국어', N_(u'Korean')),
    (u'lt', u'Lietuvių', N_(u'Lithuanian')),
    (u'nb', u'Norsk bokmål', N_(u'Norwegian Bokmal')),
    (u'nl', u'Nederlands', N_(u'Dutch')),
    (u'pl', u'Polski', N_(u'Polish')),
    (u'pt', u'Português', N_(u'Portuguese')),
    (u'pt_BR', u'Português do Brasil', N_(u'Brazilian Portuguese')),
    (u'ro', u'Română', N_(u'Romanian')),
    (u'ru', u'Pyccĸий', N_(u'Russian')),
    (u'sco', u'Scots leid', N_(u'Scots')),
    (u'sk', u'Slovenčina', N_(u'Slovak')),
    (u'sl', u'Slovenščina', N_(u'Slovenian')),
    (u'sr', u'Србин', N_(u'Serbian')),
    (u'sv', u'Svenska', N_(u'Swedish')),
    (u'tr', u'Türkçe', N_(u'Turkish')),
    (u'zh_CN', u'中文', N_(u'Chinese')),
]
