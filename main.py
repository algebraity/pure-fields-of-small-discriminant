from sage.all import *
import json
from compute_invariants import *

def main(n=-1):
    if n == -1:
        n = int(input("Enter the number of fields to compare: "))
        while not (isinstance(n, int)) and not (n > 0):
            n = int(input("Input not accepted. Enter 0 for real and 1 for imaginary: "))

    invariants = compute_invariants(n)

    to_json(invariants, inv_spikes, 'invariants_data.json')

def to_json(invariants, inv_spikes, filename):
    print("Saving data to", filename)
    to_store = {}

    # Process the 'invariants' data
    if isinstance(invariants, dict):
        for field, invariants in invariants.items():
            field_info = {}

            # Store the invariants in a dictionary
            field_info['defining_polynomial'] = str(field.polynomial())

            # Store the invariants
            field_info['invariants'] = {        
                'dK': int(invariants[1]),   
                'hK': int(invariants[2]),       
                'fu': str(invariants[3]),   
                'rK': float(invariants[4]),
                'mb': float(invariants[5])      
            }

            # Store the field info under its corresponding key
            to_store[str(field)] = field_info

        fu_spikes = []
        for spike in inv_spikes:
            fu_spikes.append([int(spike[0]), str(real(spike[1]))])
        to_store["fu_spikes"] = fu_spikes

    # Save the structured data to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(to_store, json_file, indent=4)

#### MAIN FUNCTION CODE ####
if __name__ == "__main__":
    main()
