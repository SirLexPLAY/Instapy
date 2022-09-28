# Instapy
## Installasjon
Fork/last ned filene og legg dem inn i en mappe. Ved hjelp av en terminal, naviger deg til mappen, og kjør følgene kommando:
`python3 -m pip install .`

## Brukermanual
Kommandolinje grensesnitt brukes her. For å benytte deg av programmet, skriver du kommandoene på formen 
`python3 -m instapy <arguments>`
For å legge et svart-hvitt filter på et .jpg bilde, la oss si filen heter `ditt_bilde.jpg`, skriv da følgende:
`python3 -m instapy ditt_bilde.jpg -g`
Du kan også skalere bilde til å være mindre. Vil du bildet skal være 3 ganger så mindre, skriver du tilsvarende:
`python3 -m instapy ditt_bilde.jpg -g -sc 3`
Vær obs på at kun positive heltall tas som parameter.

Her er listen over parametrene:
```
positional arguments:
  file                  The filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -g, --gray            Select gray filter
  -se, --sepia          Select sepia filter
  -sc SCALE, --scale SCALE
                        Scale factor to resize image
  -i {python,numba,numpy}, --implementation {python,numba,numpy}
                        The implementation
```

Du kan få opp en lignende ved å taste
`python3 -m instapy -h`


## [Info]
**Tittel:** Instapy

**Dato:** September 2022

**Type prosjekt:** Assigment 3, IN3110: Problemløsning med høynivå-språk (UiO)

**Programmeringsspråk:** Python

