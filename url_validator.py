#!/usr/bin/python3

def relative_link( url ):
    result =  non_shitty_link(url) and \
        ( url[0] == '/' or \
           url[:3] == "../" ) 
        
    print url + " " + str(result)
    return result

def clean_crappy_link( url ): 
    ##i've allready encountered dumb broken links that have obvious mistakes.
    ##let's fix them!
    if has_http( chop_http(url) ):
        return chop_http(url)
    elif has_https( chop_https(url) ):
        return chop_https(url)
    else:
        return url



MAILTO_LEN = len("mailto:") 

def has_mailto(href):
    return href[:MAILTO_LEN] == 'mailto:'

def chop_mailto(href):
    return href[MAILTO_LEN:] == 'mailto:'

def make_non_relative_link( top, url ):
    
    #print "doink " +  url
    if url[:2] == '..':
        url = url [2:]
    #print url[0]
    if url[0] =='/':
        url = url[1:]
    #print url
    if top[-1] == '\n':
        top = top[:-1]
    if top[-1:] != '/':
        top = top + '/'
    #print "TO: " + top + url
    return top + url

def is_local_div_link(url):
    return url[0] == '#'

def non_shitty_link(url):
    return url is not None and  \
                url != '' and   \
                len(url)> 1 and \
                not is_local_div_link(url) 
         # i see many corner cases in the future. (edit: maybe not?)

def has_http( test_url ):
    #print "has http:// ",  test_url, test_url[:7] == 'http://' 
    return test_url[:7] == 'http://'

def has_https( test_url ):
    #print "has https:// " , test_url, test_url[:8] == 'https://'

    return test_url[:8] == 'https://'

def chop_https( test_url ):
    #print "chopping ", test_url, "to ", test_url[8:]
    return test_url[8:]

def chop_http(test_url):
    #print "chopping ", test_url, "to ", test_url[7:]
    return test_url[7:]

def has_www( test_url ):
    #print "has www. ", test_url,  test_url[:4] == 'www.'
    return test_url[:4] == 'www.'

def chop_www( test_url ):
    return test_url[4:]

