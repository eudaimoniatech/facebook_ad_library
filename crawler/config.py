# enviroment-Variables:
# DBURL = "mongodb://localhost"
# TOKEN = "TOKEN1,TOKEN2,TOKEN3"
import os
# You can just create multiple apps to get multiple access tokens.
# Make sure to use long-life keys
TOKENS = os.getenv("TOKEN").split(",")
DBURL = os.getenv("DBURL")


KEYS_PER_THREAD = 7

URL = "https://graph.facebook.com/v15.0/ads_archive"
# All except for ad_snapshot_url
FIELDS = "id,ad_creation_time,ad_creative_bodies,ad_creative_link_captions,ad_creative_link_descriptions,ad_creative_link_titles,ad_delivery_start_time,ad_delivery_stop_time,bylines,currency,delivery_by_region,demographic_distribution,estimated_audience_size,impressions,languages,page_id,page_name,publisher_platforms,spend,target_locations,target_gender,target_ages,eu_total_reach,beneficiary_payers,age_country_gender_reach_breakdown"

# Lower to prevent returning of too much data which would result in an error.
# 5000 would be the maximum allowed.
LIMIT = 100

# Amount of Crawls a hourly quick crawler is stopped
# These are used to crawl the newly created Ads every hour
HOURLY_LIMIT = 500

# Hours after which the whole database should be crawled again
GLOBAL_RECRAWL = 48

