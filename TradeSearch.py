import requests
import json
import webbrowser
import sys

#{"query":{"status":{"option":"online"},"stats":[{"type":"count","filters":[----filter ids here| {"id":"id name","value":{"min":x,"max":x},"disabled":false}, ----],"value":{"min":1}}]},"sort":{"price":"asc"}}
class TradeSearch:
    def __init__(self, seed, jewel_type_in):

        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                }

        vanity_ids = ["explicit.pseudo_timeless_jewel_xibaqua", "explicit.pseudo_timeless_jewel_zerphi", "explicit.pseudo_timeless_jewel_doryani", "explicit.pseudo_timeless_jewel_ahuana"]
        restraint_ids = ["explicit.pseudo_timeless_jewel_nasima", "explicit.pseudo_timeless_jewel_asenath", "explicit.pseudo_timeless_jewel_deshret", "explicit.pseudo_timeless_jewel_balbala"]
        hubris_ids = ["explicit.pseudo_timeless_jewel_chitus", "explicit.pseudo_timeless_jewel_victario", "explicit.pseudo_timeless_jewel_cadiro", "explicit.pseudo_timeless_jewel_caspiro"]
        pride_ids = ["explicit.pseudo_timeless_jewel_rakiata", "explicit.pseudo_timeless_jewel_kiloava", "explicit.pseudo_timeless_jewel_kaom", "explicit.pseudo_timeless_jewel_akoya"]
        faith_ids = ["explicit.pseudo_timeless_jewel_venarius", "explicit.pseudo_timeless_jewel_avarius", "explicit.pseudo_timeless_jewel_dominus", ]

        leaguename = "Standard"

        r = requests.get("http://api.pathofexile.com/leagues?type=main&offset=4&limit=1", headers=headers)
        if r.status_code == 200:
            leaguename = r.json()[0]['id']
            # print(f"found league name: {leaguename}")



        if "Elegant Hubris" in jewel_type_in:
            currentjewel_ids = hubris_ids
        if "Lethal Pride" in jewel_type_in:
            currentjewel_ids = pride_ids
        if "Militant Faith" in jewel_type_in:
            currentjewel_ids = faith_ids
        if "Glorious Vanity" in jewel_type_in:
            currentjewel_ids = vanity_ids
        if "Brutal Restraint" in jewel_type_in:
            currentjewel_ids = restraint_ids

        filterstring = ""

        jsonstringany = {"query":{"status":{"option":"any"},"stats":[{"type":"count","filters":[{"id":currentjewel_ids[3],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[0],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[1],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[2],"value":{"min":seed,"max":seed},"disabled":False}],"value":{"min":1}}]},"sort":{"price":"asc"}}
        jsonstringonline = {"query":{"status":{"option":"online"},"stats":[{"type":"count","filters":[{"id":currentjewel_ids[3],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[0],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[1],"value":{"min":seed,"max":seed},"disabled":False}, {"id":currentjewel_ids[2],"value":{"min":seed,"max":seed},"disabled":False}],"value":{"min":1}}]},"sort":{"price":"asc"}}


        ra = requests.post('https://www.pathofexile.com/api/trade/search/'+leaguename, json=jsonstringany, headers=headers)
        ro = requests.post('https://www.pathofexile.com/api/trade/search/'+leaguename, json=jsonstringonline, headers=headers)

        if ra.status_code == 200 :
            webbrowser.open_new(f"https://www.pathofexile.com/trade/search/{leaguename}/{ra.json()['id']}")
