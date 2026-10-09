# Generation checklist

The repository is built in the requested order. Each bank is written fully before the next one. No entries are placeholders.

- [x] Folder structure: tools/ and verification/
- [x] README.md: full theory and conventions
- [x] pseudocode-writing-questions.md: 60 questions
- [x] pseudocode-writing-answers.md: 60 matching solutions
- [x] output-prediction-questions.md: 100 questions
- [x] output-prediction-answers.md: 100 matching solutions
- [x] error-detection-questions.md: 75 faulty programs
- [x] error-detection-answers.md: 75 matching repairs
- [x] mock-tests.md: 3 × 30 questions
- [x] mock-test-answers.md: 90 matching solutions
- [x] last-minute-revision.md: schedule, checklist and rubric
- [x] Verification: ID coverage, execution checks, boundary cases and option uniqueness


Verified 235 bank questions and 90 mock entries with exact question/answer ID order. See verification/report.json for methods and limitations. Re-run `python tools/build_repository.py` to regenerate and validate. The builder emits the requested files sequentially after the teaching guide.
