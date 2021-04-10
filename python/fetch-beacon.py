import os
import sys
import requests

# Fetch from public genomics databases
class BeaconGateway:
    def __init__(self):
        self.beacon_api_base = "http://cancer.sanger.ac.uk/api/ga4gh/beacon"

    # Driver...
    def fetch(self, chrom, pos, allele):
        if not chrom or not pos or not allele:
            print("Missing required beacon data...")
            print(f"CHROM: {chrom}")
            print(f"POS: {pos}")
            print(f"ALLELE: {allele}")
            return None
        
        s = self.format_beacon(chrom, pos, allele)
        json = self.fetch_beacon(s)
        if 'error' in json:
            print("Error in json...")
            print(json)
            return None

        if json == None:
            return None

        return json

    # Parse exists keyword
    def parse_beacon(self, json):
        try:
            return json['response']['exists']
        except:
            return None

    # Create a request to COSMIC Beacon and return json response
    def fetch_beacon(self, url):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, headers=headers)
            return response.json()
        except Exception as e:
            print("Exception in beacon fetch...")
            print(e)
            return None
    
    # Returns a formatted request as a string
    def format_beacon(self, chrom, pos, allele, ref="37", res="json"):
        # Query Parameters
        #     Required:
        #         chrom
        #             Chromosome name - either 1-22, X or Y
        #         pos
        #             1-based position - a positive integer (not greater than length of chromosome)
        #         allele
        #             Mutant Allele - 'A', 'C', 'G', 'T', 'I' (insertion) or 'D' (deletion)
        #     Optional:
        #         ref
        #             Genome Assembly - GRCh38 (default), or GRCh37
        #         dataset
        #             Data Source - cosmic (default) or cell_lines (Cell Lines Project)
        #         format
        #             Data Format - text (default), json or xml
        #
        # For programmatic access to the COSMIC beacon, the minimal URL for the request is: 
        #    http://cancer.sanger.ac.uk/api/ga4gh/beacon/query?chrom=?;pos=?;allele=?
        return f"{self.beacon_api_base}?allele={allele}&chrom={chrom}&pos={pos}&ref={ref}&format={res}"



