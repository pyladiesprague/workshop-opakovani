# Workshop vs. `materialy`: conventions report

Written 13 Nov 2026. Compares this repo (projects, lessons and the plan in
`TODO-format.md`) with the conventions of the course repo
[`pyladiesprague/materialy`](https://github.com/pyladiesprague/materialy)
(`main` at `104788f`, plus the open `lekce09/init-materials` branch) and with the
authoring rules in `organizace/content/podzim-2026/materialy.md`. Like
`TODO-format.md`, this is a one-off working note.

Short version: the **lessons** here (`lekce-testovani/`, `lekce-moduly/`) already
follow `materialy`. The **projects** follow their own format, and most of it is
fine for multi-step projects. There are three real conflicts: where solutions
live, how files are numbered, and whether the web converter will read the
projects. Everything else is small alignment.

## 1. Conventions in `materialy`

**Structure**
- One folder per lesson, `lekceNN-nazev/` (hyphens, two-digit number).
- Inside a lesson: `TAHAK.md` and concept folders `NN_nazev/` (underscores).
- Inside a concept: explanation files `NN_nazev.py`, plus `cviceni/`,
  `cviceni/reseni/`, `cviceni_bonusy/` and `cviceni_bonusy/reseni/`.
- Images (PNG) sit in the concept folder. The `obrazek` skill keeps their
  style consistent.
- Numbers are always two digits with no word prefix: `01_oddelovac.py`, not
  `cviceni01_…`.

**File format** (required, because the public-pages converter reads it)
- Explanation file: a title between two `# ---` lines, then runnable code with
  comments.
- Exercise: one task per file. The first line is `# Cvičení N – <koncept>`,
  then `# Doplň kód pod zadání a soubor spusť (Run).`
- Bonus: `# Bonus N – <koncept>`.
- Solution: same file name in `reseni/`. The first line is
  `# Řešení cvičení N – …`, then
  `# Tvoje řešení může vypadat jinak, a to je v pořádku.`
- Everything is a `.py` file. The only Markdown files are `TAHAK.md` and
  `README.md`.

**Tahák**
- Title `# Tahák – Lekce N: Téma`, then the line
  `Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.`
- 50–150 lines: short code blocks and tables.

**Language and style**
- Participants are addressed with *ty* and feminine forms (*napsala*,
  *prošla*).
- En dash in titles. PEP 8 in all examples. Comments wrapped at about 75
  characters.

**Getting the materials**
- README: Download ZIP, then open the folder in VS Code.
- Lesson 1 also teaches fork and clone.
- `.gitattributes` uses `export-ignore` to keep `.github` out of the ZIP.

**Repo setup**
- No `.vscode/`. Every file is run with the Run button.
- No tests anywhere.
- `.gitignore` holds only `.idea`.

**Workflow**
- Every change goes through a PR from a branch named `lekceNN/init-materials`,
  `docs/…`, `fix/…` or `ci/…`.
- Review by Vojta R. and Vojta Š.
- Commit subjects are like `L8: …` (Czech or English).
- CI (`web.yml`) checks that the converter can read everything. After a merge
  it triggers the web import.

**Authoring rules (organizace)**
- Every lesson has at least one block where participants write code from
  scratch.
- The hardest topic is never last.
- Bonuses are for fast participants.
- **Solutions are available in the repo, and participants go back to them
  after their own attempt.**
- PEP 8.

**Schedule context**
- L8 Seznamy (12 Nov) and L9 Slovníky (19 Nov) come right before the
  workshop (Sat 21 Nov).
- Then L10 Procvičování, L11–12 Třídy, and L13 CSV a výjimky (17 Dec).
- Organizace says *soubory, výjimky a moduly patří do middle workshopu*.

## 2. Comparison

✅ = matches, ⚠️ = differs but is fine or easy to fix, ❌ = conflict to decide.

| Topic | `materialy` | This repo (plan in `TODO-format.md`) | |
| --- | --- | --- | --- |
| Solutions | `reseni/` on `main`, next to the exercises | Projects: `reseni` branch only, `main` never has answers (D5). Lessons: `reseni/` on `main` | ❌ |
| Numbering | `NN_nazev`, no prefix | D7: `krokNN_nazev.md`, `bonusNN_nazev.md` (Vojta unsure) | ❌ |
| Converter / web | Every file fits the converter; CI checks it | Lessons fit. Projects are Markdown steps the converter cannot read | ❌ |
| Lesson layout | `NN_koncept/`, `cviceni/`, `cviceni_bonusy/`, `reseni/` | `lekce-testovani/` and `lekce-moduly/` use the same layout | ✅ |
| Lesson folder name | `lekceNN-nazev` | `lekce-testovani`, `lekce-moduly` (no number, they are not course lessons) | ✅ |
| Content format | `.py` with comments | Lessons `.py`; projects `.md` steps with code to copy | ⚠️ |
| Titles | `Cvičení N – …`, en dash | Finance `Krok N – …` ✅; Wordle `Krok 1: …`, Titanic `Bonus 1: …` (colon) | ⚠️ |
| Solution header | `# Řešení … N – …` + "Tvoje řešení může vypadat jinak…" | Finance bonuses ✅; Wordle/Titanic `# Bonus 1: …`, no second line | ⚠️ |
| Bonus folder | `cviceni_bonusy/` | Lessons ✅; projects plan `bonusy/` | ⚠️ |
| Tahák | `Tahák – Lekce N: Téma` + A4 line | `lekce-testovani` ✅; finance `Tahák – Správce osobních financí` with its own intro | ⚠️ |
| Getting the repo | Download ZIP (README); fork and clone taught in L1 | Root README says ZIP; plan says fork and clone (D3) | ⚠️ |
| Opening in VS Code | Folder from the ZIP, Run per file | Repo root, shared `.vscode/` with pytest (D2) | ⚠️ |
| Tests | None | pytest everywhere (D1), taught in `lekce-testovani` | ✅ |
| `.gitignore` | `.idea` only | Python, IDEs, VS Code, outputs | ✅ |
| `.gitattributes` | `export-ignore` for ZIP | `eol=lf`, no `export-ignore` | ⚠️ |
| Images | PNGs per concept, one style | None | ⚠️ |
| Line wrapping | Comments ~75 characters | Finance wrapped; Wordle and Titanic steps have unwrapped lines over 100 | ⚠️ |
| Addressing | *ty*, feminine | Same in all three projects | ✅ |
| Workflow | PR per change, review, `L8:` subjects | Mostly direct pushes to `main` (one PR so far) | ⚠️ |
| CI | `web.yml` converter check | None | ⚠️ |

## 3. Conflicts to decide

**C1. Where solutions live.** *Decided provisionally by Vojta on 13 Nov, Tomas to
confirm: projects keep solutions only on the `reseni` branch, lessons keep
`reseni/` on `main` (the suggestion below).*
`materialy` and organizace say solutions sit next to the exercises, so
participants can compare after trying. D5 says `main` never has answers. The
repo now does both: `lekce-testovani/` on `main` contains `cviceni/reseni/`.
- *Suggested:* write the rule down as **lessons follow `materialy`
  (`reseni/` on `main`); projects keep solutions on the `reseni` branch.**
- The reasons differ. A lesson exercise is small and tried once. A project is
  one long build, and a finished step on `main` would let anyone skip ahead.
- Change the guiding rule in `TODO-format.md` from "`main` never contains
  direct answers" to "`main` never contains project solutions".

**C2. Numbering and names.** *Decided 13 Nov (see D7 in `TODO-format.md`):
the same as `materialy`. Steps go in `cviceni/NN_nazev.md`, hints in
`napovedy/NN_nazev.md`, 1:1 with their step, with gaps allowed. A hard step
may split its hint into `_1` and `_2`, and the web UI will show both. Bonuses go in
`bonusy/NN_nazev.md`. Solutions on `reseni` go in `cviceni/reseni/` and
`bonusy/reseni/`. Done in all three projects.*
Vojta's doubt on D7 matches `materialy`: two digits, no word prefix.
- *Suggested:* `zadani/01_zaklad.md`, `napovedy/01_zaklad.md`,
  `bonusy/01_barvy.md`. Solution folders on `reseni`: `reseni/01/` or
  `reseni/krok01/`. The latter is fine, since it is not participant-facing.
- Keep two digits (agreed).
- Titles stay `Krok N – Název` and `Bonus N – Název`, in line with
  `Cvičení N – …`.
- Optional: rename `bonusy/` to `cviceni_bonusy/` for the full match. I would
  not. `bonusy/` reads better in a project, and the converter rules for
  projects will be new anyway.

**C3. Projects and the web converter.**
The TODO already plans a converter for this repo. It can read the lessons as
they are. Projects are Markdown. The options:
1. Teach the converter a simple Markdown project format (`README.md`, then
   `zadani/NN_*.md`, `napovedy/`, `bonusy/`). Steps stay readable on GitHub.
2. Rewrite steps as `.py` files with comments, like the lessons. This is clumsy
   for multi-file steps with tables and sample output.
3. Keep projects off the web. GitHub renders the Markdown well enough.

*Suggested:* 1, or 3 for now.
- Either way, fix the format before the converter is written, so it targets
  something stable.
- If 1: make the format strict, as in `materialy`: fixed first line and fixed
  section headings from the step template.

## 4. Smaller alignment items

- **Titles with an en dash:** Wordle `# Krok 1: …` becomes `# Krok 1 – …`;
  Titanic and Wordle bonus files `# Bonus 1: …` become `# Bonus 1 – …`.
- **Solution headers in Wordle and Titanic:**
  `# Řešení kroku N – …` / `# Řešení bonusu N – …`, followed by
  "Tvoje řešení může vypadat jinak, a to je v pořádku.". Finance already does
  this.
- **Tahák intro:** project taháky keep their title. The intro says what they
  add beyond the lesson taháky; finance already does this. The root
  `TAHAK.md` (planned) uses the `materialy` style.
- **Line wrapping:** wrap Markdown prose at about 75–80 characters in Wordle
  and Titanic, like finance and `materialy`. This belongs to the "final pass
  for one style" item.
- **`.gitattributes`:** add `export-ignore` for `TODO-format.md`,
  `REPORT-materialy.md`, `feedback.md` and any future `.github/`, so a ZIP
  download stays clean, as in `materialy`.
- **Root README "Jak si materiály stáhnout":** still says Download ZIP only.
  Align with D3 (fork and clone, ZIP as fallback), using the same wording as
  lesson 1 in `materialy`.
- **Workflow:** from now on, project changes go through PRs with the other
  project owner as reviewer, like `materialy`. Branch names follow the same
  style: `finance/…`, `wordle/…`, `docs/…`. Commit subjects take a prefix:
  `Finance: …`, `Wordle: …`. That is already mostly the case.
- **CI:** once the converter exists, copy the `web.yml` pattern. Until then,
  a simple workflow that runs pytest on `reseni` covers the TODO item "check
  script on `reseni`".
- **Images:** optional. One picture per project (the finished program, or the
  data flow `finance.json` → `finance.py` → `app.py`) made with the `obrazek`
  skill would match the lessons.

## 5. Fit with the course schedule

- **Slovníky:** taught on 19 Nov, two days before the workshop.
  - Finance stores transactions as dictionaries from step 1.
  - Titanic rows are dictionaries too.
  - This works, but it is the freshest topic. The taháky should link to
    lesson 9 (its tahák once merged), and coaches should expect questions on
    it.
- **CSV:** taught in L13 (17 Dec), after the workshop.
  - Titanic uses `import csv` now.
  - The planned Titanic `TAHAK.md` must cover reading CSV on its own, as
    already in the TODO.
- **Výjimky:** organizace puts them into this workshop. None of the projects
  or lessons uses `try`/`except` today.
  - Either add exceptions somewhere, for example in finance input cleaning
    (`int()` on bad input) or Titanic number parsing, or tell organizace that
    exceptions move to L13.
  - This is the one syllabus gap.
  - *Decided by Vojta on 13 Nov, Tomas to confirm if needed: exceptions are
    out of scope for this workshop and stay in L13.*
- **Soubory and moduly:** covered.
  - Files: finance step 6 (JSON), Wordle word lists, Titanic CSV.
  - Modules: `lekce-moduly`, plus the logic/program split in every project.
- **Třídy:** not taught yet (L11). D1 removes the `unittest` classes from
  Wordle and Titanic, so this is already handled.
- **"Writing from scratch":** organizace wants at least one block of code
  written from scratch. Projects cover it; D9 (own tests in later steps) also
  fits.

## 6. Proposed TODO additions

Recorded on 13 Nov in `TODO-format.md`, section 4, "From the materialy
comparison". C1 and C2 are also noted at the guiding rule, D5 and D7.

- [ ] Decide C1 and reword the guiding rule in `TODO-format.md`.
- [ ] Decide C2 (`NN_nazev.md` without prefix?) before any renaming starts.
- [ ] Decide C3 (project format for the converter, or projects off the web).
- [x] Exceptions: out of scope, they stay in L13 (Vojta, 13 Nov).
- [ ] Titles and solution headers in Wordle and Titanic: en dash, second line.
- [ ] `.gitattributes`: `export-ignore` for working notes.
- [ ] Root README: fork and clone, ZIP as fallback, same wording as lesson 1.
- [ ] Project changes through PRs with cross-review.
- [ ] Delete `REPORT-materialy.md` together with `TODO-format.md` before the
      workshop.
