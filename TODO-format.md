# Repo format: analysis and TODO

Written 11 Nov 2026, after all three project drafts landed on `main`.
It compares the two structures (finance by Vojtěch, Wordle and Titanic by Tomas),
takes the notes in `feedback.md` as already agreed, and proposes one format for
the repo. Both `feedback.md` and this file are one-off working notes. They are
not part of the format and do not need to live on any branch.

Guiding rule: **`main` never contains project solutions.** Participants get
hints in separate files. Full project solutions and coach notes live on a branch
that only coaches use during the day. Lessons (`lekce-*/`) follow `materialy`:
their solutions sit in `reseni/` next to the exercises, on `main`.
(C1, decided provisionally by Vojta on 13 Nov; **Tomas to confirm**.)

Companion note: `REPORT-materialy.md` (13 Nov) compares this repo with the
conventions of `pyladiesprague/materialy`. Its open decisions C1–C3 are listed
in section 4 under "From the materialy comparison". C1 changed the guiding rule
above: it now covers projects only.

Section 3 records each decision as Tomas chose it. Vojtěch adds his feedback here.

## 1. Where we are

| | Finance | Wordle | Titanic |
| --- | --- | --- | --- |
| Folder | `projekt-finance/` | `wordle/` | `titanic/` |
| Steps | `zadani/krokN_nazev.md`, 6 steps | `kroky/NN_nazev.md`, 10 steps | `kroky/NN_nazev.md`, 9 steps |
| Step layout | sample output, 1 Testy, 2 Funkce, 3 Menu, Nápověda, Hotovo když, Když zbyde čas | Logika, Testy, Program | question, Logika, Testy, Zpráva |
| Hints | inline at the end of each step, mostly pointers to taháky | separate `napovedy/` folder, code skeletons | none |
| Tests | pytest, plain functions with `assert` | unittest classes | unittest classes |
| How tests are handed out | copy ready tests each step, plus one own test | given, then fill in blanks, then own | same as Wordle |
| Working files | directly in the project folder | subfolder `moje_hra/` | subfolder `moje_analyza/` |
| Folder to open in VS Code | whole repo | `wordle/moje_hra` | `titanic/moje_analyza` |
| VS Code settings | repo root, pytest | inside `moje_hra/`, unittest | inside `moje_analyza/`, unittest |
| Solutions | branch `projekt-finance-reseni`, generated from one template | `reseni/` **on `main`** | `reseni/` **on `main`** |
| Coach notes | `reseni/README.md` on the branch | none | `pro_kouce.md` **on `main`**, with all results |
| Cheat sheet | `TAHAK.md` (imports, tests, JSON) | none | none |
| Bonuses | one file, 11 bonuses, 4 with solutions | one file, 2 bonuses | one file, 5 bonuses |
| Smoke test at start | yes: one green test and a program that runs | no, starts red | no, starts red |
| Minimum goal stated | yes, step 3 | no | no |
| Saving work | not mentioned | Commit and Sync after each step | Commit and Sync after each step |

### Problems found while comparing

1. **Solutions are on `main`.** `wordle/reseni/`, `titanic/reseni/` and
   `titanic/pro_kouce.md` came in with PR #1 and move to `reseni`.
2. **Opening the repo root shows other projects' red tests.** `python -m pytest`
   from the root gives 7 failed, 1 passed on a fresh `main`: the starter tests of
   Wordle and Titanic fail by design. A finance participant sees them too.
3. **Three READMEs disagree on which folder to open** (repo root, `moje_hra`,
   `moje_analyza`), and on the test tool.
4. **Getting the repo is undefined.** The root README says Download ZIP. Wordle
   and Titanic say Commit and Sync, which needs a fork and a clone.
5. **The solutions branch is not private.** The repo is public, so anyone can
   open the branch on GitHub. It keeps answers out of the way, nothing more.
   Accepted: see D5.
6. **The solutions branch falls behind.** `projekt-finance-reseni` is already
   behind `main`. Every change to steps or tests needs a follow-up there.
7. **Tests are explained three times**, once per project README, in two styles.
8. **File paths.** Wordle and Titanic find their data from the file's own
   location. Finance step 6 opens `finance.json` by bare name and relies on a
   VS Code setting.

## 2. Target format

```
README.md                  how the day works, how to get the repo, project table
(no root TAHAK.md: the lesson taháky cover imports and tests, decided 16 Nov)
pytest.ini, .gitignore, .vscode/   one shared VS Code setup, repo root is what gets opened
<projekt>/
    README.md              what you build, steps table, files, before you start, when stuck
    TAHAK.md               only what this project needs beyond lessons (JSON, CSV)
    cviceni/NN_nazev.md    one step per file, two-digit number (C2, as `materialy`)
    napovedy/NN_nazev.md   hint, same file name as its step; steps without a hint leave gaps
    bonusy/NN_nazev.md     one bonus per file
    napady.md              ideas for extensions, no solutions
    <logika>.py, <program>.py, test_<logika>.py, data files
```