# These are from the javascript of this site: https://www.facebook.com/ads/library/report/
COUNTRIES = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
    "AR": "Argentina",
    "AU": "Australia",
    "AT": "Austria",
    "BE": "Belgium",
    "BR": "Brazil",
    "CL": "Chile",
    "CN": "China",
    "CO": "Colombia",
    "HR": "Croatia",
    "DK": "Denmark",
    "DO": "Dominican Republic",
    "EG": "Egypt",
    "FI": "Finland",
    "FR": "France",
    "DE": "Germany",
    "GR": "Greece",
    "HK": "Hong Kong",
    "IN": "India",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IT": "Italy",
    "JP": "Japan",
    "JO": "Jordan",
    "KW": "Kuwait",
    "LB": "Lebanon",
    "MY": "Malaysia",
    "MX": "Mexico",
    "NL": "Netherlands",
    "NZ": "New Zealand",
    "NG": "Nigeria",
    "NO": "Norway",
    "PK": "Pakistan",
    "PA": "Panama",
    "PE": "Peru",
    "PH": "Philippines",
    "PL": "Poland",
    "RU": "Russia",
    "SA": "Saudi Arabia",
    "RS": "Serbia",
    "SG": "Singapore",
    "ZA": "South Africa",
    "KR": "South Korea",
    "ES": "Spain",
    "SE": "Sweden",
    "CH": "Switzerland",
    "TW": "Taiwan",
    "TH": "Thailand",
    "TR": "Turkey",
    "AE": "United Arab Emirates",
    "VE": "Venezuela",
    "PT": "Portugal",
    "LU": "Luxembourg",
    "BG": "Bulgaria",
    "CZ": "Czech Republic",
    "SI": "Slovenia",
    "IS": "Iceland",
    "SK": "Slovakia",
    "LT": "Lithuania",
    "TT": "Trinidad and Tobago",
    "BD": "Bangladesh",
    "LK": "Sri Lanka",
    "KE": "Kenya",
    "HU": "Hungary",
    "MA": "Morocco",
    "CY": "Cyprus",
    "JM": "Jamaica",
    "EC": "Ecuador",
    "RO": "Romania",
    "BO": "Bolivia",
    "GT": "Guatemala",
    "CR": "Costa Rica",
    "QA": "Qatar",
    "SV": "El Salvador",
    "HN": "Honduras",
    "NI": "Nicaragua",
    "PY": "Paraguay",
    "UY": "Uruguay",
    "PR": "Puerto Rico",
    "BA": "Bosnia and Herzegovina",
    "PS": "Palestine",
    "TN": "Tunisia",
    "BH": "Bahrain",
    "VN": "Vietnam",
    "GH": "Ghana",
    "MU": "Mauritius",
    "UA": "Ukraine",
    "MT": "Malta",
    "BS": "The Bahamas",
    "MV": "Maldives",
    "OM": "Oman",
    "MK": "Macedonia",
    "LV": "Latvia",
    "EE": "Estonia",
    "IQ": "Iraq",
    "DZ": "Algeria",
    "AL": "Albania",
    "NP": "Nepal",
    "MO": "Macau",
    "ME": "Montenegro",
    "SN": "Senegal",
    "GE": "Georgia",
    "BN": "Brunei",
    "UG": "Uganda",
    "GP": "Guadeloupe",
    "BB": "Barbados",
    "AZ": "Azerbaijan",
    "TZ": "Tanzania",
    "LY": "Libya",
    "MQ": "Martinique",
    "CM": "Cameroon",
    "BW": "Botswana",
    "ET": "Ethiopia",
    "KZ": "Kazakhstan",
    "NA": "Namibia",
    "MG": "Madagascar",
    "NC": "New Caledonia",
    "MD": "Moldova",
    "FJ": "Fiji",
    "BY": "Belarus",
    "JE": "Jersey",
    "GU": "Guam",
    "YE": "Yemen",
    "ZM": "Zambia",
    "IM": "Isle Of Man",
    "HT": "Haiti",
    "KH": "Cambodia",
    "AW": "Aruba",
    "PF": "French Polynesia",
    "AF": "Afghanistan",
    "BM": "Bermuda",
    "GY": "Guyana",
    "AM": "Armenia",
    "MW": "Malawi",
    "AG": "Antigua",
    "RW": "Rwanda",
    "GG": "Guernsey",
    "GM": "The Gambia",
    "FO": "Faroe Islands",
    "LC": "St. Lucia",
    "KY": "Cayman Islands",
    "BJ": "Benin",
    "AD": "Andorra",
    "GD": "Grenada",
    "VI": "US Virgin Islands",
    "BZ": "Belize",
    "VC": "Saint Vincent and the Grenadines",
    "MN": "Mongolia",
    "MZ": "Mozambique",
    "ML": "Mali",
    "AO": "Angola",
    "GF": "French Guiana",
    "UZ": "Uzbekistan",
    "DJ": "Djibouti",
    "BF": "Burkina Faso",
    "MC": "Monaco",
    "TG": "Togo",
    "GL": "Greenland",
    "GA": "Gabon",
    "GI": "Gibraltar",
    "CD": "Democratic Republic of the Congo",
    "KG": "Kyrgyzstan",
    "PG": "Papua New Guinea",
    "BT": "Bhutan",
    "KN": "Saint Kitts and Nevis",
    "SZ": "Swaziland",
    "LS": "Lesotho",
    "LA": "Laos",
    "LI": "Liechtenstein",
    "MP": "Northern Mariana Islands",
    "SR": "Suriname",
    "SC": "Seychelles",
    "VG": "British Virgin Islands",
    "TC": "Turks and Caicos Islands",
    "DM": "Dominica",
    "MR": "Mauritania",
    "AX": "Aland Islands",
    "SM": "San Marino",
    "SL": "Sierra Leone",
    "NE": "Niger",
    "CG": "Republic of the Congo",
    "AI": "Anguilla",
    "YT": "Mayotte",
    "CV": "Cape Verde",
    "GN": "Guinea",
    "TM": "Turkmenistan",
    "BI": "Burundi",
    "TJ": "Tajikistan",
    "VU": "Vanuatu",
    "SB": "Solomon Islands",
    "ER": "Eritrea",
    "WS": "Samoa",
    "AS": "American Samoa",
    "FK": "Falkland Islands",
    "GQ": "Equatorial Guinea",
    "TO": "Tonga",
    "KM": "Comoros",
    "PW": "Palau",
    "FM": "Federated States of Micronesia",
    "CF": "Central African Republic",
    "SO": "Somalia",
    "MH": "Marshall Islands",
    "VA": "Vatican City",
    "TD": "Chad",
    "KI": "Kiribati",
    "ST": "Sao Tome and Principe",
    "TV": "Tuvalu",
    "NR": "Nauru",
    "RE": "R\u00e9union",
    "LR": "Liberia",
    "ZW": "Zimbabwe",
    "CI": "C\u00f4te d'Ivoire",
    "MM": "Myanmar",
    "AN": "Netherlands Antilles",
    "AQ": "Antarctica",
    "BQ": "Bonaire, Sint Eustatius and Saba",
    "BV": "Bouvet Island",
    "IO": "British Indian Ocean Territory",
    "CX": "Christmas Island",
    "CC": "Cocos (Keeling) Islands",
    "CK": "Cook Islands",
    "CW": "Cura\u00e7ao",
    "TF": "French Southern Territories",
    "GW": "Guinea-Bissau",
    "HM": "Heard Island and McDonald Islands",
    "XK": "Kosovo",
    "MS": "Montserrat",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "PN": "Pitcairn",
    "BL": "Saint Barth\u00e9lemy",
    "SH": "Saint Helena",
    "MF": "Saint Martin",
    "PM": "Saint Pierre and Miquelon",
    "SX": "Sint Maarten",
    "GS": "South Georgia and the South Sandwich Islands",
    "SS": "South Sudan",
    "SJ": "Svalbard and Jan Mayen",
    "TL": "Timor-Leste",
    "TK": "Tokelau",
    "UM": "United States Minor Outlying Islands",
    "WF": "Wallis and Futuna",
    "EH": "Western Sahara"
}

