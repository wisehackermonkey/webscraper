# webscraper:  simple script that scrapes top 1 million websites
#
# Copyright (C) wisehackermonkey
#
# This file is part of webscraper.
#
# webscraper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# webscraper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with webscraper. If not, see <http://www.gnu.org/licenses/>.
#
#
# @author = 'wisehackermonkey'
# @email = 'oranbusiness@gmail.com'

import requests

class webscraper:
    def __init__(self):
        self._url = 1


    @property
    def url(self):
        """
        I am a getter.


        """

        return self._url

if __name__ == "__main__":
    print("webscriaping started")

    print(requests.get("http://www.example.com").text)