from flask_restplus import Namespace, fields, Model


class StudentSatusModel:
    api = Namespace(
        "Statut étudiant",
        description="Informations sur un étudiant et ses inscriptions académiques",
        path="/v2/etudiants",
    )
    status = api.model(
        "Etudiant",
        {
            "ine": fields.String(
                description="Identifiant unique de l'étudiant", example="1234567890G"
            ),
            "nom": fields.String(
                required=True, description="Le nom de naissance", example="Moustaki"
            ),
            "prenom": fields.String(
                required=True, description="Le prénom", example="Georges", max_length=13
            ),
            "dateNaissance": fields.DateTime(
                required=True,
                description="La date de naissance",
                example="1992-11-29T00:00:00",
            ),
            "inscriptions": fields.List(
                fields.Nested(
                    api.model(
                        "Inscription",
                        {
                            "dateDebutInscription": fields.DateTime(
                                required=True,
                                description="La date de début d'inscription à l'établissement",
                                example="2019-09-01T00:00:00",
                            ),
                            "dateFinInscription": fields.DateTime(
                                required=True,
                                description="La date de fin d'inscription à l'établissement",
                                example="2020-06-29T00:00:00",
                            ),
                            "statut": fields.String(
                                required=True,
                                attribute="statut",
                                description="Le statut de l'inscription",
                                example="admis",
                                enum=["admis", "inscrit"],
                            ),
                            "regime": fields.String(
                                required=True,
                                attribute="regime",
                                description="Le régime de formation",
                                example="formation initiale",
                                enum=["formation initiale", "formation continue"],
                            ),
                            "codeCommune": fields.String(
                                required=True,
                                attribute="codeCommune",
                                description="Le code commune",
                                example="29085",
                            ),
                            "etablissement": fields.Nested(
                                api.model(
                                    "Établissement",
                                    {
                                        "uai": fields.String(
                                            required=True,
                                            attribute="uai",
                                            description="Identifiant unique de l'établissement",
                                            example="0011402U",
                                        ),
                                        "nom": fields.String(
                                            required=True,
                                            attribute="nom",
                                            description="Nom de l'établissement",
                                            example="EGC AIN BOURG EN BRESSE EC GESTION ET COMMERCE (01000)",
                                        ),
                                    },
                                )
                            ),
                        },
                    )
                )
            ),
        },
    )


parser = StudentSatusModel.api.parser()
parser.add_argument(
    "ine", type=str, location="args", required=True,
)
