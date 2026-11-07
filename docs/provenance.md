# Data provenance

Activity data were retrieved from the ChEMBL REST API (`/activity`, joined to `/assay` on
`assay_chembl_id`) by `src/1_fetch_p38.ipynb`. Each fetch with `REFRESH = True` appends an entry
below.

Selection criteria for all targets: *Homo sapiens*, IC50 or Ki in nM, relation `=`, assay
confidence score ≥ 8, no data validity comment, not flagged as a potential duplicate.

ChEMBL data are licensed under CC BY-SA 3.0.

## p38α (MAPK14) training set (2026-11-04)

- Target: `CHEMBL260` (MAPK14, p38α), *Homo sapiens*
- ChEMBL release: ChEMBL_37
- Records fetched: 9916 -> surviving activities: 6163 -> unique molecules: 5012
- Labels: active 4078, inactive 148, dropped (5-6 band) 786
- Raw payload: `data/raw/p38_activities_raw.json`

## COX-2 (PTGS2) training set (2026-11-06)

- Target: `CHEMBL230` (PTGS2, COX-2), *Homo sapiens*
- ChEMBL release: ChEMBL_37
- Records fetched: 9404 -> surviving activities: 5148 -> unique molecules: 4395
- Labels: active 2482, inactive 651, dropped (5-6 band) 1262
- Raw payload: `data/raw/cox2_activities_raw.json`

## 5-LOX (ALOX5) training set (2026-11-06)

- Target: `CHEMBL215` (ALOX5, 5-LOX), *Homo sapiens*
- ChEMBL release: ChEMBL_37
- Records fetched: 4322 -> surviving activities: 3345 -> unique molecules: 2355
- Labels: active 1299, inactive 214, dropped (5-6 band) 842
- Raw payload: `data/raw/lox5_activities_raw.json`
