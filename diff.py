def get_se(name, beta_base):
	print(beta_base)

def find_new_se(beta_base, airtable_base):
	# extraire des colonnes de la base
	# print(beta_base)
	# print(beta_base.loc[:, ["id", "name"]])

	# boucler dans la base 
	# for s in beta_base:
	#     print(s)
	# for id in beta_base["id"]:
		# print(id)

	for key in airtable_base["records"]:
		print(key["fields"]["Nom"])

	return ""

def find_changes(beta_base, airtable_base):
	# print(beta_base.loc[:, ["id", "name"]])
	melt = beta_base.melt('name')
	melt = melt.loc[melt['name'] == "Zam", 'value']
	print(melt)

	for key in airtable_base["records"]:
		# print(key["fields"])
		# print(key["fields"]["Nom"])
		return
		

		# update fields
		# key["fields"]["Nom2"] = key["fields"]["Nom"]



	return ""

