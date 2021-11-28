import requests
import json
import os
from .Utils.ClassUtils import UniversalRandomizer


class SomeRandomApi:

    def __init__(self, APIOptions: dict = None):
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Constants', 'Caches.json')), 'r') as JsonCacheFile:
            self.CacheJsonData = json.load(JsonCacheFile)
        self.BaseUrl = self.CacheJsonData["BaseUrls"]["SomeRandomApi"]
        self.APIOptions = APIOptions

    def raw(self, APIOptions: dict):
        if not APIOptions and not self.APIOptions:
            raise RuntimeError(
                "API-Options are Null/None for API Fetch Request")
        elif not APIOptions:
            APIOptions = self.APIOptions

        RequestUrl = self.BaseUrl + '/' + \
            self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower().lower()]["name"] + '/' + \
            self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()
                                                                            ]["endpoint"][APIOptions['endpoint'].lower().lower()]
        rawResponse = None
        JsonResponse = None
        if APIOptions and "parameters" in APIOptions and "parameters" in self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()] and self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["parameters"]:
            for param in self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["parameters"]:
                if self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["parameters"][param] and not APIOptions[param]:
                    raise RuntimeError(
                        param + " is Required by SomeRandomApi on Url -> " + RequestUrl)
            rawResponse = requests.get(
                RequestUrl, params=APIOptions["parameters"])
        else:
            rawResponse = requests.get(RequestUrl)
        if not rawResponse or rawResponse.status_code != 200:
            raise RuntimeError(
                "Invalid Response is Detected by API -> " + RequestUrl)
        elif not self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["ignoreResponse"]:
            try:
                JsonResponse = json.loads(rawResponse.text)
            except:
                JsonResponse = None
        return {"json": JsonResponse, "rawData": rawResponse, "url": rawResponse.url}

    def fetch(self, APIOptions: dict):
        if not APIOptions and not self.APIOptions:
            raise RuntimeError(
                "API-Options are Null/None for API Fetch Request")
        elif not APIOptions:
            APIOptions = self.APIOptions
        RawOutput = self.raw(APIOptions)
        if RawOutput and "json" in RawOutput and RawOutput["json"] and APIOptions and "filters" in APIOptions and (type(APIOptions['filters']) is list or type(APIOptions['filters']) is tuple) and "filters" in self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()] and self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["filters"]:
            FetchOutput = {}
            for filter in APIOptions['filters']:
                if filter.lower() in self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"][APIOptions['category'].lower()]["filters"]:
                    FetchOutput[filter] = RawOutput['json'][filter]
            return FetchOutput
        elif "json" not in RawOutput and "url" in RawOutput:
            return RawOutput['url']
        elif "json" in RawOutput:
            return RawOutput['json']
        else:
            return RawOutput['rawData']

    def random(self, APIOptions: dict):
        if not APIOptions and not self.APIOptions:
            raise RuntimeError(
                "API-Options are Null/None for API Fetch Request")
        elif not APIOptions:
            APIOptions = self.APIOptions
        if APIOptions and "category" not in APIOptions:
            APIOptions["category"] = UniversalRandomizer(
                self.CacheJsonData["OptionCaches"]["SomeRandomApi"]["category"])
        RandomCategoryCache = self.CacheJsonData["OptionCaches"][
            "SomeRandomApi"]["category"][APIOptions["category"].lower()]
        if APIOptions and "endpoint" not in APIOptions:
            APIOptions["endpoint"] = UniversalRandomizer(
                RandomCategoryCache["endpoint"])
        return self.fetch(APIOptions)
