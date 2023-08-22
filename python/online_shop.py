import re

def cost_of_project(engraving, solid_gold):
    total_cost = 0
    
    if len(engraving) <= 0:
        return total_cost
   
    spaces_len = len(engraving.split(" "))
    # Define the base cost and cost per engraved unit for gold plated and solid gold rings
    base_cost_gold_plated = 50
    cost_per_engraved_unit_gold_plated = 7

    base_cost_solid_gold = 100
    cost_per_engraved_unit_solid_gold = 10

    # Find all occurrences of engraved units (including spaces and punctuation)
    engraved_units = re.findall(r'[^\w\s]', engraving)

    # Calculate the total number of engraved units (including spaces and punctuation)
    total_engraved_units = len(engraved_units) + spaces_len -1
    
    # Calculate the total cost based on the type of ring (gold plated or solid gold)
    if solid_gold:
        total_cost = base_cost_solid_gold + (cost_per_engraved_unit_solid_gold * total_engraved_units)
    else:
        total_cost = base_cost_gold_plated + (cost_per_engraved_unit_gold_plated * total_engraved_units)

    return total_cost

# Example usage:
engraving_text = ""
is_solid_gold = True
total_cost_of_project = cost_of_project(engraving_text, is_solid_gold)
print("Total cost of the project:", total_cost_of_project)
