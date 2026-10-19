# COPPA Compliance Requirements Reference — 16 CFR Part 312

## Covered Operators
Operators of commercial websites or online services directed to children under 13, or operators with actual knowledge that they collect personal information from children under 13.

## Definition of Personal Information (16 CFR 312.2)
Personal information includes:
- First and last name
- Home or physical address
- Online contact information (email address)
- Screen or user name that functions as online contact information
- Telephone number
- Social security number
- **A persistent identifier** that can be used to recognize a user over time and across different websites or online services, including but not limited to: **a cookie number, an IP address, a processor or device serial number, or a unique device identifier**
- **Geolocation information** sufficient to identify street name and name of city or town
- Photograph, video, or audio file containing a child's image or voice
- Information concerning the child or the parents combined with any of the above identifiers

## Verifiable Parental Consent Requirements (16 CFR 312.5)
Operators must obtain verifiable parental consent before:
- Collecting personal information from children under 13
- Using or disclosing personal information collected from children
- Making personal information publicly available

## Site Directed to Children (16 CFR 312.2)
A website or online service is directed to children if:
- The subject matter, visual content, music, animated characters, celebrities, or other features suggest it is directed to children under 13
- The operator has actual knowledge that it is collecting personal information from users under 13

## Audit Scope
This audit covers all three data-collection flows of the platform:
1. Account creation records (name, email) — `data_category: account_pii`
2. In-app purchase history — `data_category: account_pii`
3. Device identifiers and geolocation — `data_category: device_analytics`

All three flows must be evaluated for consent coverage across the full under-13 user population.
