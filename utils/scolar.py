from scholarly import scholarly


def scolar_search(query):

    pubs = scholarly.search_pubs(query)

    results = []
    count = 0
    for pub in pubs:

        results.append(
            {
                "title": pub["bib"]["title"],
                # "url": pub["bib"]["url"],
                "url": pub["pub_url"],
                "snippet": pub["bib"]["abstract"],
                "authors": pub["bib"]["author"],
                "year": pub["bib"]["pub_year"],
            }
        )
        count += 1
        if count == 10:
            break
    return results