Branch `reseni` (one for all projects) is `main` plus:

```
<projekt>/cviceni/reseni/NN_nazev/   full project after step NN, same name as the step
<projekt>/bonusy/reseni/NN_nazev[.py|/]  bonus solution: one file, or a folder for a whole project
<projekt>/pro_kouce.md               intro script, expected results, what to watch for
```

The layout mirrors a concept folder in `materialy` (`cviceni/`, `cviceni/reseni/`,
bonuses with their own `reseni/`). Two differences: bonuses are in `bonusy/`
(not `cviceni_bonusy/`), and `napovedy/` is new. Solutions exist only on the
`reseni` branch, so on `main` the `reseni/` folders are simply missing.

### Step file template

1. Title: `# Krok N – Název`.
2. **What the program does at the end of the step**: sample output or one example call.
3. **Funkce**: table of functions and what they return. Always before the tests (D8).
4. **Testy**: early steps give finished tests to copy; later steps list the cases
   and the participant writes the tests (D9).
5. **Program**: what to add to the runnable file.
6. One line pointing to the hint file.
7. **Hotovo, když**: checklist.

### Hint file rules

- Same file name as the step, in `napovedy/` (1:1). Not every step needs a hint.
- First: the idea in words, and where to look (tahák and section).
- Then, only if needed: a code skeleton with `...` where the thinking is.
- Never the full function. That is what `reseni` is for.
- Hard steps may have two files, `_1` and `_2`, so the first can be read alone.
  Kept on purpose (decided 13 Nov): the step name plus a suffix, e.g.
  `06_opakovana_pismena_1.md` and `_2.md`. The web UI shows them as hint 1
  and hint 2 of that step.

### Project README template

1. What you will build, with sample output.
2. Steps table: step, what is added, what you practise. State the minimum goal.
3. Files table.
4. Before you start: checklist ending with a smoke test (one green test, program runs).
5. When you get stuck: error message, hint file, neighbour, coach. No mention of solutions.
6. End of day: you will show what you built.

## 3. Decisions

Status on 11 Nov: Tomas has chosen on all twelve. Vojtěch reviews them and writes
his feedback into this file.

**D1. Test tool. Tomas, Vojta: pytest.**
Plain functions and `assert`, no `class` or `self` to explain, clearer failure
output, already configured at the root. The cost is `pip install pytest`: ask
participants to install it before the workshop and keep five minutes for it at
the start. Titanic bonus 3 needs `pip` anyway.

**D2. Which folder a participant opens in VS Code. Tomas, Vojta: the repo root.**
Reason: switching between projects is easy, Git works with no prompt, and there
is one settings file. This differs from my first suggestion (project folder).
Opening the root has one cost, the red tests of other projects, and it is solved
like this:
- Every project's starter test file holds only one test, and it passes. The
  tests for step 1 are in the step file and the participant copies them in, as
  finance already does. A fresh `main` is then fully green from the root.
- Module and test file names must be unique across projects (`logika`,
  `analyza`, `finance`; `test_logika`, `test_analyza`, `test_finance`), because
  pytest run from the root loads them all into one namespace.
- READMEs show how to run only your own project's tests in the Testing panel.
- Per-project `.vscode` folders are removed; the root one is the only one.

**D3. How participants get the repo and save work. Tomas, Vojta: fork and clone.**
The fork dialog copies only `main` by default, so the solutions branch does not
come along. Download ZIP stays as the fallback for anyone whose Git setup
fails. Every step in all three projects ends with the same Commit and Sync line.
Saving to GitHub is taught before 21 Nov.

**D4. `moje_hra/` and `moje_analyza/`. Tomas, Vojta: flatten.**
The subfolders kept participant files apart from `reseni/`. Once solutions leave
`main`, that reason is gone. Working files sit in the project folder, as in finance.

**D5. Who uses the solutions. Tomas, Vojta: coaches during the day, everyone afterwards.**
- During the workshop the `reseni` branch is a tool for coaches. A coach looks
  at it to help a stuck participant straight away, or when the coach is stuck too.
- The aim is not to lock solutions away, only to not make them easy. A branch
  does that: forks copy only `main`, and no participant material links to it.
- At the end of the workshop participants get the link to the branch, so they
  can compare their work with the solution.
- No catching up by copying. Nobody is handed a finished step to move on. A
  stuck participant works it out with hints and a coach. This drops the earlier
  design assumption that anyone stuck can jump ahead from a solution.

