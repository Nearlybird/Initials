def get_country_codes(prices):
    c_codes = ""
    new_prices = prices.split()
    for code in new_prices:
        new_code = code[:2]
        c_codes += new_code+", "
    c_codes = c_codes[:-2]    
    return(c_codes)

# some tests to check your work. You shouldn't modify these.
from test import testEqual

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")
