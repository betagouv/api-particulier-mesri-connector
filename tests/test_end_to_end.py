def test_api_call_not_found(client):
    response = client.get("/v2/etudiants?ine=yolo")

    assert response.status_code == 404


def test_api_call(client):
    response = client.get("/v2/etudiants?ine=0906018155T")

    assert response.status_code == 200
    assert response.json == {
        "ine": "0906018155T",
        "nom": "Dupont",
        "prenom": "Gaëtan",
        "dateNaissance": "1999-10-12T00:00:00",
        "inscriptions": [
            {
                "dateDebutInscription": "2019-09-01T00:00:00",
                "dateFinInscription": "2020-08-31T00:00:00",
                "statut": "admis",
                "regime": "formation initiale",
                "codeCommune": "44000",
                "etablissement": {
                    "uai": "0011402U",
                    "nom": "EGC AIN BOURG EN BRESSE EC GESTION ET COMMERCE (01000)",
                },
            }
        ],
    }
