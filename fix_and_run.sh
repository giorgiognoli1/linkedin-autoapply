#!/bin/bash

# Fix search.py - NESSUN filtro
cat > config/search.py << 'SEARCH'
search_terms = ["Salesforce Director", "CRM Director"]
search_location = ""
switch_number = 30
randomize_search_order = False
sort_by = ""
date_posted = ""
salary = ""
easy_apply_only = True
experience_level = []
job_type = []
on_site = []
companies = []
location = []
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []
under_10_applicants = False
in_your_network = False
fair_chance_employer = False
pause_after_filters = False
about_company_bad_words = []
about_company_good_words = []
bad_words = []
security_clearance = False
did_masters = True
current_experience = 15
SEARCH

# Verifica che secrets.py abbia le credenziali
grep -q "giorgiognoli@gmail.com" config/secrets.py && echo "✓ Credenziali OK" || echo "✗ Credenziali mancanti"

# Lancia bot
python3 runAiBot.py
