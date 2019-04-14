# nameSearch
Given 300k docs, implement search using python and flask web service

# doc relevance criteria
Scoring is done based on the following rules:

	if first name matches the given query: 200
	if last name matches the given query: 100	
	if middle name matches the given query: 50
	if first name starts with given query: 30
	if last name starts with given query: 20
	if middle name starts with given query: 10