C1 (provisional, Vojta 13 Nov, Tomas to confirm): this applies to projects only.
Lessons follow `materialy` and the organizace authoring rules: their solutions
sit in `reseni/` next to the exercises, on `main`, as `lekce-testovani/` and
`lekce-moduly/` already do.

Consequence: the READMEs must not tell participants to copy a solution and
carry on. Wordle and Titanic say that today, and the finance README promises
"dostaneš hotové řešení toho kroku".

**D6. Solutions branch. Tomas, Vojta: one combined `reseni` branch.**
All three projects' solutions and coach notes live on one branch.

**D7. Names. Tomas: Vojtěch's style throughout.**
- Project folders keep the `projekt-` prefix: `projekt-finance/`, `projekt-wordle/`,
  `projekt-titanic/`. Vojta: good to keep the projekt prefix as in root there will be also materials about testing and modules.
- ~~Steps folder: `zadani/`.~~ Replaced by C2: `cviceni/`.
- ~~Step files: `krokNN_nazev.md`.~~ Replaced by C2: `NN_nazev.md`.
  Vojta: Not sure about this one, in lesson materials we use just numbering.
- Titles: `Krok 1 – Název`.
- Code file names stay per project (`finance.py`/`app.py`, `logika.py`/`wordle.py`,
  `analyza.py`/`zprava.py`). The rule is only: one logic file, one runnable file,
  one `test_<logika>.py`, all with names unique in the repo (see D2).
- Numbers always have two digits: `krok01_nazev.md`, `bonus01_nazev.md`,
  `reseni/krok01/`. Wordle has ten steps and finance has eleven bonuses, and
  without the leading zero `krok10_` sorts between `krok1_` and `krok2_`. Vojta: I think we should have leading zeros for sorting.
- **Decided 13 Nov by Vojta (C2 in `REPORT-materialy.md`): same as `materialy`,
  the folder says what a file is.** `cviceni/01_zaklad.md`, `napovedy/01_zaklad.md`
  (1:1 with its step, gaps allowed; a hard step may split its hint into `_1`
  and `_2`), `bonusy/01_barvy.md`. Solutions on `reseni`
  as in `materialy`: `cviceni/reseni/01_zaklad/`, `bonusy/reseni/01_barvy/` or
  `bonusy/reseni/02_hledani.py`. Titles stay `Krok N – Název` and
  `Bonus N – Název`, like `Cvičení N – …`. Done in all three projects.

**D8. Order inside a step. Tomas, Vojta: function description first, then tests.**
Finance currently gives tests first, so its steps swap the two sections.

**D9. How tests are handed out. Tomas, Vojta: ready tests first, own tests later.**
One style for all three projects:
- *Early steps:* the step file contains finished tests. The participant copies
  them in and uses them to confirm quickly that her code works.
- *Later steps:* the participant writes the tests herself, to confirm her own
  implementation. The step file lists what to cover (cases, or a table of calls
  and expected results), not the test code.
- A middle stage with blanks to fill in (`___`) is allowed where it helps.
- Each project owner picks the step where the switch happens.

Wordle and Titanic already work this way. Finance switches at step 4 (16 Nov):
steps 4 and 5 list cases, step 6 keeps ready tests as an exception (`tmp_path`).

**D10. Wordle game screen. Tomas, Vojta: stays as step 10.**
It was considered for a bonus only because clearing the screen did not seem to
work when tried. It stays a regular step, so the cause needs finding first: see
the Wordle TODO. Finance and Titanic get screen clearing as a bonus (feedback).

**D11. Charts in Titanic. Tomas: a regular step, placed before the report.**
The text bar chart (today bonus 2) becomes a regular step before the report
step, so the report can include it. It reuses the bar function from finance
step 5, `sloupec(hodnota, nejvyssi, sirka)`: same name, same parameters, same
tests, so both projects teach one design. The plotext charts stay a bonus,
because they need an install. Vojta: What are plottext charts and are we using it? Should we do the same in finance?

**D12. HTML report in finance. Tomas, Vojta: last bonus.**
Feedback said it comes too early and may be dropped. It moves to the end of the
bonuses and can still be removed.
Done 13 Nov on `main`: HTML report is now bonus 4 (after Barvy, Hledání, Řazení),
so it stays last once bonuses 5 to 11 move to `napady.md`.

## 4. TODO

### Who does what
- **Wordle and Titanic:** Tomas.
- **Finance:** Vojtěch.
- **Unit Testing Lesson:** Vojtěch.
- **Modules Lesson:** Vojtěch.
- **Repo-wide items:** whoever gets to them first.

Order: project-specific work first, repo-wide changes after.

### Still open
- Vojtěch reads this file and writes his feedback into it. => Done
  - Tomas: Validate feedback from Vojtech
