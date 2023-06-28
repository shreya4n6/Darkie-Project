# DARKie
DARKie is a command line tool for searching any keyword in dark web using supported search engines.
```
PS C:\Users\akash\Documents\GitHub\DARKie\src> python darkie.py -k drugs -a -f op.csv

     _____               __ _    __   _
    |  _  \      /\      ||  \   ||  //         _____
    | | | |     //\\     ||__/   || //   _o_   /_____\
    | | | /    //  \\    ||\\    |||     | |  //_____/
    | |/ /    //____\\   || \\   || \\   | |  \______
    |___/    //      \\  ||  \\  ||  \\  |_|   \_____|

    Developer: Shreya T
    Version: 1.0



[>] Checking for tor service ...

'systemctl' is not recognized as an internal or external command,
operable program or batch file.
[>] Tor Service is Running...

Searching in 'ahmia'.
Found 1000 onion links.
Searching for ahmia done!

Found 1020 onion links.
Searching for onionland done!

Searching in 'excavator'.
Found 1040 onion links.
Searching for excavator done!

Searching in 'onionengine'.
Found 1086 onion links.
Searching for onionengine done!

Searching in 'venus'.
Found 1086 onion links.
Searching for venus done!

Writing onion links to :  op.csv

Writing done :  op.csv
```

### Setup and Installation
1. Download and install python.
2. Download the required python packages.
3. Download/Clone this repository.
4. Open terminal/cmd and change directory to [DARKie/src](https://github.com/shreya4n6/DARKie/tree/main/src) and run the command `python darkie.py -k drugs -f op.csv`.

### Supported Search Engines
- ahmia
- onionland
- excavator
- onionengine
- venus

### Features
You can check the available command line options by running the command `python darkie.py -h`.
```
usage: darkie.py [-h] -k  [-e] [-a] -f

Darkie Search Control

optional arguments:
  -h, --help        show this help message and exit
  -k , --keyword    Search Keyword
  -e , --engine     Search engine name (Available search engines : ahmia, onionland, excavator, onionengine, venus)
  -a, --all         Search using all available engine(s)
  -f , --filepath   Save onion urls in given filepath
```
  
### Some Example Commands
#### Search keyword "drugs" in default search engine (default = "ahmia") and save the results in "op.csv":
```
python darkie.py -k drugs -f op.csv
```

#### Search keyword "drugs" in default search engine (default = "ahmia") and save the results in "op.txt":
```
python darkie.py -k drugs -f op.txt
```

#### Search keyword "redline stealer" in default search engine (default = "ahmia") and save the results in "op.csv":
```
python darkie.py -k "redline stealer" -f op.csv
```

#### Search keyword "drugs" in given search engine "ahmia" and save the results in "op.csv":
```
python darkie.py -k drugs -e ahmia -f op.csv
```

#### Search keyword "drugs" in given search engine "onionland" and save the results in "op.csv":
```
python darkie.py -k drugs -e onionland -f op.csv
```

#### Search keyword "drugs" in given search engine "excavator" and save the results in "op.txt":
```
python darkie.py -k drugs -e excavator -f op.txt
```

#### Search keyword "drugs" in given search engines "ahmia", "onionland", "excavator" and save the results in "op.csv":
```
python darkie.py -k drugs -e ahmia onionland excavator -f op.csv
```

#### Search keyword "drugs" in all available search engines (ahmia, onionland, excavator, onionengine, venus) and save the results in "op.csv":
```
python darkie.py -k drugs -a -f op.csv
```
