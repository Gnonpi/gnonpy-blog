Title: PyConFr 2018
Slug: pyconfr-2018
Date: 2018-10-10T19:29:43+02:00
Category: News
Status: published

Je suis allé a la PyConFr ces 4 derniers jours.
Histoire de garder une trace, je vais essayer de résumer un peu ce que j'y ai fait, ce que j'ai vu.

## Sprint: Anyblok

J'ai d'abord commencé en participant aux journées de sprint, le jeudi et le vendredi.
L'objectif pour moi était de voir comment travaillent les gens de l'open-source,
quels outils, quelle organisation, etc...
et aussi un peu d'aider si je pouvais, bien sûr.

J'ai fait un premier tour des équipes et je suis resté sur [Anyblok](github.com/AnyBlok)
(il y avait d'autres projets intéressants, comme Kivy ou Ansible).
Anyblok est un projet open-source (license Mozilla) soutenu par une entreprise, [Anybox](anybox.fr).

### Anybox

Je commence d'abord par l'entreprise, avant de passer sur le projet.
C'est une boîte atypique:
c'est une entreprise libérée suivant un systeme holacratique
dont tous les employés travaillent a distance.
Une entreprise libérée signifie que le pouvoir est directement repassé aux employés,
ceux qui possèdent le savoir technique.
Il y a une idée importante d'égalité et de liberté.
Je vous renvoie vers ce Ted Talk où c'est bien mieux expliqué
([vidéo sur youtube](https://www.youtube.com/watch?v=9oZUMzQDaw8)).
Il y aussi une excellente BD qui retrace l'histoire du mouvement
et ce que cela signifie d'être 'libéré'
([lien sens critique](https://www.senscritique.com/bd/Les_Entreprises_liberees/24819573)).
Même cela ne m'a pas impacté lors des jours de sprint,
je pense que cela impacte beaucoup la vie des gens de Anybox
et donc sur le projet Anyblok.

### Anyblok

Le projet maintenant.
**Anyblok** sert a créér des applications métiers en assemblant des **bloks** a la volée.

Un exemple concret, je suis dans l'administration d'une petite entreprise.
J'ai besoin de suivre ma comptabilité, je charge le blok correspondant.
Si demain, je veux aussi suivre mes employés ou la gestion de mon stock
de marchandise, je peux aller chercher les bloks correspondants et les intégrer dans mon systeme,
sans avoir à le redémarrer ou a appliquer des migrations compliquées.
Si je veux faire quelque chose de plus compliqué ou de specialisé pour mon domaine,
je peux aussi le faire a la volée en surchargeant les bloks déjà existants via héritage.
Mais, j'ai une base solide pour mes changements via les bloks officiels.

Sous le capot, Anyblok repose sur **SQLAlchemy** pour représenter ses objets dans une base de données.
Le framework expose une classe appelée **Registry** de laquelle on peut accéder a toutes les infos dont on a besoin.
Pour l'instant, le seul framework web supporté est **Pyramid** et la seule base de données est **PostgreSQL**.
Cependant, via le système de blok, d'autres framework peuvent être intégrés et via la configuration de SQLAlchemy,
d'autres bases de données peuvent être utilisées.

Ce que j'ai fait sur le projet tient en quelques lignes:
* apprendre ce qu'est Anyblok, les problèmes qu'il résout, les enjeux
* corriger certaines fautes d'anglais dans le [book](https://github.com/AnyBlok/anyblok-book), le manuel d'Anyblok
* aider à passer Anyblok de Nosetests vers Pytest
* tester si le framework fonctionnait avec une base **MySQL** sans changements dans le code
(pour l'instant, pas encore)

### Nose to Pytest

Le point sur lequel j'ai passé le plus de temps était d'aider
à passer les tests de NoseTest vers Pytest.

Pourquoi? Plusieurs raisons (voir aussi les [slides](https://speakerdeck.com/lothiraldan/une-revolution-dans-le-monde-des-tests) de l'auteur de Balto),
mais notamment que Nose n'est plus actif
depuis 2015 et que Pytest possède tout un ecosystème de plugins, dont notamment un qui introduit de la couleur
ou un autre qui permet de lancer ses tests en parallèle.

Mais au final, Nose et Pytest fonctionne sur la même base: unitTest,
le framework de test par défaut de Python.
Donc, au premier essai juste en remplaçant la commande `nose` par `pytest`, environ 70% des tests n'étaient pas cassés,
ce qui était déjà un petit succès.
Les tests cassés l'étaient à cause de la manière de réinitialiser ou rollbacker la base de données
utilisée durant les tests.
Ensuite, le but du jeu était de migrer un maximum de tests de la forme nose vers la forme pytest
(`self.assertEqual` vers `assert True`)
et d'utiliser à fond les features de pytest.

Quelque chose qui nous a beaucoup plu a été le fait d'utiliser les *fixtures* de pytest
pour faire de l'injection de dépendance et réutiliser des structures de données
coûteuses à créér entre différents tests.
Cela a permis de réduire de beaucoup la durée de run des tests
(à la fin du sprint, on était passé de 25min à environ 17-18min,
à confirmer par l'équipe Anyblok).

J'utilisais déjà pytest au travail,
mais devoir le réexpliquer, me replonger dans la doc et surtout,
devoir trouver comment faire que le projet en tire le meilleur avantage
m'a permis de beaucoup apprendre.

Un **merci particulier aux gens de Anybox**
qui m'ont guidés et avec qui j'ai passé de bons moments.

## Les conférences

Voici les conférences auxquelles j'ai assisté:

| nº | Langue | Nom | Présentateur |
| ---- | ---- | ---- | ---- |
| 1 |  En | Keynote: Science et Opensource | Viviane Pons |
| 2 |  En | Metric-learn: scikit-extension | William de Vazelhes |
| 3 |  Fr | Trio asynchrone | Emmanuel Leblond |
| 4 |  Fr | Dites au revoir au 'quick & dirty' | Antonin Morel |
| 5 |  Fr | Révolution dans le monde des tests | Boris Feld |
| 7 |  Fr | Anyblok | Franck Bret & Georges Racinet |
| 8 |  Fr | Hypothesis | Thierry Chapuis |
| 9 |  Fr  | Crypto pour les devs  | Matthias Dugué |
| 10 |  Fr | Maintenir un code lisible | Sébastien Corbin |
| 11 |  En | Keynote: Consensus dans la communauté Python | Julien Palard |
| 12 |  En | Data-science in the e-commerce | Pietro Fodra |
| 13 |  En | Containers for devs | Sami Makki & Vincent Maillol |
| 14 |  Fr | Micro-services with Kubernetes | Michael Bright |
| 15 |  Fr | **Keynote: Contributing to CPython** | **Victor Stinner** |
| 16 |  En | Python in data-communities | Alexys Jacob |
| 17 |  En | Pythonic monads | Vincent Perez |
| 18 |  Fr | La cartographie: simple mais compliqué | Julien Tayon |

Premiere remarque:
beaucoup étaient en anglais.
Si c'est génial sur un plan d'ouverture au monde
d'utiliser la lingua franca de l'informatique,
il n'empêche que certains speakers ne la maîtrisaient pas suffisamment pour
pouvoir donner une présentation fluide et agréable à écouter.
Pas la majorité, pas inintelligible
mais pas top non plus.
Mais je suis très mauvais public doublé d'un immense connard,
à voir le ressenti d'autres participants.

Deuxieme remarque:
j'ai essayé de ne pas aller que aux talks de data et de tests,
mais de m'ouvrir à des sujets qui ne me touchent pas de prime abord.
Au pire, toutes les presentations étaient filmées et retranscrites en direct
(gros big-up aux orgas pour ça) et seront sûrement bientôt sur Youtube ou autre plateforme.

Je vais essayer d'écrire un peu des points que j'ai trouvé intéressants dans les conférences:

*nº1* : très bonne ouverture,
l'oratrice a donné toutes les bonnes raisons de faire de l'open-source en science.
Cela m'a fait pense à un ami chimiste qui justement avait des problèmes pour faire marcher ses logiciels.

*nº2* : je m'attendais plus à quelque chose centré sur l'integration avec scikit-learn,
cela dit je garderai les techniques evoquées, je pense pouvoir les réutiliser.

*nº3* : j'avais lu la doc de Trio, j'avais fait des essais,
mais je pense que je ne l'avais même pas utilisé à 10% de ses capacités.
ça a relancé mon intérêt pour l'asynchrone en Python.
Il faut vraiment que je m'y plonge sérieusement.

*nº4* : présentation très intéressante, mais c'était des techniques
que je connaissais déjà.

*nº5* : présentation de Balto et de LIPF, le format d'échange d'informations de tests,
je pense jouer avec dans mon temps libre.

*nº7* : présentation de Anyblok sur lequel j'ai contribué durant les sprints.
Avoir une vision plus globale et plus "commerciale" m'a plu,
même si je sais que je ne vais pas l'utiliser.

*nº8* : un orateur avec une aisance super naturelle, une présence surprenante.
Les questions ont quelque peu scellé mon avis sur Hypothesis:
il n'est pas adapté a tester du code comme on en a l'habitude
(une entrée données doit fournir une sortie donnée suivant des règles et interactions logiques)
et force a re-implementer du code dans le testcase ou
à tester des comportements incomplets.

*nº9* : super intéressant, pas vraiment axé sur les maths, mais plutôt sur comment
appliquer la cryptographie pour protéger ses données en pratique et pourquoi.

*nº10* : très axé sur les linter et le codestyle

*nº11* : une étude à partir des repos pypi plus github des pratiques de dev.
Je suis pas sur que pratiques communes = bonnes pratiques mais ça vaut le coup de les connaître.
Je reviendrai un jour sur les slides.

*nº13* : deux personnes venaient présenter leur wrapper autour de divers outils Docker,
nommé ` pkr`, je n'ai tout à fait compris en quoi c'était une amélioration mais ça m'intéresse,
il faudrait que je relise la documentation et les use-cases.

*nº14* : (l'orateur ne parlait pas fort et le micro ne marchait pas, je n'ai pas tout suivi)

*nº15* : Un des points forts de cette PyConFr. **Victor Stinner** est un core dev de Python,
le seul à temps plein dans le monde.
Il a commencé par nous expliquer comment cela pesait sur un maintainer de continuer
à améliorer le langage, surtout sur son temps libre et au détriment de sa vie familiale, personnelle, sociale...
Il a ensuite parlé de la toxicité au sein des communautés,
j'ai appris que c'était lui qui avait remplacé les termes 'master' et 'slaves',
déclenchant la vague de polémique.
Au final, le fond de l'affaire est juste que des journaux ont repris une info sans la vérifier
et en l'amplifiant mille fois.
Il a poursuivi en parlant du problème de la diversité, de
comment il faut ouvrir Python au monde.
Un programme de mentorat pour former plus de core dev est en cours et semble bien fonctionner.
Ce gars a vraiment réussi à inspirer son auditoire et
m'a personnellement fait réaliser à quel point,
Python est une communaute de passionné qui peuvent changer le monde.
*\ Inserer ici citation motivationnelle type instagram \*

*nº16* : cette présentation m'a assez surpris,
la vision de l'orateur Alexys Jacob est complète, élégante et me semble proche de la 'réalité terrain'.
J'ai reproduis son diagramme et pense de le faire circuler
au bureau, c'est vraiment complet.

*nº17* : je n'ai pas tellement aimé cette façon de présenter les monades,
qui au final ressemblait plus à du hack que l'on pourrait remplacer
par une meilleure abstraction objet.

*nº18* : gros coup coeur pour cet orateur.
Déjà le mec était en kilt, sa présentation avait une petite licorne qui marchait en header
et un bagou énorme.
J'étais venu pour la partie cartographie mais
au final, il a plus parlé de débrouille, de comment apprendre,
de qu'est-ce que c'est d'écrire du code et comment y prendre plaisir.
Un de mes défauts est d'avoir peur d'écrire du "mauvais" code ce qui me bloque souvent à commencer des trucs
mais ce mec m'a fait comprendre que des fois,
c'est ok de faire des choses bizarres, d'expérimenter,
de faire des approximations, si c'est pour passer un bon moment.

## Tentative de conclusion

J'ai passé une PyConFr très agreable, appris beaucoup de choses
et rencontré plein de gens intéressants qui avait tous en commun
d'adhérer (je pense) aux valeurs de Python (`import this` entre autres).
Des valeurs de simplicité, d'élégance et de partage.
Victor Stinner a utilisé une citation de Brett Cannon:
"Python, venez pour le langage, restez pour la communauté".
Et c'est ce qui est en train de se passer pour moi.
Avant, la communauté, c'était les dépots pypi, les blogs et les livres.
Maintenant, je sais que derrière chaque dépôt se cache quelqu'un avec sa propre histoire,
chaque blog est écrit par quelqu'un qui attend son train ou son avion,
et les livres, par des gens tellement devoués qu'ils sont prêts à sacrifier des jours
et des nuits pour nous.

Et ça putain, c'est beau.
