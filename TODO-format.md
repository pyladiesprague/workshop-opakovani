# Repo format: analysis and TODO

Written 11 Nov 2026, after all three project drafts landed on `main`.
It compares the two structures (finance by Vojtěch, Wordle and Titanic by Tomas),
takes the notes in `feedback.md` as already agreed, and proposes one format for
the repo. Both `feedback.md` and this file are one-off working notes. They are
not part of the format and do not need to live on any branch.

Guiding rule: **`main` never contains direct answers.** Participants get
hints in separate files. Full solutions and coach notes live on a branch that
only coaches use during the day.

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
TAHAK.md                   shared: importing your own file, tests, reading a failed test
pytest.ini, .gitignore, .vscode/   one shared VS Code setup, repo root is what gets opened
<projekt>/
    README.md              what you build, steps table, files, before you start, when stuck
    TAHAK.md               only what this project needs beyond lessons (JSON, CSV)
    zadani/krokNN_nazev.md     one step per file, two-digit number
    napovedy/krokNN_nazev.md   hint for the step with the same name
    bonusy/bonusNN_nazev.md    one bonus per file
    napady.md              ideas for extensions, no solutions
    <logika>.py, <program>.py, test_<logika>.py, data files
```

Branch `reseni` (one for all projects) is `main` plus:

```
<projekt>/reseni/krokNN/      full project after step NN
<projekt>/reseni/bonusy/
<projekt>/pro_kouce.md        intro script, expected results, what to watch for
```

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

- Same file name as the step, in `napovedy/`.
- First: the idea in words, and where to look (tahák and section).
- Then, only if needed: a code skeleton with `...` where the thinking is.
- Never the full function. That is what `reseni` is for.
- Hard steps may have two files, `_1` and `_2`, so the first can be read alone.

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

**D1. Test tool. Tomas: pytest.**
Plain functions and `assert`, no `class` or `self` to explain, clearer failure
output, already configured at the root. The cost is `pip install pytest`: ask
participants to install it before the workshop and keep five minutes for it at
the start. Titanic bonus 3 needs `pip` anyway.

**D2. Which folder a participant opens in VS Code. Tomas: the repo root.**
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

**D3. How participants get the repo and save work. Tomas: fork and clone.**
The fork dialog copies only `main` by default, so the solutions branch does not
come along. Download ZIP stays as the fallback for anyone whose Git setup
fails. Every step in all three projects ends with the same Commit and Sync line.
Saving to GitHub is taught before 21 Nov.

**D4. `moje_hra/` and `moje_analyza/`. Tomas: flatten.**
The subfolders kept participant files apart from `reseni/`. Once solutions leave
`main`, that reason is gone. Working files sit in the project folder, as in finance.

**D5. Who uses the solutions. Tomas: coaches during the day, everyone afterwards.**
- During the workshop the `reseni` branch is a tool for coaches. A coach looks
  at it to help a stuck participant straight away, or when the coach is stuck too.
- The aim is not to lock solutions away, only to not make them easy. A branch
  does that: forks copy only `main`, and no participant material links to it.
- At the end of the workshop participants get the link to the branch, so they
  can compare their work with the solution.
- No catching up by copying. Nobody is handed a finished step to move on. A
  stuck participant works it out with hints and a coach. This drops the earlier
  design assumption that anyone stuck can jump ahead from a solution.

Consequence: the READMEs must not tell participants to copy a solution and
carry on. Wordle and Titanic say that today, and the finance README promises
"dostaneš hotové řešení toho kroku".

**D6. Solutions branch. Tomas: one combined `reseni` branch.**
All three projects' solutions and coach notes live on one branch.

**D7. Names. Tomas: Vojtěch's style throughout.**
- Project folders keep the `projekt-` prefix: `projekt-finance/`, `projekt-wordle/`,
  `projekt-titanic/`.
- Steps folder: `zadani/`.
- Step files: `krokNN_nazev.md`. Hints and bonuses follow the same pattern:
  `napovedy/krokNN_nazev.md`, `bonusy/bonusNN_nazev.md`.
- Titles: `Krok 1 – Název`.
- Code file names stay per project (`finance.py`/`app.py`, `logika.py`/`wordle.py`,
  `analyza.py`/`zprava.py`). The rule is only: one logic file, one runnable file,
  one `test_<logika>.py`, all with names unique in the repo (see D2).
- Numbers always have two digits: `krok01_nazev.md`, `bonus01_nazev.md`,
  `reseni/krok01/`. Wordle has ten steps and finance has eleven bonuses, and
  without the leading zero `krok10_` sorts between `krok1_` and `krok2_`.

**D8. Order inside a step. Tomas: function description first, then tests.**
Finance currently gives tests first, so its steps swap the two sections.

**D9. How tests are handed out. Tomas: ready tests first, own tests later.**
One style for all three projects:
- *Early steps:* the step file contains finished tests. The participant copies
  them in and uses them to confirm quickly that her code works.
- *Later steps:* the participant writes the tests herself, to confirm her own
  implementation. The step file lists what to cover (cases, or a table of calls
  and expected results), not the test code.
- A middle stage with blanks to fill in (`___`) is allowed where it helps.
- Each project owner picks the step where the switch happens.

Wordle and Titanic already work this way. Finance gives ready tests in all six
steps, so its later steps need rework; see the finance TODOs, including the
note about the step 6 tests.

**D10. Wordle game screen. Tomas: stays as step 10.**
It was considered for a bonus only because clearing the screen did not seem to
work when tried. It stays a regular step, so the cause needs finding first: see
the Wordle TODO. Finance and Titanic get screen clearing as a bonus (feedback).

**D11. Charts in Titanic. Tomas: a regular step, placed before the report.**
The text bar chart (today bonus 2) becomes a regular step before the report
step, so the report can include it. It reuses the bar function from finance
step 5, `sloupec(hodnota, nejvyssi, sirka)`: same name, same parameters, same
tests, so both projects teach one design. The plotext charts stay a bonus,
because they need an install.

**D12. HTML report in finance. Tomas: last bonus.**
Feedback said it comes too early and may be dropped. It moves to the end of the
bonuses and can still be removed.

## 4. TODO

### Who does what
- **Wordle and Titanic:** Tomas.
- **Finance:** Vojtěch.
- **Repo-wide items:** whoever gets to them first.

Order: project-specific work first, repo-wide changes after.

### Still open
- Vojtěch reads this file and writes his feedback into it.

### Repo
- [ ] Create branch `reseni` from `main` and move the finance solutions there.
- [ ] Delete stale branches: `projekt-finance` (equals old `main`),
      `projekty-wordle-titanic` (merged), and `projekt-finance-reseni` once moved.
- [ ] Root `README.md`: how the day runs, fork and clone (D3), open the whole repo
      folder (D2), how to run only your project's tests, project table with the new folder links (D7), and that
      the day ends with a show and tell. No mention of solutions.
- [ ] At the end of the workshop, send participants the link to the `reseni` branch (D5).
- [ ] Before the workshop, tell participants to install pytest (D1) and to have a
      GitHub account ready (D3).
- [ ] Root `TAHAK.md`: importing from your own file, writing a test, reading a
      failed test, common error messages. Move this out of the finance tahák
      and out of the Wordle and Titanic READMEs.
- [ ] Keep the root `.vscode/` as the only one; remove the per-project unittest
      settings in Wordle and Titanic (D2).
- [ ] `pytest.ini`: keep `norecursedirs = reseni`, needed on the `reseni` branch.
- [ ] One root `.gitignore` with `statistiky.txt`, `zprava.txt`, `report.html`;
      drop the per-project ones.
- [ ] Add `.gitattributes` with `* text=auto eol=lf`. Windows checkouts already
      produced mixed line endings.
- [ ] A check script on `reseni` that runs pytest in every `krokNN` folder.
- [ ] Solutions are generated, not edited by hand, in all three projects. Each
      owner regenerates and updates `reseni` after changing their project. See
      whether finance's `sestav.py` can be made to serve all three.
- [ ] Coach notes in one place per project: `pro_kouce.md` on `reseni`. Titanic has
      one, finance keeps its notes in `reseni/README.md`, Wordle has none.
- [ ] Update the workshop design doc: pytest, ten Wordle steps as decided, and the
      dropped rule that anyone stuck can catch up from a solution (D5).
- [ ] Final pass for one style across projects (feedback): headings, tables,
      line wrapping, how the participant is addressed.

### Every project
- [ ] Rename to the agreed layout (D7): `zadani/krokNN_nazev.md`, title `Krok N – Název`.
- [ ] Use two-digit numbers in every file and folder name: steps, hints, bonuses
      and solution folders (`krok01_…`, `bonus01_…`, `reseni/krok01/`). Update the
      links in the READMEs and step tables to match.
- [ ] Rewrite each step to the step template: result first, Hotovo když at the end.
- [ ] Hints into `napovedy/`, following the hint rules.
- [ ] Remove every sentence that sends participants to solutions or offers a
      finished step for catching up (D5).
- [ ] Split bonuses into `bonusy/bonusNN_nazev.md`.
- [ ] Add `napady.md`: extension ideas without solutions (high scores,
      difficulty levels, and similar).
- [ ] Add a bonus for clearing the terminal where the project lacks one.
- [ ] README to the README template, including the minimum goal and the
      smoke test in "before you start".
- [ ] Starter test file contains only one test, and it passes. Step 1 tests move
      into the step file (D2).
- [ ] Module and test file names are unique across the repo (D2).
- [ ] Check that input cleaning is practised (feedback): case, `strip`, types,
      positive and negative numbers, dates.
- [ ] Data files are found from the file's own location, not the working folder.
- [ ] Last: test the participant path on Windows and macOS with this project:
      fork, clone, open the repo root, install pytest, Testing panel, Run,
      Commit and Sync.

### Finance
- [ ] Renumber `krok1_…` to `krok01_…`, also in the solution generator (D7).
- [ ] Put the function description before the tests in every step (D8).
- [ ] Move the inline "Nápověda" sections into `napovedy/`.
- [ ] Move "Když zbyde čas" items and bonuses 5 to 11 (no solutions) into `napady.md`.
- [ ] Split bonuses 1 to 4 into separate files, HTML report last (D12).
- [ ] Step 6: build the path to `finance.json` from the file's location.
- [ ] Move shared tahák parts to the root `TAHAK.md`; keep JSON in the project tahák.
- [ ] Adjust the tests to D9: pick the step where ready tests stop, and from
      there on replace the test code with a list of cases the participant tests
      herself.
- [ ] **To figure out:** the step 6 tests use pytest's `tmp_path`, so they do not
      touch the real `finance.json`. Beginners cannot write that themselves, which
      clashes with "own tests in later steps". Either keep these tests ready-made
      as an exception, or explain `tmp_path` briefly in the step.
- [ ] The solution generator takes tests from the step files. Once later steps
      have none, the solution tests need another source.
- [ ] Add the Commit and Sync line to each step (D3).

### Wordle
- [ ] Move `wordle/reseni/` from `main` to the `reseni` branch.
- [ ] Convert tests to pytest functions (D1) in the starter file, the step files
      and the solutions; drop the `class` and `self` note.
- [ ] Rename the folder `wordle/` to `projekt-wordle/` (D7).
- [ ] Flatten `moje_hra/` (D4); rename `kroky/` to `zadani/` and the files to `krokNN_` (D7).
- [ ] Add "result first" and "Hotovo, když" to every step.
- [ ] Review hints against the hint rules; several give most of the function.
- [ ] Step 10 stays (D10). Find out why clearing the screen did not seem to work:
      try it in the VS Code terminal on Windows and macOS.
- [ ] Split the two bonuses into files.
- [ ] Add `napady.md`.
- [ ] `pomocnik.py` looks for the word lists in `moje_hra/` when run from a solution
      folder. Point it at the project folder after flattening.
- [ ] Write `pro_kouce.md` (intro, what to watch for in steps 5 and 6).
- [ ] Build a generator for the solution folders, as finance has (one template,
      marked by step).

### Titanic
- [ ] Move `titanic/reseni/` and `titanic/pro_kouce.md` from `main` to the `reseni` branch.
- [ ] Convert tests to pytest functions (D1) in the starter file, the step files
      and the solutions.
- [ ] Rename the folder `titanic/` to `projekt-titanic/` (D7).
- [ ] Flatten `moje_analyza/` (D4); rename `kroky/` to `zadani/` and the files to `krokNN_` (D7).
- [ ] Write hints for all nine steps; none exist.
- [ ] Add "Hotovo, když" to every step. "Result first" needs care here, because
      the result is the answer. Show the shape of the output with made-up numbers.
- [ ] Turn the text bar chart (bonus 2) into a regular step before the report,
      using finance's `sloupec(hodnota, nejvyssi, sirka)` and its tests (D11).
      Renumber the steps and include the chart in the report step.
- [ ] Split the remaining four bonuses into files.
- [ ] Add `TAHAK.md` for CSV and `None`, and `napady.md`.
- [ ] Add user input somewhere, so input cleaning is practised (for example,
      ask which column to group by in step 9).
- [ ] Every solution folder carries its own copy of the CSV. Keep one copy in the
      project folder and point the solutions at it.
- [ ] Build a generator for the solution folders, as finance has.

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