CURRENCYS = {
    "AF": "AFN",
    "AX": "EUR",
    "AL": "USD",
    "DZ": "DZD",
    "AS": "USD",
    "AD": "EUR",
    "AO": "AOA",
    "AI": "XCD",
    "AG": "XCD",
    "AR": "ARS",
    "AM": "AMD",
    "AW": "AWG",
    "AU": "AUD",
    "AT": "EUR",
    "AZ": "AZN",
    "BS": "BSD",
    "BH": "BHD",
    "BD": "BDT",
    "BB": "BBD",
    "BY": "BYR",
    "BE": "EUR",
    "BZ": "USD",
    "BJ": "USD",
    "BM": "BMD",
    "BT": "BTN",
    "BO": "BOB",
    "BQ": "USD",
    "BA": "BAM",
    "BW": "BWP",
    "BV": "NOK",
    "BR": "BRL",
    "IO": "GBP",
    "BN": "BND",
    "BG": "EUR",
    "BF": "USD",
    "BI": "BIF",
    "KH": "KHR",
    "CM": "XAF",
    "CA": "CAD",
    "CV": "CVE",
    "KY": "USD",
    "CF": "XAF",
    "TD": "XAF",
    "CL": "CLP",
    "CN": "CNY",
    "CX": "AUD",
    "CC": "AUD",
    "CO": "COP",
    "KM": "KMF",
    "CG": "XAF",
    "CD": "CDF",
    "CK": "NZD",
    "CR": "CRC",
    "CI": "USD",
    "HR": "EUR",
    "CU": "CUC",
    "CW": "ANG",
    "CY": "EUR",
    "CZ": "CZK",
    "DK": "DKK",
    "DJ": "DJF",
    "DM": "XCD",
    "DO": "USD",
    "EC": "USD",
    "EG": "EGP",
    "SV": "USD",
    "GQ": "XAF",
    "ER": "ERN",
    "EE": "EUR",
    "ET": "USD",
    "FK": "GBP",
    "FO": "DKK",
    "FJ": "FJD",
    "FI": "EUR",
    "FR": "EUR",
    "GF": "EUR",
    "PF": "XPF",
    "TF": "EUR",
    "GA": "XAF",
    "GM": "GMD",
    "GE": "USD",
    "DE": "EUR",
    "GH": "USD",
    "GI": "GIP",
    "GR": "EUR",
    "GL": "DKK",
    "GD": "XCD",
    "GP": "EUR",
    "GU": "USD",
    "GT": "GTQ",
    "GG": "GBP",
    "GN": "GNF",
    "GW": "XOF",
    "GY": "USD",
    "HT": "HTG",
    "HM": "AUD",
    "VA": "EUR",
    "HN": "HNL",
    "HK": "HKD",
    "HU": "HUF",
    "IS": "ISK",
    "IN": "INR",
    "ID": "IDR",
    "IR": "IRR",
    "IQ": "USD",
    "IE": "EUR",
    "IM": "GBP",
    "IL": "ILS",
    "IT": "EUR",
    "JM": "JMD",
    "JP": "JPY",
    "JE": "GBP",
    "JO": "JOD",
    "KZ": "KZT",
    "KE": "KES",
    "KI": "AUD",
    "KP": "KPW",
    "KR": "KRW",
    "KW": "KWD",
    "KG": "USD",
    "LA": "LAK",
    "LV": "EUR",
    "LB": "LBP",
    "LS": "LSL",
    "LR": "LRD",
    "LY": "LYD",
    "LI": "CHF",
    "LT": "EUR",
    "LU": "EUR",
    "MO": "HKD",
    "MK": "EUR",
    "MG": "USD",
    "MW": "MWK",
    "MY": "MYR",
    "MV": "MVR",
    "ML": "USD",
    "MT": "EUR",
    "MH": "USD",
    "MQ": "EUR",
    "MR": "MRO",
    "MU": "USD",
    "YT": "EUR",
    "MX": "MXN",
    "FM": "USD",
    "MD": "EUR",
    "MC": "EUR",
    "MN": "USD",
    "ME": "EUR",
    "MS": "XCD",
    "MA": "USD",
    "MZ": "MZN",
    "MM": "USD",
    "NA": "NAD",
    "NR": "AUD",
    "NP": "NPR",
    "NL": "EUR",
    "NC": "XPF",
    "NZ": "NZD",
    "NI": "NIO",
    "NE": "XOF",
    "NG": "NGN",
    "NU": "NZD",
    "NF": "AUD",
    "MP": "USD",
    "NO": "NOK",
    "OM": "OMR",
    "PK": "PKR",
    "PW": "USD",
    "PS": "USD",
    "PA": "PAB",
    "PG": "PGK",
    "PY": "PYG",
    "PE": "PEN",
    "PH": "PHP",
    "PN": "NZD",
    "PL": "PLN",
    "PT": "EUR",
    "PR": "USD",
    "QA": "QAR",
    "RE": "EUR",
    "RO": "RON",
    "RU": "RUB",
    "RW": "RWF",
    "BL": "EUR",
    "SH": "SHP",
    "KN": "XCD",
    "LC": "USD",
    "MF": "EUR",
    "PM": "CAD",
    "VC": "USD",
    "WS": "USD",
    "SM": "EUR",
    "ST": "USD",
    "SA": "SAR",
    "SN": "USD",
    "RS": "EUR",
    "SC": "USD",
    "SL": "SLL",
    "SG": "SGD",
    "SX": "ANG",
    "SK": "EUR",
    "SI": "EUR",
    "SB": "SBD",
    "SO": "SOS",
    "ZA": "ZAR",
    "GS": "GBP",
    "SS": "SSP",
    "ES": "EUR",
    "LK": "USD",
    "SD": "SDG",
    "SR": "USD",
    "SJ": "NOK",
    "SZ": "SZL",
    "SE": "SEK",
    "CH": "CHF",
    "SY": "SYP",
    "TW": "TWD",
    "TJ": "TJS",
    "TZ": "USD",
    "TH": "THB",
    "TL": "USD",
    "TG": "XOF",
    "TK": "NZD",
    "TO": "USD",
    "TT": "USD",
    "TN": "TND",
    "TR": "TRY",
    "TM": "TMT",
    "TC": "USD",
    "TV": "AUD",
    "UG": "UGX",
    "UA": "USD",
    "AE": "AED",
    "GB": "GBP",
    "US": "USD",
    "UM": "USD",
    "UY": "UYU",
    "UZ": "UZS",
    "VU": "VUV",
    "VE": "VEF",
    "VN": "VND",
    "VG": "USD",
    "VI": "USD",
    "WF": "XPF",
    "EH": "USD",
    "YE": "YER",
    "ZM": "USD",
    "ZW": "USD",
}

AD_COUNTRIES = ["US", "IL", "IN", "UA", "CA", "AR", "SG", "TW", "GB", "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LK", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "NZ", "AU", "BF", "BO", "BR", "BZ", "CI", "CL", "CO",
                "DO", "EC", "GE", "GH", "GY", "ID", "IQ", "IS", "JP", "KG", "MD", "ME", "MK", "ML", "MM", "MN", "MX", "MY", "PH", "PW", "RS", "SC", "SR", "TR", "TZ", "VC", "AL", "BJ", "KY", "ET", "FK", "HN", "KE", "MG", "MU", "MA", "PY", "PE", "LC", "WS", "ST", "SN", "GS", "TO", "TT", "UY", "NO", "ZA", "ZM"]