- **Wordle and Titanic refactor (Tomas, 14 Nov).** Both projects are rewritten
  to the agreed format: pytest, flattened, result first, hints, `napady.md`,
  generated solutions. Titanic also has a new line of questions. Details in the
  Wordle and Titanic lists below. For Vojtěch to review:
  - Titanic now has twelve steps and a different main question.
  - `sloupec_grafu` in Titanic differs in name from finance's `sloupec`.
  - Each step's "Hotovo, když" ends with the Commit and Sync item (D3).
  - `zkontroluj_reseni.py` on `reseni` runs pytest in every
    `cviceni/reseni/NN_*` folder of all three projects.
- **plotext (answer to Vojtěch's question in D11).** A small library that draws
  charts in the terminal. Only Titanic bonus 2 uses it, as a taste of "a library
  does this for you" after participants wrote their own chart in step 9. It
  needs `pip install plotext==5.3.2`. Finance does not need it.

### Repo
- [x] Tag `pred-unifikaci` on `main` before any unification change (pushed 13 Nov).
- [x] Create branch `reseni` from `main` and move the finance solutions there.
      Done 13 Nov: `reseni` = `main` + merge of `projekt-finance-reseni`.
- [x] Delete stale branches: `projekt-finance` (equals old `main`),
      `projekty-wordle-titanic` (merged), and `projekt-finance-reseni` once moved.
      Done 13 Nov, locally and on GitHub. All three were fully contained in
      `main` or `reseni`; the pre-unification state is kept by tag `pred-unifikaci`.
- [x] Root `README.md`: how the day runs, fork and clone (D3), open the whole repo
      folder (D2), how to run only your project's tests, project table with the new folder links (D7), and that
      the day ends with a show and tell. No mention of solutions.
      Done 16 Nov, with a link to `PRED-WORKSHOPEM.md` and fork and clone
      replacing Download ZIP (ZIP stays as the fallback).
- [ ] At the end of the workshop, send participants the link to the `reseni` branch (D5).
- [ ] Before the workshop, tell participants to install pytest (D1) and to have a
      GitHub account ready (D3).
- [x] **Later, after the converter below:** a "before the workshop" document for
      participants: GitHub account, fork and clone, `pip install pytest cowsay`
      (the modules lesson needs cowsay; pyfiglet only for bonuses), what to do
      when the install fails. It has to fit the public-pages converter, so it is
      written once the converter supports this repo.
      Done 15 Nov: `PRED-WORKSHOPEM.md` (fork, clone in GitHub Desktop, ZIP
      fallback, `pip install pytest cowsay pyfiglet`, troubleshooting table,
      check with the Testing panel and the cow, sync the fork in the morning).
      The converter renders it as `/materialy/workshop-opakovani/pred-workshopem/`,
      linked from the workshop page (public-pages PR #15).
  - [ ] Announce it: e-mail and Discord still open. Web banner done 16 Nov
        (public-pages `content/oznameni/workshop-opakovani.md`, until 21 Nov).
- [x] public-pages converter for the workshop repo. Done 13–14 Nov (public-pages
      PR #13, merged; automatic import since 14 Nov). It used to read only
      `pyladiesprague/materialy`. The lessons here (`lekce-moduly/`, testing)
      already follow the materialy format; the projects get their own Markdown
      format (C3: projects go on the web like `materialy`).
      It must support several hints per step: `napovedy/NN_nazev_1.md`,
      `_2.md` show as hint 1 and hint 2, so the second is opened only when the
      first is not enough.
- [x] Lesson order: modules first, then testing, which builds on importing your
      own module (Vojta, 17 Nov). README, both lessons and their taháky say so.
  - [ ] public-pages: swap `order` of `lekce-moduly` and `lekce-testovani` in
        `code/workshop/opakovani.json`, today testing is still first on the web.
- [x] ~~Root `TAHAK.md`~~: dropped by Vojta on 16 Nov. The lesson taháky
      (`lekce-testovani/TAHAK.md`, `lekce-moduly/TAHAK.md`) already cover
      importing your own file, writing and reading tests and common errors;
      a root tahák would be a third copy. Project taháky and READMEs link there.
- [x] Keep the root `.vscode/` as the only one; remove the per-project unittest
      settings in Wordle and Titanic (D2). Done 14 Nov (PR #2).
- [x] `pytest.ini`: keep `norecursedirs = reseni`, needed on the `reseni` branch.
      Present on `main` and `reseni`.
- [x] One root `.gitignore` with `statistiky.txt`, `zprava.txt`, `report.html`;
      drop the per-project ones. Done 13 Nov, also covers Python, IntelliJ/PyCharm
      and VS Code (only the shared `.vscode/settings.json` and `launch.json` are kept).
- [x] Add `.gitattributes` with `* text=auto eol=lf`. Windows checkouts already
      produced mixed line endings.
      Done 13 Nov on `main` and `reseni`, plus `"files.eol": "\n"` in the shared
      `.vscode/settings.json`. LF on disk on every OS, including Windows.
- [x] A check script on `reseni` that runs pytest in every `cviceni/reseni/NN_*` folder:
      `zkontroluj_reseni.py` in the repo root (14 Nov).
- [x] Solutions are generated, not edited by hand, in all three projects. Each
      owner regenerates and updates `reseni` after changing their project. See
      whether finance's `sestav.py` can be made to serve all three.
      Done 15 Nov: each project has its own `cviceni/reseni/_predloha/sestav.py`
      on `reseni`; `zkontroluj_reseni.py` passes for all three.
- [x] Coach notes in one place per project: `pro_kouce.md` on `reseni`. Titanic has
      one (moved off `main` 13 Nov), finance's moved there from `reseni/README.md`
      13 Nov, Wordle's added 15 Nov. All three have `pro_kouce.md` on `reseni`.
- [x] Update the workshop design doc: pytest, ten Wordle steps as decided, and the
      dropped rule that anyone stuck can catch up from a solution (D5).
      Done 16 Nov as a new comment under Tomas's design in organizace issue #22
      (his comment left as is): pytest, steps per project, `reseni` branch for
      coaches only, no catching up by copying.
- [ ] Delete `TODO-format.md` and `REPORT-materialy.md` from `main` before the workshop.
- [x] Final pass for one style across projects (feedback): headings, tables,
      line wrapping, how the participant is addressed. Done 15 Nov: participant
      is "ty", feminine, everywhere; function tables use "Co vrátí", or "Co dělá"
      where a function changes data or returns nothing; `napady.md` titles and
      the README ending ("Na konci dne") unified.

### From the materialy comparison (`REPORT-materialy.md`)
Decisions:
- [x] **C1. Solutions:** provisionally decided by Vojta on 13 Nov: projects keep
      solutions only on the `reseni` branch, lessons keep `reseni/` on `main`
      (as `materialy`). Guiding rule and D5 reworded.
  - [ ] Tomas: confirm C1.
- [x] **C2. Numbering:** decided 13 Nov, see D7: `cviceni/NN_nazev.md`,
      `napovedy/NN_nazev.md`, `bonusy/NN_nazev.md`, solutions as in `materialy`.
- [x] **C3. Web:** decided by Vojta on 13 Nov: projects go on the web like
      `materialy`. The public-pages converter learns a strict Markdown project
      format (option 1 in the report): `README.md`, `cviceni/NN_*.md`,
      `napovedy/NN_*.md` (with `_1`/`_2`), `bonusy/NN_*.md`, `TAHAK.md`.
  - [x] Write the project format down for the converter: draft in
        `FORMAT-projektu.md` (13 Nov). Part 2 is the source format (later moves
        into the root README as "Pro autory"); part 3 lists what the current
        materials need to change to fit it, per project.
  - [ ] Tomas: review `FORMAT-projektu.md`. All open points were decided by
        Vojta on 13 Nov:
        - Hints sit behind a "Zobrazit nápovědu" button like "Zobrazit řešení";
          each further hint behind "Zobrazit další nápovědu" inside the previous one.
        - No project solutions on the web, not even a link to the `reseni` branch.
        - Step sections are fixed: `Funkce`, `Testy`, `Program`, `Hotovo, když`,
          in this order, missing ones allowed, `###` free. Exceptions: a test-first
          step may put `Testy` first, an open last step uses `Postup`. The converter
          rejects anything else. Mapping of today's headings: part 2, Krok, point 3.
        - README title is the short project name only (`# Správce osobních
          financí`, `# Wordle s řešičem`, `# Titanic`; done). The converter takes
          the page title from it; `config.json` holds order and a short description.
        - The workshop goes under Materiály, like the course lessons:
          `/materialy/workshop-opakovani/` plus repo paths. Details in part 1.
        - The "test your module" bonus: the solution has the same name as the
          task, with a copy of `spropitne.py` next to it so it runs with
          `python -m pytest 03_test_modulu.py` (done). Since 17 Nov it is
          bonus 3 in `lekce-testovani/02_pytest/`, no longer bonus 2 in
          `lekce-moduly` (it needs pytest, which comes after modules).
- [x] **Exceptions:** out of scope for this workshop, decided by Vojta on
      13 Nov; Tomas to confirm if he disagrees. They stay in L13 (CSV a výjimky).
  - [ ] Tomas: confirm, if needed.
  - [x] Update `organizace/content/podzim-2026/materialy.md`, which still says
        *soubory, výjimky a moduly patří do middle workshopu*.
        Done 16 Nov (organizace `22a32f8`): moduly, pytest and soubory belong
        to the workshop, výjimky stay in L13.

Alignment with `materialy`:
- [x] Titles with an en dash: Wordle `# Krok 1: …` becomes `# Krok 1 – …` (13 Nov).
      Bonus files already use `# Bonus N – …` since the split on 13 Nov.
- [x] Solution headers in Wordle and Titanic: `# Řešení kroku N – …` /
      `# Řešení bonusu N – …`, then "Tvoje řešení může vypadat jinak, a to je
      v pořádku." Done 15 Nov in all three generators on `reseni`; the step
      name comes from the step title.
- [x] Wrap Markdown prose at about 75–80 characters in Wordle and Titanic
      (part of the final style pass). Done 15 Nov, all three projects. Tables,
      code and the hint pointer line stay on one line (the converter needs it).
- [x] `.gitattributes`: `export-ignore` for `TODO-format.md`,
      `REPORT-materialy.md`, `feedback.md` and a future `.github/`, as
      `materialy` does for its ZIP.
      Done 16 Nov: `.github`, `.gitattributes` and `FORMAT-projektu.md`.
      `feedback.md` is gone; TODO and REPORT get deleted before the workshop.
- [x] Root README "Jak si materiály stáhnout": fork and clone with ZIP as
      fallback (D3), same wording as lesson 1 in `materialy`.
- [ ] Project changes go through PRs with the other owner as reviewer; branch
      names `finance/…`, `wordle/…`, `docs/…`; commit subjects `Finance: …`.
- [x] CI: a workflow that runs pytest on `reseni`
      (covers the "check script" item above); later copy the `web.yml` pattern.
      `web.yml` copied 14 Nov: converter check on PRs and pushes to `main`,
      automatic import into `public-pages` after a push. Done 16 Nov:
      `.github/workflows/reseni.yml`, only on `reseni` (forks copy only `main`),
      runs `zkontroluj_reseni.py` on push and PR to `reseni`; first run green.
- [ ] Optional: one picture per project made with the `obrazek` skill from
      `materialy`.

Schedule fit (workshop Sat 21 Nov, after L9 Slovníky on 19 Nov):
- [ ] Dictionaries are two days old. Project taháky link to the lesson 9
      tahák; coaches expect questions on them.
- [x] CSV is taught only in L13 (17 Dec), so the Titanic tahák must explain
      reading CSV on its own. Done 14 Nov: `projekt-titanic/TAHAK.md`.

### Every project
- [x] Rename to the agreed layout (D7, C2): `cviceni/NN_nazev.md`, bonuses split
      into `bonusy/NN_nazev.md`, solutions into `cviceni/reseni/` and
      `bonusy/reseni/` on `reseni`, README links updated. Done 13 Nov, all three
      projects. Finance's bonus intro moved into its README.
- [x] Rewrite each step to the step template: result first, Hotovo když at the end.
      All three projects (finance 13 Nov, Wordle and Titanic 14 Nov).
- [x] Hints into `napovedy/`, following the hint rules. Every step of all three.
- [x] Remove every sentence that sends participants to solutions or offers a
      finished step for catching up (D5). Done in the three project READMEs on
      13 Nov; step and hint files checked 15 Nov, none left.
- [x] Add `napady.md`: extension ideas without solutions (high scores,
      difficulty levels, and similar).
- [x] Add a bonus for clearing the terminal where the project lacks one.
      Wordle has it as step 10, Titanic as bonus 5; finance still lacks one.
      Done 16 Nov: finance bonus 5 `05_cisteni_obrazovky.md`, same recipe as
      Titanic (clear before the menu, wait for Enter, balance above the menu);
      solution `bonusy/reseni/05_cisteni_obrazovky.py` on `reseni`.
- [x] README to the README template, including the minimum goal and the
      smoke test in "before you start". Done: all three have the template
      sections, a minimum goal (finance and Wordle step 3, Titanic step 6) and a
      smoke test. 16 Nov: "Než začneš" step 1 links to `PRED-WORKSHOPEM.md`
      (pytest command kept as fallback), finance step 3 runs only its own tests
      like Wordle and Titanic.
- [x] Starter test file contains only one test, and it passes. Step 1 tests move
      into the step file (D2). All three: one passing test each (15 Nov).
- [x] Module and test file names are unique across the repo (D2):
      `finance.py`, `logika.py`, `analyza.py` and their `test_*.py`.
- [x] Check that input cleaning is practised (feedback): case, `strip`, types,
      positive and negative numbers, dates.
      Finance checked 16 Nov: types, sign, dates and empty input were already in
      step 2 (`je_platna_castka`, `je_platne_datum`, Hotovo když); `strip` and
      `lower` were only in the solution, now also in the step, its Hotovo když
      and the hint. Wordle and Titanic checked 16 Nov, no change needed:
      Wordle step 2 `uprav_vstup` (strip, lower) with a test and Hotovo když
      (`Kabát` with spaces), length check, step 3 unknown words and the
      play-again answer through the same function. Titanic step 2 converts
      types (`int`, `cislo_nebo_nic`, empty text to `None`), step 11
      `najdi_sloupec` ignores case and spaces, unknown column and empty answer
      do not crash. Negative numbers and dates only apply to finance.
- [x] Data files are found from the file's own location, not the working folder.
      Done 15 Nov: all three use `Path(__file__).parent`.
- [ ] Last: test the participant path on Windows and macOS with this project:
      fork, clone, open the repo root, install pytest, Testing panel, Run,
      Commit and Sync.

### Finance
- [x] Renumber steps to `cviceni/01_…`, also in the solution generator (D7, C2).
- [x] Put the function description before the tests in every step (D8). Done 13 Nov:
      steps follow `FORMAT-projektu.md` (`Funkce`, `Testy`, `Program`, hint link,
      `Hotovo, když`); paragraphs about the tests moved from Funkce to Testy.
- [x] Move the inline "Nápověda" sections into `napovedy/` (13 Nov).
- [x] Move "Když zbyde čas" items and bonuses 5 to 11 (no solutions) into `napady.md`
      (13 Nov). Bonuses are now 1 to 4, all with solutions.
- [x] HTML report moved to bonus 4, last of the bonuses with solutions (D12).
- [x] Solutions: rename `bonus2_html_report.py` to `bonus4_html_report.py`,
      `bonus3_hledani.py` to `bonus2_hledani.py`, `bonus4_razeni.py` to
      `bonus3_razeni.py`; update `reseni/README.md` and `_predloha/sestav.py` (D12).
- [x] Split all eleven bonuses into separate files (13 Nov).
- [x] Step 6: build the path to `finance.json` from the file's location.
      Done 15 Nov: `Path(__file__).parent / "finance.json"` as a recipe in the
      step, the tahák and the hint; solutions regenerated on `reseni`.
- [x] Shared tahák parts out of the finance tahák (16 Nov): imports and tests
      replaced by links to the lesson taháky; kept the `finance.py` import
      rule, `ukazka()` and JSON. README got "Jak vypadá test" like Wordle and
      Titanic.
- [x] Adjust the tests to D9: pick the step where ready tests stop, and from
      there on replace the test code with a list of cases the participant tests
      herself.
      Done 16 Nov (Vojta picked step 4): step 4 has a table of calls and
      expected results (the empty-budgets row is left for her to work out),
      step 5 a list of cases. Step 6 keeps ready tests (tmp_path exception
      below) and says why. README "Každý krok" and the file table updated.
- [x] **Decided 16 Nov (Vojta):** the step 6 tests use pytest's `tmp_path`, so they do not
      touch the real `finance.json`. Beginners cannot write that themselves, which
      clashes with "own tests in later steps". They stay ready-made as an
      exception to D9, even if earlier steps switch to own tests. The step
      already explains `tmp_path` in one paragraph as a recipe; the own test
      (save and load an empty list) reuses it.
- [x] The solution generator takes tests from the step files. Once later steps
      have none, the solution tests need another source.
      Done 16 Nov on `reseni`: `_predloha/testy_04.py` and `testy_05.py`,
      appended after the step's own tests; `sestav.py` stops when a step has
      no tests at all. Includes the former "own test" cases (empty budgets,
      75 of 100 at width 20).
- [x] Add the Commit and Sync line to each step (D3). Done 14 Nov, same wording
      as Wordle and Titanic.
- [x] Every "Tahák LN" reference names the section: "Tahák L6, *Výřez*"
      (14 Nov, section names from the lesson taháky; L9 from `materialy`
      branch `lekce09/init-materials`).

### Wordle
Done by Tomas on 14 Nov, on top of the format from 13 Nov. Waiting for review.
- [x] Move `wordle/reseni/` from `main` to the `reseni` branch (13 Nov).
- [x] Convert tests to pytest functions (D1) in the starter file, the step files
      and the solutions; drop the `class` and `self` note. Tests use
      `import logika` and `logika.vyhodnot(...)`, as finance does.
- [x] Rename the folder `wordle/` to `projekt-wordle/` (D7).
- [x] Flatten `moje_hra/` (D4). Steps already moved to `cviceni/` (C2).
- [x] Step 6 keeps two hints, `06_opakovana_pismena_1.md` and `_2.md`
      (decided 13 Nov). The web UI gets support for several hints per step.
- [x] Add "result first" and "Hotovo, když" to every step.
- [x] Review hints against the hint rules; several give most of the function.
      Every hint now points to a lesson tahák section first.
- [ ] Step 10 stays (D10). Find out why clearing the screen did not seem to work:
      try it in the VS Code terminal on Windows and macOS. Changed meanwhile:
      `pomocnik.py` calls the system command (`cls` on Windows, `clear`
      elsewhere) instead of printing an escape code. Not tried on Windows or macOS.
- [x] Split the two bonuses into files (13 Nov).
- [x] Add `napady.md`.
- [x] `pomocnik.py` after flattening: it looks next to itself. The generator
      rewrites the path when it copies the file into a solution folder.
- [x] Write `pro_kouce.md` (intro, what to watch for in steps 5 and 6).
- [x] Build a generator for the solution folders, as finance has (one template,
      marked by step): `cviceni/reseni/_predloha/sestav.py`. It names the
      folders after the step files and runs their tests.
- [x] Steps follow `FORMAT-projektu.md`; the converter on `workshop-import`
      accepts the project without errors (preview run, 14 Nov).

### Titanic
Done by Tomas on 14 Nov, on top of the format from 13 Nov. Waiting for review.
- [x] Move `titanic/reseni/` and `titanic/pro_kouce.md` from `main` to the `reseni` branch (13 Nov).
- [x] Convert tests to pytest functions (D1) in the starter file, the step files
      and the solutions. The test data is a function `ukazka()`, as in finance.
- [x] Rename the folder `titanic/` to `projekt-titanic/` (D7).
- [x] Flatten `moje_analyza/` (D4). Steps already moved to `cviceni/` (C2).
- [x] Write hints for all steps; none existed.
- [x] Add "Hotovo, když" to every step. "Result first" shows the shape of the
      output with question marks in place of the numbers.
- [x] Turn the text bar chart (bonus 2) into a regular step before the report (D11).
      It is step 9; the report is step 10 and includes a chart. Same parameters
      and the same five test cases as finance. **Deviation:** the function is
      called `sloupec_grafu`, not `sloupec`, because in Titanic `sloupec` already
      means a column of the data and is a parameter name in several functions.
- [x] Split the bonuses into files (13 Nov). Bonuses are now: report in a file,
      charts with a library, families, children and adults, clearing the screen.
- [x] Add `TAHAK.md` for CSV and `None`, and `napady.md`.
- [x] Add user input somewhere, so input cleaning is practised: step 11 is a
      small explorer that asks for a column name and accepts any letter case.
- [x] One copy of the CSV in the project folder; the solutions read it from there.
- [x] Build a generator for the solution folders, as finance has.
- [x] **New line of questions (Tomas, 12 Nov).** The project no longer tests the
      claim "women and children first". It asks "who was on board and how did
      they fare?" and has twelve steps in three blocks:
      - who was on board: 3 oldest, youngest and average age, 4 ticket prices,
        5 names and titles (counts only);
      - how they fared: 6 who survived, 7 ports, 8 port or class;
      - putting it together: 9 chart, 10 report "Titanic v číslech",
        11 explorer, 12 own question.
      Steps 1 and 2 (loading, cleaning) are unchanged.
- [x] One idea next to the Python: a difference between groups is not a cause.
      Women and 1st class in step 6 (large groups, big difference), ports in
      steps 7 and 8 (most of the difference comes from class), titles in the
      explorer in step 11 (groups of one to seven people, chance). No
      terminology in the participant materials; `pro_kouce.md` has the numbers.
- [x] The heavy-topic warnings are gone. Children and adults moved to bonus 4.
- [x] Steps follow `FORMAT-projektu.md`; the converter on `workshop-import`
      accepts the project without errors (preview run, 14 Nov).
- [x] public-pages `code/workshop/opakovani.json` still describes Titanic as
      "jestli platilo ženy a děti první". Change it to the new question. Done 14 Nov.

## 5. How `feedback.md` maps to this

| Feedback | Where it lands |
| --- | --- |
| HTML too early, maybe drop | D12 |
| Unify style and format once all three exist | Repo: final pass |
| Input cleaning | Every project |
| Show the finished result at the start of each step | Step template |
| Bonuses in separate files | Target format, every project |
| Solutions branch for coaches only | Guiding rule, "Now" list, D5, D6 |
| Presentation at the end, announce it at the start | Root README, project README template |
| Hints as separate files in a separate folder | Target format, hint rules |
| Clearing the terminal as a bonus where missing | Every project, D10 |
| File of extension ideas without solutions | `napady.md` |
| Charts for Titanic too? | D11 |
