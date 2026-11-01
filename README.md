# GradeTargetCalc.com
A dependency-free static educational website, designed for GitHub Pages.

## Current status
Built and locally checked; **deployment in progress**. Public repository: https://github.com/abidtashifain-maker/GradeTargetCalc. GitHub connection verified for abidtashifain-maker. Owner-approved contact: Info@gradetargetcalc.com. Registrar: IONOS. Public repository creation, publishing and domain connection are owner-approved. GitHub browser sign-in completed and repository created. IONOS account access, Search Console and AdSense access remain pending. Repository name: GradeTargetCalc. SEO metric validation is incomplete without an authorized dataset. See docs/SEO-STRATEGY.md.

## Agent maintenance
- Build: `python3 scripts/build.py` (draft/noindex by default).
- Test: `npm test` (Node 22+, Python 3; no package installation).
- Release: after explicit public launch approval, set `public_launch_approved` to true in site-config.json and build with `PUBLIC_RELEASE=1`, then test. Contact defaults to the owner-approved address in site-config.json; CONTACT_EMAIL can override it. Confirm privacy disclosures match the live host before launch.
- GitHub Actions can use the CONTACT_EMAIL repository variable; an unset value falls back to site-config.json. Production builds require an address and recorded public-launch approval. The email address is public, not a secret credential.
- Publish dist using the included workflow after enabling Pages with GitHub Actions.
- CNAME and metadata assume gradetargetcalc.com at the domain root, not a repository subpath. For a temporary repository URL, use a separate preview configuration; do not claim root-relative assets work under /repository/.
- dist/assets are authored source assets and must be retained. The generator creates HTML and SEO files without clearing those assets.
- Do not add analytics, ads, publisher IDs, verification tokens or consent notices until actual account details and applicable consent behavior are configured.

## Scope
Seven tools cover final grade (required and resulting), weighted assessments/module marks, semester GPA, cumulative GPA, percentages, test scores and equal-weight averages. Semester GPA intentionally shares a page with general GPA. Numeric GPA inputs avoid universal conversion claims. No school-specific classification, dropped-score, curve, extra-credit or retake rule is implied.
