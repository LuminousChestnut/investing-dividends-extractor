# investing-dividends-extractor
## 0. Git clone / download the 3 files into the same folder.
## 1. Change the param of Forge.py
If you want to extract different periods, you can just change the param of _Forge.py_.
This Week:

```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__('**-7**')
pro_data = idr.__init__(raw_data)
```

Next Week:
```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__('**7**')
pro_data = idr.__init__(raw_data)
```

Today:
```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__('**0**')
pro_data = idr.__init__(raw_data)
```
Yesterday:

```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__('**-1**')
pro_data = idr.__init__(raw_data)
```

Tomorrow:
```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__('**1**')
pro_data = idr.__init__(raw_data)
```

Option Period:
```
import Investing_Dividends_Downloader as idd
import Investing_Dividends_Reader as idr
raw_data = idd.__init__(**'o', start_date='01/31/2024', end_date='09/01/2024'**)
pro_data = idr.__init__(raw_data)
```

## 2. Run **Forge.py**
