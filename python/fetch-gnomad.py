import os
import sys
import requests

# Fetch from public genomics databases
class GnomadGateway:
    def __init__(self):
            self.gnomad_api_base = "https://gnomad.broadinstitute.org/api"

    # Driver...
    def fetch(self, chrom, pos, ref, alt):
        if not chrom or not pos or not alt:
            print("Missing required gnomad data...")
            print(f"CHROM: {chrom}")
            print(f"POS: {pos}")
            print(f"REF: {ref}")
            print(f"ALT: {alt}")
            return None
        
        s = self.format_gnomad(chrom, pos, ref, alt)
        json = self.fetch_gnomad(s)
        if 'error' in json:
            print("Error in json...")
            print(json)
            return None
        return json

    # Create a request to gnomad API and return json response
    def fetch_gnomad(self, jsondata):
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.gnomad_api_base, json=jsondata, headers=headers)
        print(response)
        return response.json()
    
    # Returns a json blob with a graphql request
    def format_gnomad(self, chrom, pos, ref, alt):
        # https://gist.github.com/hliang/aad37d960adf42da16b3bad8677d7f19
        query = ''' 
        {{
            variant(variantId: "{chrom}-{pos}-{ref}-{alt}", dataset: gnomad_r2_1) {{
                variantId
                reference_genome
                chrom
                pos
                ref
                alt
                colocatedVariants
                sortedTranscriptConsequences {{
                transcript_id
                consequence_terms
                canonical
                major_consequence
                polyphen_prediction
                sift_prediction
                lof
                }}
            }}
        }}
        '''.format(chrom=chrom, pos=pos, ref=ref, alt=alt)

        json_data = {
            "query": query,
            "variables": {"withFriends": False}
        }

        return json_data



