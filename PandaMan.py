import pandas as pd
food_info= pd.read_csv('Datafiles/food_info.csv')
col_names=food_info.columns.tolist()
#print(col_names)
#print(food_info.head(3))

sodium_grams=food_info["Sodium_(mg)"] / 1000
sugar_milligrams= food_info["Sugar_Tot_(g)"] * 1000
print(sugar_milligrams[0:5])

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"]/food_info["Water_(g)"] 
print(grams_of_protein_per_gram_of_water[0:5])

milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"]+food_info["Iron_(mg)"] 
print(milligrams_of_calcium_and_iron[0:5])


weighted_protein=food_info["Protein_(g)"]*2
weighted_fat=-0.75*food_info["Lipid_Tot_(g)"]
initial_rating=weighted_protein+weighted_fat
print(initial_rating[0:5])


normalized_protein=(food_info["Protein_(g)"]-food_info["Protein_(g)"].min())/(food_info["Protein_(g)"].max()-food_info["Protein_(g)"].min())
normalized_fat=(food_info["Lipid_Tot_(g)"]-food_info["Lipid_Tot_(g)"].min())/(food_info["Lipid_Tot_(g)"].max()-food_info["Lipid_Tot_(g)"].min())
print(normalized_protein[0:5])
print(normalized_fat[0:5])


food_info["Normalized_Protein"]=normalized_protein
food_info["Normalized_Fat"]=normalized_fat
#print(food_info.head(3))

Norm_Nutr_Index= 2* food_info["Normalized_Protein"] -0.75*food_info["Normalized_Fat"]
print(Norm_Nutr_Index[0:5])

food_info["Norm_Nutr_Index"]=Norm_Nutr_Index
food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)
print(food_info.head(5))


