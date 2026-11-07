# Plant compounds and inflammation targets

Known inhibitors of p38α (MAPK14), COX-2 (PTGS2) and 5-LOX (ALOX5) from ChEMBL, compared by
structural similarity with the natural products of 12 Greek plants recorded in COCONUT 2.0.

For each plant compound, the most similar active inhibitor of each target is identified by
Tanimoto similarity on Morgan fingerprints (radius 2, 2048 bits), together with that
inhibitor's measured potency.

## Notebooks

| Notebook | Purpose | Output |
|---|---|---|
| `src/1_fetch_p38.ipynb` | IC50/Ki activities from ChEMBL for the three targets | `data/{slug}_training_raw.csv` |
| `src/2_explore_p38.ipynb` | Labels, potency, descriptors and chemical diversity | `analysis/{slug}/` |
| `src/3_prepare_p38.ipynb` | Structure standardization, Morgan fingerprints, clustering | `analysis/{slug}/prepared/` |
| `src/6_fetch_plants.ipynb` | Plant natural products from COCONUT 2.0 | `data/coconut/` |
| `src/7_plant_similarity.ipynb` | Closest known inhibitor for each plant compound | `analysis/plants/` |

`{slug}` is `p38` (CHEMBL260), `cox2` (CHEMBL230) or `lox5` (CHEMBL215).

## Data

Input data and generated results are not included in this repository. They are produced by
the notebooks in the order listed above:

- notebooks 1 and 6 download the source data when `REFRESH = True`;
- notebooks 2, 3 and 7 read those files and write their results to `analysis/`.

Sources:

- ChEMBL, release 37 (CC BY-SA 3.0); retrieval details in `docs/provenance.md`
- COCONUT 2.0, https://coconut.naturalproducts.net

Both are accessed through public endpoints; no credentials are required.

## Requirements

Python 3 with the packages in `requirements.txt`:

```
pip install -r requirements.txt
```
