from flask import current_app
import requests


def get_student(id):
    (base_url, api_key) = _get_credentials()

    payload = {"filterByFormula": "{{ine}} = '{}'".format(id)}
    headers = {"Authorization": "Bearer {}".format(api_key)}

    r = requests.get(
        "{}/%C3%89tudiants".format(base_url), params=payload, headers=headers
    )

    response_content = r.json()

    if len(response_content["records"]) == 0:
        return None

    record = response_content["records"][0]["fields"]

    student = {
        "ine": record.get("ine"),
        "nom": record.get("nom"),
        "prenom": record.get("prenom"),
        "dateNaissance": record.get("dateNaissance"),
        "inscriptions": [],
    }

    for inscription_id in record["inscriptions"]:
        headers = {"Authorization": "Bearer {}".format(api_key)}
        r = requests.get(
            "{}/Inscriptions/{}".format(base_url, inscription_id), headers=headers
        )

        response_content = r.json()
        record = response_content["fields"]
        student["inscriptions"].append(
            {
                "dateDebutInscription": record.get("dateDebutInscription"),
                "dateFinInscription": record.get("dateFinInscription"),
                "statut": record.get("statut"),
                "regime": record.get("regime"),
                "codeCommune": record.get("codeCommune"),
                "etablissement": {
                    "uai": record.get("uaiEtablissement"),
                    "nom": record.get("nomEtablissement"),
                },
            }
        )

    return student


def _get_credentials():
    return (
        current_app.config["AIRTABLE_API_URL"],
        current_app.config["AIRTABLE_API_KEY"],
    )
