# _Greenhouse.io Date Posted Scraper_

<div align="center">
    <!-- Project Shields -->
    <div align="center">
        <a href="https://github.com/MarcusKyung/greenhouse.io-scraper/graphs/contributors">
            <img src="https://img.shields.io/github/contributors/MarcusKyung/greenhouse.io-scraper.svg?style=plastic">
        </a>
        ¨
        <a href="https://github.com/MarcusKyung/greenhouse.io-scraper/stargazers">
            <img src="https://img.shields.io/github/stars/MarcusKyung/greenhouse.io-scraper.svg?color=yellow&style=plastic">
        </a>
        ¨
        <a href="https://github.com/MarcusKyung/greenhouse.io-scraper/issues">
            <img src="https://img.shields.io/github/issues/MarcusKyung/greenhouse.io-scraper?style=plastic">
        </a>
        ¨
        <a href="https://github.com/MarcusKyung/greenhouse.io-scraper/blob/main/license.txt">
            <img src="https://img.shields.io/github/license/MarcusKyung/greenhouse.io-scraper?color=orange&style=plastic">
        </a>
        ¨
        <a href="https://linkedin.com/in/MarcusKyung">
            <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=plastic&logo=linkedin&colorB=2867B2">
        </a>
    </div>
</div>

#### By _**Marcus Kyung**_

## Contents:

- [Technologies Used](#technologies-used)
- [Description](#description)
- [Setup & installation](#setupinstallation-requirements)
- [Known Bugs](#known-bugs)
- [License](#license)

## Technologies Used:

- _Python_
- _Selenium_

## Description:
Scrapes Greenhouse.io job careers pages and prints the date the job was posted. Examples:
- https://boards.greenhouse.io/kallesgroup
- https://boards.greenhouse.io/energysolutions
- https://boards.greenhouse.io/arcadiacareers
- https://boards.greenhouse.io/harrys
- https://boards.greenhouse.io/1800contacts
- https://boards.greenhouse.io/archrival
- https://boards.greenhouse.io/colehourcoheninc/


## Setup/Installation Requirements:
### Run Locally:
1. Clone this repository to a local machine with Python. Install Selenium
2. Input Greenhouse.io careers page you wish to scrape. Must be a https://boards.greenhouse.io/XYZ careers page. Cannot be custom or embedded job listings
3. Run using terminal

## Known Bugs:
- Script doesn't work on employer site embedded greenhouse.io pages like this one: https://www.airship.com/company/careers/
- Script doesn't work on non-standard greenhouse.io page like this one: https://boards.greenhouse.io/alma because the job title is formatted in a non-standard method
- Minimal error handling

## Contact:
_For questions, comments, or concerns please reach out at Kyungmj@gmail.com_

## MIT License & Copywrite:
Copyright (c) [2023] [Marcus Kyung]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR\ A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.