# Searchstring generator for Pokemon Go

This script generates a Searchstring based on your  [Pokedextracker](https://pokedextracker.com/) 
info. 

If you have never used Pokedextracker, here is what the demo account looks like.
[demouser: ashketchum10](https://pokedextracker.com/u/ashketchum10/)

The basic idea is, that you can keep a list of caught/uncaugt Pokemon on Pokedextracker and then 
use that list in order to generate a Searchstring, which can be copied into Pokemon Go in order to 
instantly see which pokemon you need from each other.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for 
development and testing purposes.

### Prerequisites

#### Python 3.7

> Should work with other versions, but has not been tested.

```powershell
choco install python
```

#### lxml

```powershell
pip install lxml
```

#### selenium

```powershell
pip install selenium
```

#### GoogleChrome

> can also work with other broweser but requires tweaking.

```powershell
choco install googlechrome
```

#### ChromeDriver

Download the ChromeDriver binary for your platform under the 
[downloads](http://chromedriver.chromium.org/downloads) section of this site.

The exe must be added to your `%PATH%` variable.

It may be possible tho install chromedriver with chocolatey, but it has not beent tested.

```powershell
choco install chromedriver
```
### Installing

Clone the project

```powershell
git clone https://github.com/Gi0m/searchstring 
```

Change into the repo

```powershell
cd searchstring
```

Edit the `url` variable in `searchstring.py` to your pokedex with the text editor of your liking or 
run the script with the default/demo user.

You can also edit the `latestPkmn` variable if you wish to limit add newer generations or remove 
them.

To run the script in terminal simply type:

```powershell
python searchstring.py
```

The default pokedex then outputs the list of uncaught pokemon.

```
Fetching your list of uncaught pokemon

DevTools listening on ws://127.0.0.1:50109/devtools/browser/5d9b89d0-4cf6-4bc9-888c-20c3129a9c54


002,003,004,005,008,009,010,011,013,014,016,017,019,021,022,023,024,026,027,028,029,030,031,032,033,034,035,036,037,038,039,040,041,042,043,044,045,046,047,048,049,050,051,052,053,054,055,056,058,059,060,061,062,063,064,065,066,067,068,069,070,071,072,073,074,075,076,077,078,079,080,081,082,083,084,085,086,087,088,090,091,092,093,094,095,096,097,098,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,154,155,157,159,160,161,162,163,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,390,391,393,394,395,396,397,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494
```

## Acknowledgments

* Raphi, thanks for the help with XPath
