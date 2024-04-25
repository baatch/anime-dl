# Anime-dl 動畫下載 [![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/rkwyu/anime-dl/main) [![Coverage Status](https://coveralls.io/repos/github/rkwyu/anime-dl/badge.svg?branch=main)](https://coveralls.io/github/rkwyu/anime-dl?branch=main)

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## About ##
A tool to get anime from different websites with [CLI (Command Line Interface)](#usage-cli) and [WebUI](#usage-webui).  
It currently supports following websites:  
- [x] [anime1.in](https://anime1.in/)  
- [x] [anime1.me](https://anime1.me/)  
- [x] [yhdm.one](https://yhdm.one/)  
- [x] [xgcartoon.com](https://www.xgcartoon.com/)
- [x] [lincartoon.com](https://www.lincartoon.com/)

Pending to supports:  
- [ ] [kickassanime.mx](https://www1.kickassanime.mx/)
- [ ] [iyinghua.io](http://www.iyinghua.io/)

## Prerequisites ##
To running this tool, please make sure the following prerequisites are ready:
- FFmpeg ([https://www.ffmpeg.org/](https://www.ffmpeg.org/))

## Setup ##
1. Download repository  
```console
git clone https://github.com/rkwyu/anime-dl
```
2. Install dependencies
```console
cd ./anime-dl
python -m pip install -r requirements.txt
```

## Usage (CLI) ##
```console
python run.py {URL}
```

#### Example ####
《Chainsaw Man Season 1》,  
- Series ([https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu](https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu))  
- Episode 1 ([https://www.xgcartoon.com/user/page_direct?cartoon_id=dianjurenriyu-tengbenshu&chapter_id=vRsDVLPPou](https://www.xgcartoon.com/user/page_direct?cartoon_id=dianjurenriyu-tengbenshu&chapter_id=vRsDVLPPou))  

Download all episodes:  
```console
python run.py https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu
```

Download episode 1:  
```console
python run.py https://www.xgcartoon.com/user/page_direct?cartoon_id=dianjurenriyu-tengbenshu&chapter_id=vRsDVLPPou
```

## Usage (WebUI) ##
```console
python webUI.py
```
After the logs are shown as below, go to [http://127.0.0.1:7860](http://127.0.0.1:7860)
```console
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```
![anime-al screenshot](docs/screenshot.png?raw=true "anime-al")


## License ##
[GNU GPL v3.0](LICENSE.md)