def has_top_level_domain( test_url ):
    #this is all wrong :(
    test_url = test_url.upper()
    domlist = [ 'AAA', 'ABB', 'ABBOTT', 'ABOGADO', 'AC', 'ACADEMY', 'ACCENTURE', 'ACCOUNTANT', 'ACCOUNTANTS', 'ACO', 'ACTIVE', 'ACTOR', 'AD', 'ADS', 'ADULT', 'AE', 'AEG', 'AERO', 'AF', 'AFL', 'AG', 'AGENCY', 'AI', 'AIG', 'AIRFORCE', 'AIRTEL', 'AL', 'ALLFINANZ', 'ALSACE', 'AM', 'AMICA', 'AMSTERDAM', 'ANDROID', 'AO', 'APARTMENTS', 'APP', 'AQ', 'AQUARELLE', 'AR', 'ARCHI', 'ARMY', 'ARPA', 'AS', 'ASIA', 'ASSOCIATES', 'AT', 'ATTORNEY', 'AU', 'AUCTION', 'AUDIO', 'AUTO', 'AUTOS', 'AW', 'AX', 'AXA', 'AZ', 'AZURE', 'BA', 'BAND', 'BANK', 'BAR', 'BARCELONA', 'BARCLAYCARD', 'BARCLAYS', 'BARGAINS', 'BAUHAUS', 'BAYERN', 'BB', 'BBC', 'BBVA', 'BCN', 'BD', 'BE', 'BEER', 'BENTLEY', 'BERLIN', 'BEST', 'BET', 'BF', 'BG', 'BH', 'BHARTI', 'BI', 'BIBLE', 'BID', 'BIKE', 'BING', 'BINGO', 'BIO', 'BIZ', 'BJ', 'BLACK', 'BLACKFRIDAY', 'BLOOMBERG', 'BLUE', 'BM', 'BMW', 'BN', 'BNL', 'BNPPARIBAS', 'BO', 'BOATS', 'BOND', 'BOO', 'BOOTS', 'BOUTIQUE', 'BR', 'BRADESCO', 'BRIDGESTONE', 'BROKER', 'BROTHER', 'BRUSSELS', 'BS', 'BT', 'BUDAPEST', 'BUILD', 'BUILDERS', 'BUSINESS', 'BUZZ', 'BV', 'BW', 'BY', 'BZ', 'BZH', 'CA', 'CAB', 'CAFE', 'CAL', 'CAMERA', 'CAMP', 'CANCERRESEARCH', 'CANON', 'CAPETOWN', 'CAPITAL', 'CAR', 'CARAVAN', 'CARDS', 'CARE', 'CAREER', 'CAREERS', 'CARS', 'CARTIER', 'CASA', 'CASH', 'CASINO', 'CAT', 'CATERING', 'CBA', 'CBN', 'CC', 'CD', 'CEB', 'CENTER', 'CEO', 'CERN', 'CF', 'CFA', 'CFD', 'CG', 'CH', 'CHANEL', 'CHANNEL', 'CHAT', 'CHEAP', 'CHLOE', 'CHRISTMAS', 'CHROME', 'CHURCH', 'CI', 'CISCO', 'CITIC', 'CITY', 'CK', 'CL', 'CLAIMS', 'CLEANING', 'CLICK', 'CLINIC', 'CLOTHING', 'CLOUD', 'CLUB', 'CM', 'CN', 'CO', 'COACH', 'CODES', 'COFFEE', 'COLLEGE', 'COLOGNE', 'COM', 'COMMBANK', 'COMMUNITY', 'COMPANY', 'COMPUTER', 'CONDOS', 'CONSTRUCTION', 'CONSULTING', 'CONTRACTORS', 'COOKING', 'COOL', 'COOP', 'CORSICA', 'COUNTRY', 'COUPONS', 'COURSES', 'CR', 'CREDIT', 'CREDITCARD', 'CRICKET', 'CROWN', 'CRS', 'CRUISES', 'CSC', 'CU', 'CUISINELLA', 'CV', 'CW', 'CX', 'CY', 'CYMRU', 'CYOU', 'CZ', 'DABUR', 'DAD', 'DANCE', 'DATE', 'DATING', 'DATSUN', 'DAY', 'DCLK', 'DE', 'DEALS', 'DEGREE', 'DELIVERY', 'DELTA', 'DEMOCRAT', 'DENTAL', 'DENTIST', 'DESI', 'DESIGN', 'DEV', 'DIAMONDS', 'DIET', 'DIGITAL', 'DIRECT', 'DIRECTORY', 'DISCOUNT', 'DJ', 'DK', 'DM', 'DNP', 'DO', 'DOCS', 'DOG', 'DOHA', 'DOMAINS', 'DOOSAN', 'DOWNLOAD', 'DRIVE', 'DURBAN', 'DVAG', 'DZ', 'EARTH', 'EAT', 'EC', 'EDU', 'EDUCATION', 'EE', 'EG', 'EMAIL', 'EMERCK', 'ENERGY', 'ENGINEER', 'ENGINEERING', 'ENTERPRISES', 'EPSON', 'EQUIPMENT', 'ER', 'ERNI', 'ES', 'ESQ', 'ESTATE', 'ET', 'EU', 'EUROVISION', 'EUS', 'EVENTS', 'EVERBANK', 'EXCHANGE', 'EXPERT', 'EXPOSED', 'EXPRESS', 'FAGE', 'FAIL', 'FAITH', 'FAMILY', 'FAN', 'FANS', 'FARM', 'FASHION', 'FEEDBACK', 'FI', 'FILM', 'FINANCE', 'FINANCIAL', 'FIRMDALE', 'FISH', 'FISHING', 'FIT', 'FITNESS', 'FJ', 'FK', 'FLIGHTS', 'FLORIST', 'FLOWERS', 'FLSMIDTH', 'FLY', 'FM', 'FO', 'FOO', 'FOOTBALL', 'FOREX', 'FORSALE', 'FORUM', 'FOUNDATION', 'FR', 'FRL', 'FROGANS', 'FUND', 'FURNITURE', 'FUTBOL', 'FYI', 'GA', 'GAL', 'GALLERY', 'GAME', 'GARDEN', 'GB', 'GBIZ', 'GD', 'GDN', 'GE', 'GEA', 'GENT', 'GENTING', 'GF', 'GG', 'GGEE', 'GH', 'GI', 'GIFT', 'GIFTS', 'GIVES', 'GIVING', 'GL', 'GLASS', 'GLE', 'GLOBAL', 'GLOBO', 'GM', 'GMAIL', 'GMO', 'GMX', 'GN', 'GOLD', 'GOLDPOINT', 'GOLF', 'GOO', 'GOOG', 'GOOGLE', 'GOP', 'GOV', 'GP', 'GQ', 'GR', 'GRAPHICS', 'GRATIS', 'GREEN', 'GRIPE', 'GROUP', 'GS', 'GT', 'GU', 'GUGE', 'GUIDE', 'GUITARS', 'GURU', 'GW', 'GY', 'HAMBURG', 'HANGOUT', 'HAUS', 'HEALTHCARE', 'HELP', 'HERE', 'HERMES', 'HIPHOP', 'HITACHI', 'HIV', 'HK', 'HM', 'HN', 'HOCKEY', 'HOLDINGS', 'HOLIDAY', 'HOMEDEPOT', 'HOMES', 'HONDA', 'HORSE', 'HOST', 'HOSTING', 'HOTELES', 'HOTMAIL', 'HOUSE', 'HOW', 'HR', 'HSBC', 'HT', 'HU', 'IBM', 'ICBC', 'ICE', 'ICU', 'ID', 'IE', 'IFM', 'IINET', 'IL', 'IM', 'IMMO', 'IMMOBILIEN', 'IN', 'INDUSTRIES', 'INFINITI', 'INFO', 'ING', 'INK', 'INSTITUTE', 'INSURE', 'INT', 'INTERNATIONAL', 'INVESTMENTS', 'IO', 'IPIRANGA', 'IQ', 'IR', 'IRISH', 'IS', 'IST', 'ISTANBUL', 'IT', 'ITAU', 'IWC', 'JAVA', 'JCB', 'JE', 'JETZT', 'JEWELRY', 'JLC', 'JLL', 'JM', 'JO', 'JOBS', 'JOBURG', 'JP', 'JPRS', 'JUEGOS', 'KAUFEN', 'KDDI', 'KE', 'KG', 'KH', 'KI', 'KIM', 'KITCHEN', 'KIWI', 'KM', 'KN', 'KOELN', 'KOMATSU', 'KP', 'KR', 'KRD', 'KRED', 'KW', 'KY', 'KYOTO', 'KZ', 'LA', 'LACAIXA', 'LANCASTER', 'LAND', 'LASALLE', 'LAT', 'LATROBE', 'LAW', 'LAWYER', 'LB', 'LC', 'LDS', 'LEASE', 'LECLERC', 'LEGAL', 'LEXUS', 'LGBT', 'LI', 'LIAISON', 'LIDL', 'LIFE', 'LIGHTING', 'LIMITED', 'LIMO', 'LINK', 'LIVE', 'LIXIL', 'LK', 'LOAN', 'LOANS', 'LOL', 'LONDON', 'LOTTE', 'LOTTO', 'LOVE', 'LR', 'LS', 'LT', 'LTDA', 'LU', 'LUPIN', 'LUXE', 'LUXURY', 'LV', 'LY', 'MA', 'MADRID', 'MAIF', 'MAISON', 'MAN', 'MANAGEMENT', 'MANGO', 'MARKET', 'MARKETING', 'MARKETS', 'MARRIOTT', 'MBA', 'MC', 'MD', 'ME', 'MEDIA', 'MEET', 'MELBOURNE', 'MEME', 'MEMORIAL', 'MEN', 'MENU', 'MG', 'MH', 'MIAMI', 'MICROSOFT', 'MIL', 'MINI', 'MK', 'ML', 'MM', 'MMA', 'MN', 'MO', 'MOBI', 'MODA', 'MOE', 'MOM', 'MONASH', 'MONEY', 'MONTBLANC', 'MORMON', 'MORTGAGE', 'MOSCOW', 'MOTORCYCLES', 'MOV', 'MOVIE', 'MOVISTAR', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MTN', 'MTPC', 'MU', 'MUSEUM', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NADEX', 'NAGOYA', 'NAME', 'NAVY', 'NC', 'NE', 'NEC', 'NET', 'NETBANK', 'NETWORK', 'NEUSTAR', 'NEW', 'NEWS', 'NEXUS', 'NF', 'NG', 'NGO', 'NHK', 'NI', 'NICO', 'NINJA', 'NISSAN', 'NL', 'NO', 'NOKIA', 'NP', 'NR', 'NRA', 'NRW', 'NTT', 'NU', 'NYC', 'NZ', 'OFFICE', 'OKINAWA', 'OM', 'OMEGA', 'ONE', 'ONG', 'ONL', 'ONLINE', 'OOO', 'ORACLE', 'ORANGE', 'ORG', 'ORGANIC', 'OSAKA', 'OTSUKA', 'OVH', 'PA', 'PAGE', 'PANERAI', 'PARIS', 'PARTNERS', 'PARTS', 'PARTY', 'PE', 'PET', 'PF', 'PG', 'PH', 'PHARMACY', 'PHILIPS', 'PHOTO', 'PHOTOGRAPHY', 'PHOTOS', 'PHYSIO', 'PIAGET', 'PICS', 'PICTET', 'PICTURES', 'PINK', 'PIZZA', 'PK', 'PL', 'PLACE', 'PLAY', 'PLUMBING', 'PLUS', 'PM', 'PN', 'POHL', 'POKER', 'PORN', 'POST', 'PR', 'PRAXI', 'PRESS', 'PRO', 'PROD', 'PRODUCTIONS', 'PROF', 'PROPERTIES', 'PROPERTY', 'PS', 'PT', 'PUB', 'PW', 'PY', 'QA', 'QPON', 'QUEBEC', 'RACING', 'RE', 'REALTOR', 'REALTY', 'RECIPES', 'RED', 'REDSTONE', 'REHAB', 'REISE', 'REISEN', 'REIT', 'REN', 'RENT', 'RENTALS', 'REPAIR', 'REPORT', 'REPUBLICAN', 'REST', 'RESTAURANT', 'REVIEW', 'REVIEWS', 'RICH', 'RICOH', 'RIO', 'RIP', 'RO', 'ROCKS', 'RODEO', 'RS', 'RSVP', 'RU', 'RUHR', 'RUN', 'RW', 'RYUKYU', 'SA', 'SAARLAND', 'SAKURA', 'SALE', 'SAMSUNG', 'SANDVIK', 'SANDVIKCOROMANT', 'SANOFI', 'SAP', 'SARL', 'SAXO', 'SB', 'SC', 'SCA', 'SCB', 'SCHMIDT', 'SCHOLARSHIPS', 'SCHOOL', 'SCHULE', 'SCHWARZ', 'SCIENCE', 'SCOR', 'SCOT', 'SD', 'SE', 'SEAT', 'SEEK', 'SENER', 'SERVICES', 'SEW', 'SEX', 'SEXY', 'SG', 'SH', 'SHIKSHA', 'SHOES', 'SHOW', 'SHRIRAM', 'SI', 'SINGLES', 'SITE', 'SJ', 'SK', 'SKI', 'SKY', 'SKYPE', 'SL', 'SM', 'SN', 'SNCF', 'SO', 'SOCCER', 'SOCIAL', 'SOFTWARE', 'SOHU', 'SOLAR', 'SOLUTIONS', 'SONY', 'SOY', 'SPACE', 'SPIEGEL', 'SPREADBETTING', 'SR', 'SRL', 'ST', 'STARHUB', 'STATOIL', 'STC', 'STCGROUP', 'STUDIO', 'STUDY', 'STYLE', 'SU', 'SUCKS', 'SUPPLIES', 'SUPPLY', 'SUPPORT', 'SURF', 'SURGERY', 'SUZUKI', 'SV', 'SWATCH', 'SWISS', 'SX', 'SY', 'SYDNEY', 'SYSTEMS', 'SZ', 'TAIPEI', 'TATAMOTORS', 'TATAR', 'TATTOO', 'TAX', 'TAXI', 'TC', 'TD', 'TEAM', 'TECH', 'TECHNOLOGY', 'TEL', 'TELEFONICA', 'TEMASEK', 'TENNIS', 'TF', 'TG', 'TH', 'THD', 'THEATER', 'TICKETS', 'TIENDA', 'TIPS', 'TIRES', 'TIROL', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TODAY', 'TOKYO', 'TOOLS', 'TOP', 'TORAY', 'TOSHIBA', 'TOURS', 'TOWN', 'TOYOTA', 'TOYS', 'TR', 'TRADE', 'TRADING', 'TRAINING', 'TRAVEL', 'TRUST', 'TT', 'TUI', 'TV', 'TW', 'TZ', 'UA', 'UBS', 'UG', 'UK', 'UNIVERSITY', 'UNO', 'UOL', 'US', 'UY', 'UZ', 'VA', 'VACATIONS', 'VC', 'VE', 'VEGAS', 'VENTURES', 'VERSICHERUNG', 'VET', 'VG', 'VI', 'VIAJES', 'VIDEO', 'VILLAS', 'VIN', 'VISION', 'VISTA', 'VISTAPRINT', 'VIVA', 'VLAANDEREN', 'VN', 'VODKA', 'VOTE', 'VOTING', 'VOTO', 'VOYAGE', 'VU', 'WALES', 'WALTER', 'WANG', 'WATCH', 'WEBCAM', 'WEBSITE', 'WED', 'WEDDING', 'WEIR', 'WF', 'WHOSWHO', 'WIEN', 'WIKI', 'WILLIAMHILL', 'WIN', 'WINDOWS', 'WINE', 'WME', 'WORK', 'WORKS', 'WORLD', 'WS', 'WTC', 'WTF', 'XBOX', 'XEROX', 'XIN', 'XN--11B4C3D', 'XN--1QQW23A', 'XN--30RR7Y', 'XN--3BST00M', 'XN--3DS443G', 'XN--3E0B707E', 'XN--3PXU8K', 'XN--42C2D9A', 'XN--45BRJ9C', 'XN--45Q11C', 'XN--4GBRIM', 'XN--55QW42G', 'XN--55QX5D', 'XN--6FRZ82G', 'XN--6QQ986B3XL', 'XN--80ADXHKS', 'XN--80AO21A', 'XN--80ASEHDB', 'XN--80ASWG', 'XN--90A3AC', 'XN--90AIS', 'XN--9DBQ2A', 'XN--9ET52U', 'XN--B4W605FERD', 'XN--C1AVG', 'XN--C2BR7G', 'XN--CG4BKI', 'XN--CLCHC0EA0B2G2A9GCD', 'XN--CZR694B', 'XN--CZRS0T', 'XN--CZRU2D', 'XN--D1ACJ3B', 'XN--D1ALF', 'XN--EFVY88H', 'XN--ESTV75G', 'XN--FHBEI', 'XN--FIQ228C5HS', 'XN--FIQ64B', 'XN--FIQS8S', 'XN--FIQZ9S', 'XN--FJQ720A', 'XN--FLW351E', 'XN--FPCRJ9C3D', 'XN--FZC2C9E2C', 'XN--GECRJ9C', 'XN--H2BRJ9C', 'XN--HXT814E', 'XN--I1B6B1A6A2E', 'XN--IMR513N', 'XN--IO0A7I', 'XN--J1AEF', 'XN--J1AMH', 'XN--J6W193G', 'XN--KCRX77D1X4A', 'XN--KPRW13D', 'XN--KPRY57D', 'XN--KPUT3I', 'XN--L1ACC', 'XN--LGBBAT1AD8J', 'XN--MGB9AWBF', 'XN--MGBA3A4F16A', 'XN--MGBAAM7A8H', 'XN--MGBAB2BD', 'XN--MGBAYH7GPA', 'XN--MGBBH1A71E', 'XN--MGBC0A9AZCG', 'XN--MGBERP4A5D4AR', 'XN--MGBPL2FH', 'XN--MGBX4CD0AB', 'XN--MK1BU44C', 'XN--MXTQ1M', 'XN--NGBC5AZD', 'XN--NODE', 'XN--NQV7F', 'XN--NQV7FS00EMA', 'XN--NYQY26A', 'XN--O3CW4H', 'XN--OGBPF8FL', 'XN--P1ACF', 'XN--P1AI', 'XN--PGBS0DH', 'XN--PSSY2U', 'XN--Q9JYB4C', 'XN--QCKA1PMC', 'XN--RHQV96G', 'XN--S9BRJ9C', 'XN--SES554G', 'XN--T60B56A', 'XN--TCKWE', 'XN--UNUP4Y', 'XN--VERMGENSBERATER-CTB', 'XN--VERMGENSBERATUNG-PWB', 'XN--VHQUV', 'XN--VUQ861B', 'XN--WGBH1C', 'XN--WGBL6A', 'XN--XHQ521B', 'XN--XKC2AL3HYE2A', 'XN--XKC2DL3A5EE0H', 'XN--Y9A3AQ', 'XN--YFRO4I67O', 'XN--YGBI2AMMX', 'XN--ZFR164B', 'XPERIA', 'XXX', 'XYZ', 'YACHTS', 'YANDEX', 'YE', 'YODOBASHI', 'YOGA', 'YOKOHAMA', 'YOUTUBE', 'YT', 'ZA', 'ZIP', 'ZM', 'ZONE', 'ZUERICH', 'ZW' ]         ##ok nevermind
    result = [ x for x in domlist if x == test_url[-len(x): ] and test_url[-len(x)-1:-len(x)] == '.' ]
    return result 
# https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

def is_tip_top_level( test_url ):
    #print has_http(test_url)
    chopped = ""
    if has_https(test_url):
        chopped = chop_https(test_url)
    elif has_http(test_url):
        chopped = chop_http( test_url )
        #print had_http
        #print has_www( had_http)
    if has_www( chopped ):
        chopped = chop_www( chopped )
            #print had_www
    if chopped != "":
        maybe_domain = chopped.split('.')[-1]
        if maybe_domain[:-1] == '/':
            maybe_domain = maybe_domain[:-1]
        #print maybe_domain
        return maybe_domain.upper() in [ 'AAA', 'ABB', 'ABBOTT', 'ABOGADO', 'AC', 'ACADEMY', 'ACCENTURE', 'ACCOUNTANT', 'ACCOUNTANTS', 'ACO', 'ACTIVE', 'ACTOR', 'AD', 'ADS', 'ADULT', 'AE', 'AEG', 'AERO', 'AF', 'AFL', 'AG', 'AGENCY', 'AI', 'AIG', 'AIRFORCE', 'AIRTEL', 'AL', 'ALLFINANZ', 'ALSACE', 'AM', 'AMICA', 'AMSTERDAM', 'ANDROID', 'AO', 'APARTMENTS', 'APP', 'AQ', 'AQUARELLE', 'AR', 'ARCHI', 'ARMY', 'ARPA', 'AS', 'ASIA', 'ASSOCIATES', 'AT', 'ATTORNEY', 'AU', 'AUCTION', 'AUDIO', 'AUTO', 'AUTOS', 'AW', 'AX', 'AXA', 'AZ', 'AZURE', 'BA', 'BAND', 'BANK', 'BAR', 'BARCELONA', 'BARCLAYCARD', 'BARCLAYS', 'BARGAINS', 'BAUHAUS', 'BAYERN', 'BB', 'BBC', 'BBVA', 'BCN', 'BD', 'BE', 'BEER', 'BENTLEY', 'BERLIN', 'BEST', 'BET', 'BF', 'BG', 'BH', 'BHARTI', 'BI', 'BIBLE', 'BID', 'BIKE', 'BING', 'BINGO', 'BIO', 'BIZ', 'BJ', 'BLACK', 'BLACKFRIDAY', 'BLOOMBERG', 'BLUE', 'BM', 'BMW', 'BN', 'BNL', 'BNPPARIBAS', 'BO', 'BOATS', 'BOND', 'BOO', 'BOOTS', 'BOUTIQUE', 'BR', 'BRADESCO', 'BRIDGESTONE', 'BROKER', 'BROTHER', 'BRUSSELS', 'BS', 'BT', 'BUDAPEST', 'BUILD', 'BUILDERS', 'BUSINESS', 'BUZZ', 'BV', 'BW', 'BY', 'BZ', 'BZH', 'CA', 'CAB', 'CAFE', 'CAL', 'CAMERA', 'CAMP', 'CANCERRESEARCH', 'CANON', 'CAPETOWN', 'CAPITAL', 'CAR', 'CARAVAN', 'CARDS', 'CARE', 'CAREER', 'CAREERS', 'CARS', 'CARTIER', 'CASA', 'CASH', 'CASINO', 'CAT', 'CATERING', 'CBA', 'CBN', 'CC', 'CD', 'CEB', 'CENTER', 'CEO', 'CERN', 'CF', 'CFA', 'CFD', 'CG', 'CH', 'CHANEL', 'CHANNEL', 'CHAT', 'CHEAP', 'CHLOE', 'CHRISTMAS', 'CHROME', 'CHURCH', 'CI', 'CISCO', 'CITIC', 'CITY', 'CK', 'CL', 'CLAIMS', 'CLEANING', 'CLICK', 'CLINIC', 'CLOTHING', 'CLOUD', 'CLUB', 'CM', 'CN', 'CO', 'COACH', 'CODES', 'COFFEE', 'COLLEGE', 'COLOGNE', 'COM', 'COMMBANK', 'COMMUNITY', 'COMPANY', 'COMPUTER', 'CONDOS', 'CONSTRUCTION', 'CONSULTING', 'CONTRACTORS', 'COOKING', 'COOL', 'COOP', 'CORSICA', 'COUNTRY', 'COUPONS', 'COURSES', 'CR', 'CREDIT', 'CREDITCARD', 'CRICKET', 'CROWN', 'CRS', 'CRUISES', 'CSC', 'CU', 'CUISINELLA', 'CV', 'CW', 'CX', 'CY', 'CYMRU', 'CYOU', 'CZ', 'DABUR', 'DAD', 'DANCE', 'DATE', 'DATING', 'DATSUN', 'DAY', 'DCLK', 'DE', 'DEALS', 'DEGREE', 'DELIVERY', 'DELTA', 'DEMOCRAT', 'DENTAL', 'DENTIST', 'DESI', 'DESIGN', 'DEV', 'DIAMONDS', 'DIET', 'DIGITAL', 'DIRECT', 'DIRECTORY', 'DISCOUNT', 'DJ', 'DK', 'DM', 'DNP', 'DO', 'DOCS', 'DOG', 'DOHA', 'DOMAINS', 'DOOSAN', 'DOWNLOAD', 'DRIVE', 'DURBAN', 'DVAG', 'DZ', 'EARTH', 'EAT', 'EC', 'EDU', 'EDUCATION', 'EE', 'EG', 'EMAIL', 'EMERCK', 'ENERGY', 'ENGINEER', 'ENGINEERING', 'ENTERPRISES', 'EPSON', 'EQUIPMENT', 'ER', 'ERNI', 'ES', 'ESQ', 'ESTATE', 'ET', 'EU', 'EUROVISION', 'EUS', 'EVENTS', 'EVERBANK', 'EXCHANGE', 'EXPERT', 'EXPOSED', 'EXPRESS', 'FAGE', 'FAIL', 'FAITH', 'FAMILY', 'FAN', 'FANS', 'FARM', 'FASHION', 'FEEDBACK', 'FI', 'FILM', 'FINANCE', 'FINANCIAL', 'FIRMDALE', 'FISH', 'FISHING', 'FIT', 'FITNESS', 'FJ', 'FK', 'FLIGHTS', 'FLORIST', 'FLOWERS', 'FLSMIDTH', 'FLY', 'FM', 'FO', 'FOO', 'FOOTBALL', 'FOREX', 'FORSALE', 'FORUM', 'FOUNDATION', 'FR', 'FRL', 'FROGANS', 'FUND', 'FURNITURE', 'FUTBOL', 'FYI', 'GA', 'GAL', 'GALLERY', 'GAME', 'GARDEN', 'GB', 'GBIZ', 'GD', 'GDN', 'GE', 'GEA', 'GENT', 'GENTING', 'GF', 'GG', 'GGEE', 'GH', 'GI', 'GIFT', 'GIFTS', 'GIVES', 'GIVING', 'GL', 'GLASS', 'GLE', 'GLOBAL', 'GLOBO', 'GM', 'GMAIL', 'GMO', 'GMX', 'GN', 'GOLD', 'GOLDPOINT', 'GOLF', 'GOO', 'GOOG', 'GOOGLE', 'GOP', 'GOV', 'GP', 'GQ', 'GR', 'GRAPHICS', 'GRATIS', 'GREEN', 'GRIPE', 'GROUP', 'GS', 'GT', 'GU', 'GUGE', 'GUIDE', 'GUITARS', 'GURU', 'GW', 'GY', 'HAMBURG', 'HANGOUT', 'HAUS', 'HEALTHCARE', 'HELP', 'HERE', 'HERMES', 'HIPHOP', 'HITACHI', 'HIV', 'HK', 'HM', 'HN', 'HOCKEY', 'HOLDINGS', 'HOLIDAY', 'HOMEDEPOT', 'HOMES', 'HONDA', 'HORSE', 'HOST', 'HOSTING', 'HOTELES', 'HOTMAIL', 'HOUSE', 'HOW', 'HR', 'HSBC', 'HT', 'HU', 'IBM', 'ICBC', 'ICE', 'ICU', 'ID', 'IE', 'IFM', 'IINET', 'IL', 'IM', 'IMMO', 'IMMOBILIEN', 'IN', 'INDUSTRIES', 'INFINITI', 'INFO', 'ING', 'INK', 'INSTITUTE', 'INSURE', 'INT', 'INTERNATIONAL', 'INVESTMENTS', 'IO', 'IPIRANGA', 'IQ', 'IR', 'IRISH', 'IS', 'IST', 'ISTANBUL', 'IT', 'ITAU', 'IWC', 'JAVA', 'JCB', 'JE', 'JETZT', 'JEWELRY', 'JLC', 'JLL', 'JM', 'JO', 'JOBS', 'JOBURG', 'JP', 'JPRS', 'JUEGOS', 'KAUFEN', 'KDDI', 'KE', 'KG', 'KH', 'KI', 'KIM', 'KITCHEN', 'KIWI', 'KM', 'KN', 'KOELN', 'KOMATSU', 'KP', 'KR', 'KRD', 'KRED', 'KW', 'KY', 'KYOTO', 'KZ', 'LA', 'LACAIXA', 'LANCASTER', 'LAND', 'LASALLE', 'LAT', 'LATROBE', 'LAW', 'LAWYER', 'LB', 'LC', 'LDS', 'LEASE', 'LECLERC', 'LEGAL', 'LEXUS', 'LGBT', 'LI', 'LIAISON', 'LIDL', 'LIFE', 'LIGHTING', 'LIMITED', 'LIMO', 'LINK', 'LIVE', 'LIXIL', 'LK', 'LOAN', 'LOANS', 'LOL', 'LONDON', 'LOTTE', 'LOTTO', 'LOVE', 'LR', 'LS', 'LT', 'LTDA', 'LU', 'LUPIN', 'LUXE', 'LUXURY', 'LV', 'LY', 'MA', 'MADRID', 'MAIF', 'MAISON', 'MAN', 'MANAGEMENT', 'MANGO', 'MARKET', 'MARKETING', 'MARKETS', 'MARRIOTT', 'MBA', 'MC', 'MD', 'ME', 'MEDIA', 'MEET', 'MELBOURNE', 'MEME', 'MEMORIAL', 'MEN', 'MENU', 'MG', 'MH', 'MIAMI', 'MICROSOFT', 'MIL', 'MINI', 'MK', 'ML', 'MM', 'MMA', 'MN', 'MO', 'MOBI', 'MODA', 'MOE', 'MOM', 'MONASH', 'MONEY', 'MONTBLANC', 'MORMON', 'MORTGAGE', 'MOSCOW', 'MOTORCYCLES', 'MOV', 'MOVIE', 'MOVISTAR', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MTN', 'MTPC', 'MU', 'MUSEUM', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NADEX', 'NAGOYA', 'NAME', 'NAVY', 'NC', 'NE', 'NEC', 'NET', 'NETBANK', 'NETWORK', 'NEUSTAR', 'NEW', 'NEWS', 'NEXUS', 'NF', 'NG', 'NGO', 'NHK', 'NI', 'NICO', 'NINJA', 'NISSAN', 'NL', 'NO', 'NOKIA', 'NP', 'NR', 'NRA', 'NRW', 'NTT', 'NU', 'NYC', 'NZ', 'OFFICE', 'OKINAWA', 'OM', 'OMEGA', 'ONE', 'ONG', 'ONL', 'ONLINE', 'OOO', 'ORACLE', 'ORANGE', 'ORG', 'ORGANIC', 'OSAKA', 'OTSUKA', 'OVH', 'PA', 'PAGE', 'PANERAI', 'PARIS', 'PARTNERS', 'PARTS', 'PARTY', 'PE', 'PET', 'PF', 'PG', 'PH', 'PHARMACY', 'PHILIPS', 'PHOTO', 'PHOTOGRAPHY', 'PHOTOS', 'PHYSIO', 'PIAGET', 'PICS', 'PICTET', 'PICTURES', 'PINK', 'PIZZA', 'PK', 'PL', 'PLACE', 'PLAY', 'PLUMBING', 'PLUS', 'PM', 'PN', 'POHL', 'POKER', 'PORN', 'POST', 'PR', 'PRAXI', 'PRESS', 'PRO', 'PROD', 'PRODUCTIONS', 'PROF', 'PROPERTIES', 'PROPERTY', 'PS', 'PT', 'PUB', 'PW', 'PY', 'QA', 'QPON', 'QUEBEC', 'RACING', 'RE', 'REALTOR', 'REALTY', 'RECIPES', 'RED', 'REDSTONE', 'REHAB', 'REISE', 'REISEN', 'REIT', 'REN', 'RENT', 'RENTALS', 'REPAIR', 'REPORT', 'REPUBLICAN', 'REST', 'RESTAURANT', 'REVIEW', 'REVIEWS', 'RICH', 'RICOH', 'RIO', 'RIP', 'RO', 'ROCKS', 'RODEO', 'RS', 'RSVP', 'RU', 'RUHR', 'RUN', 'RW', 'RYUKYU', 'SA', 'SAARLAND', 'SAKURA', 'SALE', 'SAMSUNG', 'SANDVIK', 'SANDVIKCOROMANT', 'SANOFI', 'SAP', 'SARL', 'SAXO', 'SB', 'SC', 'SCA', 'SCB', 'SCHMIDT', 'SCHOLARSHIPS', 'SCHOOL', 'SCHULE', 'SCHWARZ', 'SCIENCE', 'SCOR', 'SCOT', 'SD', 'SE', 'SEAT', 'SEEK', 'SENER', 'SERVICES', 'SEW', 'SEX', 'SEXY', 'SG', 'SH', 'SHIKSHA', 'SHOES', 'SHOW', 'SHRIRAM', 'SI', 'SINGLES', 'SITE', 'SJ', 'SK', 'SKI', 'SKY', 'SKYPE', 'SL', 'SM', 'SN', 'SNCF', 'SO', 'SOCCER', 'SOCIAL', 'SOFTWARE', 'SOHU', 'SOLAR', 'SOLUTIONS', 'SONY', 'SOY', 'SPACE', 'SPIEGEL', 'SPREADBETTING', 'SR', 'SRL', 'ST', 'STARHUB', 'STATOIL', 'STC', 'STCGROUP', 'STUDIO', 'STUDY', 'STYLE', 'SU', 'SUCKS', 'SUPPLIES', 'SUPPLY', 'SUPPORT', 'SURF', 'SURGERY', 'SUZUKI', 'SV', 'SWATCH', 'SWISS', 'SX', 'SY', 'SYDNEY', 'SYSTEMS', 'SZ', 'TAIPEI', 'TATAMOTORS', 'TATAR', 'TATTOO', 'TAX', 'TAXI', 'TC', 'TD', 'TEAM', 'TECH', 'TECHNOLOGY', 'TEL', 'TELEFONICA', 'TEMASEK', 'TENNIS', 'TF', 'TG', 'TH', 'THD', 'THEATER', 'TICKETS', 'TIENDA', 'TIPS', 'TIRES', 'TIROL', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TODAY', 'TOKYO', 'TOOLS', 'TOP', 'TORAY', 'TOSHIBA', 'TOURS', 'TOWN', 'TOYOTA', 'TOYS', 'TR', 'TRADE', 'TRADING', 'TRAINING', 'TRAVEL', 'TRUST', 'TT', 'TUI', 'TV', 'TW', 'TZ', 'UA', 'UBS', 'UG', 'UK', 'UNIVERSITY', 'UNO', 'UOL', 'US', 'UY', 'UZ', 'VA', 'VACATIONS', 'VC', 'VE', 'VEGAS', 'VENTURES', 'VERSICHERUNG', 'VET', 'VG', 'VI', 'VIAJES', 'VIDEO', 'VILLAS', 'VIN', 'VISION', 'VISTA', 'VISTAPRINT', 'VIVA', 'VLAANDEREN', 'VN', 'VODKA', 'VOTE', 'VOTING', 'VOTO', 'VOYAGE', 'VU', 'WALES', 'WALTER', 'WANG', 'WATCH', 'WEBCAM', 'WEBSITE', 'WED', 'WEDDING', 'WEIR', 'WF', 'WHOSWHO', 'WIEN', 'WIKI', 'WILLIAMHILL', 'WIN', 'WINDOWS', 'WINE', 'WME', 'WORK', 'WORKS', 'WORLD', 'WS', 'WTC', 'WTF', 'XBOX', 'XEROX', 'XIN', 'XN--11B4C3D', 'XN--1QQW23A', 'XN--30RR7Y', 'XN--3BST00M', 'XN--3DS443G', 'XN--3E0B707E', 'XN--3PXU8K', 'XN--42C2D9A', 'XN--45BRJ9C', 'XN--45Q11C', 'XN--4GBRIM', 'XN--55QW42G', 'XN--55QX5D', 'XN--6FRZ82G', 'XN--6QQ986B3XL', 'XN--80ADXHKS', 'XN--80AO21A', 'XN--80ASEHDB', 'XN--80ASWG', 'XN--90A3AC', 'XN--90AIS', 'XN--9DBQ2A', 'XN--9ET52U', 'XN--B4W605FERD', 'XN--C1AVG', 'XN--C2BR7G', 'XN--CG4BKI', 'XN--CLCHC0EA0B2G2A9GCD', 'XN--CZR694B', 'XN--CZRS0T', 'XN--CZRU2D', 'XN--D1ACJ3B', 'XN--D1ALF', 'XN--EFVY88H', 'XN--ESTV75G', 'XN--FHBEI', 'XN--FIQ228C5HS', 'XN--FIQ64B', 'XN--FIQS8S', 'XN--FIQZ9S', 'XN--FJQ720A', 'XN--FLW351E', 'XN--FPCRJ9C3D', 'XN--FZC2C9E2C', 'XN--GECRJ9C', 'XN--H2BRJ9C', 'XN--HXT814E', 'XN--I1B6B1A6A2E', 'XN--IMR513N', 'XN--IO0A7I', 'XN--J1AEF', 'XN--J1AMH', 'XN--J6W193G', 'XN--KCRX77D1X4A', 'XN--KPRW13D', 'XN--KPRY57D', 'XN--KPUT3I', 'XN--L1ACC', 'XN--LGBBAT1AD8J', 'XN--MGB9AWBF', 'XN--MGBA3A4F16A', 'XN--MGBAAM7A8H', 'XN--MGBAB2BD', 'XN--MGBAYH7GPA', 'XN--MGBBH1A71E', 'XN--MGBC0A9AZCG', 'XN--MGBERP4A5D4AR', 'XN--MGBPL2FH', 'XN--MGBX4CD0AB', 'XN--MK1BU44C', 'XN--MXTQ1M', 'XN--NGBC5AZD', 'XN--NODE', 'XN--NQV7F', 'XN--NQV7FS00EMA', 'XN--NYQY26A', 'XN--O3CW4H', 'XN--OGBPF8FL', 'XN--P1ACF', 'XN--P1AI', 'XN--PGBS0DH', 'XN--PSSY2U', 'XN--Q9JYB4C', 'XN--QCKA1PMC', 'XN--RHQV96G', 'XN--S9BRJ9C', 'XN--SES554G', 'XN--T60B56A', 'XN--TCKWE', 'XN--UNUP4Y', 'XN--VERMGENSBERATER-CTB', 'XN--VERMGENSBERATUNG-PWB', 'XN--VHQUV', 'XN--VUQ861B', 'XN--WGBH1C', 'XN--WGBL6A', 'XN--XHQ521B', 'XN--XKC2AL3HYE2A', 'XN--XKC2DL3A5EE0H', 'XN--Y9A3AQ', 'XN--YFRO4I67O', 'XN--YGBI2AMMX', 'XN--ZFR164B', 'XPERIA', 'XXX', 'XYZ', 'YACHTS', 'YANDEX', 'YE', 'YODOBASHI', 'YOGA', 'YOKOHAMA', 'YOUTUBE', 'YT', 'ZA', 'ZIP', 'ZM', 'ZONE', 'ZUERICH', 'ZW' ]         ##ok nevermind
    return False


if __name__ == "__main__":
    assert has_top_level_domain("www.google.com")
    assert not has_top_level_domain("www.google.ab")
    assert not has_top_level_domain("www.google.woooo")
    assert has_top_level_domain("www.google.abogado")
    print is_tip_top_level("http://www.google.com")

    print make_non_relative_link("https://www.google.com", "research")